# DI-searching

Decision Intelligence heuristic searching and optimization platform


## Introduction

**DI-searching** is a heuristic searching and optimization platform with various Decision Intelligence methods such as Genetic Algorithm, Bayesian Optimization and Reinforcement Learning etc. It can be used to handle combinatorial optimization problems and non-gradient search problems.

**DI-searching** is a fundamental platform under [**OpenDILab**](http://opendilab.org/) and it uses [**DI-engine**](https://github.com/opendilab/DI-engine) to build RL searching pipelines.


## Outlines
- [DI-searching](#di-searching)
  - [Introduction](#introduction)
  - [Outlines](#outlines)
  - [Installation](#installation)
  - [Quick start](#quick-start)
  - [Engine Zoo](#engine-zoo)
  - [License](#license)


## Installation

You can simply install DI-searching with `pip` from the source code.

```bash
pip install --user .
python -c 'import disearch'
```

It will automatically install **DI-engine** together with its requirement packages i.e. **PyTorch**.

## Quick start

**DI-searching** defines core algorithm and searching methods as `Engine`. You can define a searching `Engine` with a search `Space`
together with your config dict.
**DI-searching** provides two kinds of searching flow for a provided target function listed as follow.

1. Interactive Procedure

It is done by calling `Engine`'s `propose` and `update_score` method, in which you can flexibly define the searching procedure. You can call the `provide_best` method at any time to get the currently best candidate sample and its score. Here's an simple example:

```python
def target_func(x):
    ...
    return score

space = YourSearchSpace(shape=(...))
engine = YourEngine(config, search_space)

for i in range(max_iterations):
    samples = engine.propose(sample_num)
    scores = [target_func(x) for x in samples]
    engine.update_score(samples, scores)

print(engine.provide_best())
```

2. Functional Procedure

It is done by calling the `search` method of `Engine`, with target function provided as input. The engine will autometically search the best samples of the target according to the config. Here's an example:

```python
def target_func(x):
    ...
    return score

space = YourSearchSpace(shape=(...))
engine = YourEngine(config, search_space)

engine.search(target_func)

print(engine.provide_best())
```

3. Reinforcement Learning Procedure

When using a Reinforcement Learning searching `Engine`, users need to provide an RL `Policy` defined in **DI-engine** form, and some other RL workers in **DI-engine** such as `Collector`, `Learner`, `ReplayBuffer` are supposed to be used in the searching `Engine`. In the searching procedure, a target `Env` is used instead of a function. So we suggest to use the `search` method to if the user is not familiar with the RL pipeline of **DI-engine**. Here's an example.

```python
def target_func(x):
    ...
    return score

rl_config = EasyDict(dict(...))
space = YourSearchSpace(shape=(...))
policy = YourPolicy(rl_config.policy, ...)
engine = BaseRLEngine(rl_cfg, space, policy)

engine.search(target_func)

print(engine.provide_best())
```

## Engine Zoo

- Genetic Algorithm
- Bayesian Optimization
- RL

## License

`DI-searching` released under the Apache 2.0 license.
