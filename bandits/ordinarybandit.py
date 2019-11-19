from absl import logging

from arms import Arm
from .utils import Bandit

__all__ = ['OrdinaryBandit']

class OrdinaryBandit(Bandit):
  """Ordinary bandit model
  Arms are numbered from 0 to len(arms)-1 by default.
  """

  def __init__(self, arms):
    logging.info('Ordinary bandit model')
    if not isinstance(arms, list):
      logging.fatal('Arms should be given in a list!')
    for arm in arms:
      if not isinstance(arm, Arm):
        logging.fatal('Not an arm!')
    self.__arms = arms

    self.__arm_num = len(arms)
    if self.__arm_num < 2:
      logging.fatal('The number of arms should be at least two!')

    sorted_mean = sorted([(arm.mean, arm) for arm in self.__arms],
        key=lambda x:x[0])
    self.__best_arm = sorted_mean[-1][1]

    self.__type = 'ordinarybandit'

  @property
  def arm_num(self):
    """return number of arms"""
    return self.__arm_num

  @property
  def type(self):
    return self.__type

  @property
  def context(self):
    return None

  @property
  def _oracle_context(self):
    return self.__best_arm, self.__arms

  def init(self):
    self.__max_rewards = 0

  def _update_context(self):
    pass

  def _take_action(self, action):
    best_arm, arms = self._oracle_context

    is_list = True
    if not isinstance(action, list):
      is_list = False
      action = [(action, 1)]

    rewards = []
    for pair in action:
      arm = pair[0]
      if arm not in range(self.arm_num):
        logging.fatal('Wrong arm index!')

      rewards.append(arms[arm].pull(pair[1]))
      self.__max_rewards += (best_arm.mean * pair[1])

    if not is_list:
      # rewards[0] is a numpy array with size 1
      return (rewards[0][0],)
    return (rewards,)

  def regret(self, rewards):
    return self.__max_rewards - rewards

  def best_arm_regret(self, ind):
    return 1 - (self.__best_arm == ind)
