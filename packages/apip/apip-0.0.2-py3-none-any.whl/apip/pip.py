from .abc import Package
from .abc import errors
import subprocess
import re

class Pip:
    def __init__(self, index="https://pypi.org/simple"):
        self.index = index

    def install(self, package, version=None):
        return Package(package, version).install(self.index)

    def uninstall(self, package):
        Package(package).uninstall()

    def list(self):
        packages = []
        output = subprocess.run(["pip", "list"], capture_output=True)
        output = output.stdout.decode()
        output = ' '.join(output.splitlines()[2:])
        output = re.findall('(?! )[a-zA-Z\d\.\-]*', output)
        it = iter(output)
        joined = [[a, b] for a, b in zip(it, it)]
        for index, item in enumerate(joined):
            if item == "":
                output.pop(index)
                continue
            packages.append(Package(item[0], item[1]))
        return packages

    def get(self, package):
        packages = self.list()
        included = False
        index = None
        for i, pkg in enumerate(packages):
            if pkg.name == package:
                included = True
                index = i

        if not included:
            raise errors.PackageNotFoundException(
                f"{package} is not installed!"
            )
        return Package(package, packages[index].version)
