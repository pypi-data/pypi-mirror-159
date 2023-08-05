import numpy as np
import warnings
from collections import deque
from typing import Callable, Dict, Any, Tuple
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern
from scipy.optimize import minimize
from scipy.stats import norm

from .base_search_engine import BaseSearchEngine, ENGINE_REGISTRY
from disearch.problem import ProblemHandler


def ucb(x, gp, kappa):
    mean, std = gp.predict(x, return_std=True)
    return mean + kappa * std


def ei(x, gp, y_max, xi):
    mean, std = gp.predict(x, return_std=True)
    a = (mean - y_max - xi)
    z = a / std
    return a * norm.cdf(z) + std * norm.pdf(z)


def poi(x, gp, y_max, xi):
    mean, std = gp.predict(x, return_std=True)
    z = (mean - y_max - xi) / std
    return norm.cdf(z)


@ENGINE_REGISTRY.register('bo')
class BayesianOptimizationEngine(BaseSearchEngine):
    """
    The searching engine of Bayesian Optimization algorithm. The engine takes a function to optimize
    in a discrete space as well as the bounds in order to find the value for samples yield the maximum
    targets using bayesian optimization.

    :param Dict cfg: user config
    :param BaseSpace search_space: searching space of engine
    """

    config = dict(
        init_point=5,
        max_iterations=25,
        acquisition='ucb',
        kappa=2.576,
        kappa_decay=1,
        kappa_decay_delay=0,
        xi=0.0,
        verbose=False,
    )

    def __init__(
            self,
            cfg: Dict,
            search_space: "BaseSpace",  # noqa
            random_state: Any = None,
    ) -> None:
        super().__init__(cfg, search_space, random_state)

        self._gp = GaussianProcessRegressor(
            kernel=Matern(nu=2.5),
            alpha=1e-6,
            normalize_y=True,
            n_restarts_optimizer=5,
            random_state=self._random_state,
        )
        self._handler = ProblemHandler(search_space)

        self._queue = deque()

        self._init_point = self._cfg.init_point
        self._max_iterations = self._cfg.max_iterations
        self._kappa = self._cfg.kappa
        self._kappa_decay = self._cfg.kappa_decay
        self._kappa_decay_delay = self._cfg.kappa_decay_delay
        self._xi = self._cfg.xi
        assert self._cfg.acquisition in ['ucb', 'ei', 'poi'], self._cfg.acquisition
        self._acquire_type = self._cfg.acquisition
        self._verbose = self._cfg.verbose

    def reset(self) -> None:  # noqa
        self._handler.clear()
        self._queue.clear()
        self._gp = GaussianProcessRegressor(
            kernel=Matern(nu=2.5),
            alpha=1e-6,
            normalize_y=True,
            n_restarts_optimizer=5,
            random_state=self._random_state,
        )

    def _predict(self, x, y_max):
        if self._acquire_type == 'ucb':
            return ucb(x, self._gp, self._kappa)
        elif self._acquire_type == 'ei':
            return ei(x, self._gp, y_max, self._xi)
        elif self._acquire_type == 'poi':
            return poi(x, self._gp, y_max, self._xi)
        else:
            raise ValueError('Unknown aquisition type:', self._acquire_type)

    def _acquisition_max(self, n_warmup=10000, n_iter=10):
        x_tries = np.array([self._search_space.sample() for _ in range(n_warmup)])
        y_max = self._handler.best_score
        ys = self._predict(x_tries, y_max)
        x_max = x_tries[ys.argmax()]
        max_acq = ys.max()

        x_seeds = np.array([self._search_space.sample() for _ in range(n_iter)])
        for x_try in x_seeds:
            res = minimize(
                lambda x: -self._predict(x.reshape(1, -1), y_max=y_max),
                x_try.reshape(1, -1),
                bounds=self._search_space.bounds,
                method="L-BFGS-B"
            )

            if not res.success:
                continue

            try:
                fun = -res.fun[0]
            except TypeError:
                fun = -res.fun

            if max_acq is None or -fun > max_acq:
                x_max = res.x
                max_acq = fun

        return np.clip(x_max, self._search_space.bounds[:, 0], self._search_space.bounds[:, 1])

    def search(self, target_func: Callable) -> Tuple[np.ndarray, float]:  # noqa
        init_point = self._init_point
        if len(self._queue) == 0 and len(self._handler) == 0:
            init_point = max(init_point, 1)
        for i in range(init_point):
            sample = self._search_space.sample()
            self._queue.append(sample)

        iterations = 0
        while len(self._queue) > 0 or iterations < self._max_iterations:
            if len(self._queue) > 0:
                sample = self._queue.pop()
            else:
                sample = self.propose()
                iterations += 1
            sample = sample.reshape(1, -1)
            score = self._handler.get_score(sample, target_func)
            self.update_score(sample, score)
            best_sample, best_score = self._handler.provide_best()
            if not self._verbose:
                print(" Iteration {} best score: {:.4f} .".format(iterations + 1, best_score))
        return best_sample, best_score

    def propose(self, sample_num: int = 1) -> np.ndarray:
        sample_list = []
        while len(sample_list) < sample_num:
            if len(self._queue) > 0:
                candidate = self._queue.pop()
            else:
                candidate = self._acquisition_max()
            sample_list.append(candidate)
        return np.array(sample_list)

    def update_score(self, sequences: np.ndarray, scores: np.ndarray) -> None:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            self._gp.fit(sequences, scores)

    def provide_best(self) -> Tuple[np.ndarray, np.ndarray]:
        return self._handler.provide_best()
