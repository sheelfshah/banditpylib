import math

import numpy as np

from absl import flags

from .utils import OrdinaryLearner

FLAGS = flags.FLAGS

__all__ = ['lilUCB_heur']


class lilUCB_heur(OrdinaryLearner):
  """lilUCB heuristic"""

  def __init__(self, pars):
    super().__init__(pars)

  @property
  def name(self):
    if self._name:
      return self._name
    return 'lilUCB_heur'

  def __bonus(self, times):
    if (1+self.__eps)*times == 1:
      return math.inf
    return (1+self.__beta)*(1+math.sqrt(self.__eps))* \
        math.sqrt(2*(1+self.__eps)* \
        math.log(math.log((1+self.__eps)*times)/self.__delta)/times)

  def _learner_reset(self):
    # alg parameters suggested by the paper
    self.__beta = 0.5
    self.__a = 1+10/self._arm_num
    self.__eps = 0
    self.__delta = self._fail_prob/5
    # total number of pulls used
    self.__t = 0

  def learner_round(self):
    # sample each arm once for the initialization step
    action = [(ind, 1) for ind in range(self._arm_num)]
    feedback = self._bandit.feed(action)
    self._model_update(action, feedback)
    self.__t = self._arm_num

    while True:
      for arm in self._em_arms:
        if arm.pulls >= (1+self.__a*(self.__t-arm.pulls)):
          return
      ucb = np.array([arm.em_mean+self.__bonus(arm.pulls) \
          for arm in self._em_arms])
      action = np.argmax(ucb)
      feedback = self._bandit.feed(action)
      self._model_update(action, feedback)
      self.__t += 1

  def best_arm(self):
    return max([(ind, arm.pulls)
                for (ind, arm) in enumerate(self._em_arms)],
               key=lambda x: x[1])[0]
