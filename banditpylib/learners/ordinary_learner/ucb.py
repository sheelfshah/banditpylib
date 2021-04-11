from typing import List, Tuple, Optional

import numpy as np

from banditpylib.arms import PseudoArm
from .utils import OrdinaryLearner


class UCB(OrdinaryLearner):
  r"""Upper Confidence Bound policy :cite:`auer2002finite`

  At time :math:`t`, play arm

  .. math::
    \mathrm{argmax}_{i \in [0, N-1]} \left\{ \bar{\mu}_i(t) + \sqrt{ \frac{
    \alpha  \ln(t) }{T_i(t)} } \right\}
  """
  def __init__(self, arm_num: int, name: str = None, alpha: float = 2.0):
    """
    Args:
      arm_num: number of arms
      name: alias name
      alpha: alpha
    """
    super().__init__(arm_num=arm_num, name=name)
    if alpha <= 0:
      raise Exception('Alpha %.2f in %s is no greater than 0!' %
                      (alpha, self.__name))
    self.__alpha = alpha

  def _name(self) -> str:
    """
    Returns:
      default learner name
    """
    return 'ucb'

  def reset(self):
    """Reset the learner

    .. warning::
      This function should be called before the start of the game.
    """
    self.__pseudo_arms = [PseudoArm() for arm_id in range(self.arm_num())]
    # current time step
    self.__time = 1

  def UCB(self) -> np.ndarray:
    """
    Returns:
      optimistic estimate of arms' real means
    """
    ucb = np.array([
        arm.em_mean +
        np.sqrt(self.__alpha * np.log(self.__time) / arm.total_pulls())
        for arm in self.__pseudo_arms
    ])
    return ucb

  def actions(self, context=None) -> Optional[List[Tuple[int, int]]]:
    """
    Args:
      context: context of the ordinary bandit which should be `None`

    Returns:
      arms to pull
    """
    del context
    if self.__time <= self.arm_num():
      self.__last_actions = [((self.__time - 1) % self.arm_num(), 1)]
    else:
      self.__last_actions = [(np.argmax(self.UCB()), 1)]
    return self.__last_actions

  def update(self, feedback: List[Tuple[np.ndarray, None]]):
    """Learner update

    Args:
      feedback: feedback returned by the bandit environment by executing
        :func:`actions`
    """
    self.__pseudo_arms[self.__last_actions[0][0]].update(feedback[0][0])
    self.__time += 1
