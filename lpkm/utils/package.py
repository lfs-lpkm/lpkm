from typing import List


class Package:
    def __init__(
        self,
        name: str,
        version: str,
        deps: List["Package"],
        make_deps: List["Package"],
    ) -> None:
        self._name = name
        self._version = version
        self._deps = deps
        self._make_deps = make_deps

        self._fullname = f"{self.name}-{self.version}"

    def __str__(self) -> str:
        return self.fullname

    def __repr__(self) -> str:
        return self.fullname

    def __eq__(self, other):
        return self.fullname == other.fullname

    def __gt__(self, other: "Package"):
        # For package named "nano" it depends on "libc" then it means that "nano > libc"
        # This is just for resolving purposed only
        return self.depends_on(other)

    def __lt__(self, other: "Package"):
        return other.depends_on(self)

    def depends_on(self, other: "Package"):
        return other in self.deps

    @property
    def name(self):
        return self._name

    @property
    def version(self):
        return self._version

    @property
    def deps(self):
        return self._deps

    @property
    def make_deps(self):
        return self._make_deps

    @property
    def fullname(self):
        return self._fullname


def resolve_packages_deps(packages: List[Package]) -> List[Package]:
    resolved_packages = []

    def add_packages(pkgs: List[Package]):
        for pkg in pkgs:
            if pkg in resolved_packages:
                continue
            resolved_packages.append(pkg)
            add_packages(pkg.deps)

    add_packages(packages)
    return sorted(resolved_packages)
