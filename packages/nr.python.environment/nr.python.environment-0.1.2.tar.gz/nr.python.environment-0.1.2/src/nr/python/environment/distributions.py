""" Inspect a Python environment for all installed packages. """

import dataclasses
import sys
from typing import Any, Dict, Iterable, List, Optional, Set, Union

import pkg_resources


@dataclasses.dataclass
class Distribution:
    """Additional metadata for a distribution."""

    name: str
    location: str
    version: str
    license_name: Optional[str]
    platform: Optional[str]
    requires_python: Optional[str]
    requirements: List[str]
    extras: Set[str]

    @staticmethod
    def from_pkg_resources(dist: pkg_resources.Distribution) -> "Distribution":
        from email.parser import Parser

        data = Parser().parsestr(dist.get_metadata(dist.PKG_INFO))

        return Distribution(
            name=dist.project_name,
            location=dist.location,
            version=data.get("Version"),
            license_name=data.get("License"),
            platform=data.get("Platform"),
            requires_python=data.get("Requires-Python"),
            requirements=data.get_all("Requires-Dist") or [],
            extras=set(data.get_all("Provides-Extra") or []),
        )

    @staticmethod
    def from_json(data: Dict[str, Any]) -> "Distribution":
        dist = Distribution(**data)
        dist.extras = set(data["extras"])
        return dist

    def to_json(self) -> Dict[str, Any]:
        result = {field.name: getattr(self, field.name) for field in dataclasses.fields(self)}
        result["extras"] = list(self.extras)
        return result


class DistributionCollector:
    distributions: Dict[str, Distribution]

    def __init__(self) -> None:
        self.distributions = {}

    def collect(self, requirement: Union[str, pkg_resources.Requirement], recursive: bool = True) -> Distribution:
        """Collect the distribution named *dist_name*.

        :param requirement: The distribution name or requirement to collect.
        :param recursive: Whether to recursively collect the dependencies of the distribution.
        """

        if isinstance(requirement, str):
            requirement = next(pkg_resources.parse_requirements(requirement))

        if requirement.project_name in self.distributions:
            return self.distributions[requirement.project_name]

        dist = Distribution.from_pkg_resources(pkg_resources.get_distribution(requirement))
        self.distributions[dist.name] = dist

        if recursive:
            for dep in dist.requirements:
                self.collect(dep, recursive=True)

        return dist

    def collect_multiple(self, requirements: Iterable[Union[str, pkg_resources.Requirement]]) -> None:
        for requirement in requirements:
            self.collect(requirement)

    def collect_all(self, sys_path: Optional[Iterable[str]] = None) -> None:
        for path in sys_path or sys.path:
            for dist in pkg_resources.find_distributions(path):
                self.distributions[dist.project_name] = Distribution.from_pkg_resources(dist)


def get_distributions() -> Dict[str, Distribution]:
    collector = DistributionCollector()
    collector.collect_all()
    return collector.distributions
