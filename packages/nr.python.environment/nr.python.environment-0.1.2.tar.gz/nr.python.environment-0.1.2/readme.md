# nr.python.environment

Utilities to work with Python environments.

### API

*function* __`nr.python.environment.distributions.get_distributions(): Dict[str, Distribution]`__

Returns all distributions that can be found in the current Python environment. This can be useful to build a dependency
graph or to collect the license of all packages used.
