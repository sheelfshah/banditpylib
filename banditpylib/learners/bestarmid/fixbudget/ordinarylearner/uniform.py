from .utils import OrdinaryLearner

__all__ = ['Uniform']


class Uniform(OrdinaryLearner):
  """sample each arm the same number of times"""

  def __init__(self, pars):
    super().__init__(pars)

  @property
  def name(self):
    if self._name:
      return self._name
    return 'Uniform'

  def _learner_reset(self):
    pass

  def learner_round(self):
    for r in range(self._budget):
      action = r % self._arm_num
      feedback = self._bandit.feed(action)
      self._model_update(action, feedback)

  def best_arm(self):
    return max([(ind, arm.em_mean)
                for (ind, arm) in enumerate(self._em_arms)],
               key=lambda x: x[1])[0]
