"""
This file is part of clcell which is released under MIT.
See file LICENSE for full license details.
"""


from pkg_resources import get_distribution, DistributionNotFound

from .core import CASimulator, RuleSet


# Set version number.
try:
	__version__ = get_distribution(__name__).version
except DistributionNotFound:
	__version__ = ""


# Rules for Conway's Game of Life.
LIFE = RuleSet(
	unpopulated=[False, False, False, True, False, False, False, False, False],
	populated=[False, False, True, True, False, False, False, False, False]
)
