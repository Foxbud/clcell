# clcell 

**clcell** is an OpenCL-accelerated cellular automata simulator for Python 3.

## Features

- OpenCL-based hardware acceleration
- Custom rulesets via `clcell.RuleSet`
- Parallel simulations via `clcell.CASimulator.batch_simulate`

## Limitations

- Only binary cell states
- No support for infinite grids
- Grid boundary cells must be unpopulated

## Installation

Regardless of the installation method you choose, you will need
[OpenCL](https://www.khronos.org/opencl/) drivers for your hardware.

### Using pip

```
$ pip install --user clcell
```

### Building from Source

Requirements:
- [GNU Make](https://www.gnu.org/software/make/)
- [Futhark](https://futhark-lang.org/)
- [setuptools](https://pypi.org/project/setuptools/)

Clone this repository:

```
$ git clone https://github.com/Foxbud/clcell.git
```

Enter the project directory:

```
$ cd clcell
```

Build and install this package:

```
$ make install
```

##  Usage

```Python
import numpy as np
import clcell

# Instantiate a simulator using Conway's Game of Life as the ruleset.
sim = clcell.CASimulator(clcell.LIFE)

# Create a randomized game state to use as a seed.
seed_state = np.random.randint(0, 2, (1023, 1023), dtype=np.int8)
# Pad state with zeros (required for now).
seed_state = np.pad(seed_state, 1, constant_values=0)

# Simulate 10,000 generations based on that seed.
final_state = sim.simulate(10000, seed_state)

# Create a batch of 1,000 randomized, padded game states to use as seeds.
seed_states = np.array([
  np.pad(
    np.random.randint(0, 2, (127, 127), dtype=np.int8),
    1,
    constant_values=0
  )
  for num
  in range(1000)
])

# Simulate 1,000 generations based on each of those seeds.
final_states = sim.batch_simulate(1000, seed_states)
```

## Changelog

**v1.0.0**
- Initial release.
