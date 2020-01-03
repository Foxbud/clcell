"""
This file is part of clcell which is released under MIT.
See file LICENSE for full license details.
"""


import numpy as np

from . import device_api


class CASimulator:
	def __init__(self, ruleset, platform=None, device=None):
		self._ruleset = ruleset
		self._api = device_api.device_api(
			platform_pref=platform,
			device_pref=device
		)

	def simulate(self, num_steps, seed_state):
		return self._api.simulate(
			self._ruleset._raw,
			num_steps,
			np.array(seed_state, dtype=np.int8)
		)

	def batch_simulate(self, num_steps, seed_states):
		return self._api.batch_simulate(
			self._ruleset._raw,
			num_steps,
			np.array(seed_states, dtype=np.int8)
		)


class RuleSet:
	def __init__(self, unpopulated, populated):
		self.unpopulated = tuple(unpopulated)
		self.populated = tuple(populated)
		self._raw = np.concatenate(
			(
				np.array(self.unpopulated, dtype=np.int8),
				np.array(self.populated, dtype=np.int8),
			)
		)
