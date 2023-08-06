# gym_toytext

This repository contains the text environments previously present in OpenAI Gym <0.20. These environments had been in the master branch of [openai/gym](https://github.com/openai/gym/) but later excluded in [this pull](https://github.com/openai/gym/pull/2384/).


### List of environments

| environment | commit history | first committer |
| --- | --- | --- |
| `GuessingGame-v0` | [`guessing_game.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/guessing_game.py) | @JKCooper2 |
| `HotterColder-v0` | [`hotter_colder.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/hotter_colder.py) | @JKCooper2 |
| `KellyCoinflip-v0` and `KellyCoinflipGeneralized-v0` | [`kellycoinflip.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/kellycoinflip.py) | @gwern |
| `NChain-v0` | [`nchain.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/nchain.py) | @machinaut |
| `Roulette-v0` | [`roulette.py`](https://github.com/openai/gym/commits/master/gym/envs/toy_text/roulette.py) | @gdb |


### Compatibility

```
gym>=0.20,<0.25
```

### Install

```
pip install gym-toytext
```

### Usage

```python
import gym
import gym_toytext

env = gym.make("Roulette-v0")
```
