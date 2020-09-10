```
 _                     _ _ _               _ _ _     
| |                   | (_) |             | (_) |    
| |__   __ _ _ __   __| |_| |_ _ __  _   _| |_| |__  
| '_ \ / _` | '_ \ / _` | | __| '_ \| | | | | | '_ \ 
| |_) | (_| | | | | (_| | | |_| |_) | |_| | | | |_) |
|_.__/ \__,_|_| |_|\__,_|_|\__| .__/ \__, |_|_|_.__/ 
                              | |     __/ |          
                              |_|    |___/                
```

A lightweight python library for bandit algorithms

![Unit Test](https://github.com/Alanthink/banditpylib/workflows/Unit%20Test/badge.svg?branch=master) ![Style Check](https://github.com/Alanthink/banditpylib/workflows/Style%20Check/badge.svg?branch=master)

## Features

* object-oriented design
* multiprocesses support
* friendly runtime info

## Getting Started

### Installing

```shell
# run under `banditpylib` root directory
pip install -e .
```

### Example

Suppose we want to run algorithms *Epsilon Greedy*, *UCB* and *Thompson Sampling*, which aim to maximize the total rewards, against the ordinary multi-armed bandit environment with 3 *Bernoulli* arms. The following code blocks show the main logic. 

#### setup bandit envoronment

```python
# real means of Bernoulli arms
means = [0.3, 0.5, 0.7]
# create Bernoulli arms
arms = [BernoulliArm(mean) for mean in means]
# create an ordinary multi-armed bandit environment
bandit = OrdinaryBandit(arms=arms)
```

#### create learners

```python
# horizon of the game
horizon = 2000
# create learners aiming to maximize the total rewards
learners = [EpsGreedy(arm_num=len(arms), horizon=horizon),
            UCB(arm_num=len(arms), horizon=horizon),
            ThompsonSampling(arm_num=len(arms), horizon=horizon)]
```

#### setup simulator and play the game

```python
# for each setup we run 200 trials
trials = 200
# record intermediate regrets for each trial
intermediate_regrets = list(range(0, horizon+1, 50))
# simulator
game = SinglePlayerProtocol(bandit=bandit,
                            learners=learners,
                            intermediate_regrets=intermediate_regrets)
# start playing the game
# add `debug=True` for debugging purpose
game.play(trials=trials)
```

The following figure shows the simulation results.

![output example](example.jpg)

Please check this [notebook](examples/ordinary_bandit.ipynb) to figure out more details.

### Running the Tests

```shell
# run all tests
pytest
```

## Implemented Policies

### Single Player Protocol

#### Regret Minimization

| Bandit Type | Policies |
|     :---      |      :--- |
| Ordinary Bandit   | `Uniform`, `EpsGreedy`, `UCB`, `ThompsonSampling`, `UCBV`, `MOSS` |
| Ordinary MNL Bandit   | `EpsGreedy`, `UCB`, `ThompsonSampling` |

#### Fixed Budget Best Arm Identification

| Bandit Type | Policies |
|     :---      |      :--- |
| Ordinary Bandit   | `Uniform`, `SR`, `SH`|

#### Fixed Confidence Best Arm Identification

| Bandit Type | Policies |
|     :---      |      :--- |
| Ordinary Bandit   | `ExpGap`, `LilUCBHeuristic`|

For a detailed description, please check the [documentation](https://alanthink.github.io/banditpylib-doc/).

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Acknowledgments

* This project is inspired by [libbandit](https://github.com/tor/libbandit) and [banditlib](https://github.com/jkomiyama/banditlib) which are both c++ libraries for bandit algorithms.
* This readme file is following the style of [README-Template.md](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2).
* The title is generated by [TAAG](http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20).
