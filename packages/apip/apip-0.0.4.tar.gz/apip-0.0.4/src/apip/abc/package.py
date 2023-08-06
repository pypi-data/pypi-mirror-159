from __future__ import annotations
import subprocess
from . import errors


class Package:
    def __init__(self, name: str, version: str = None):
        self.name = name
        self.version = version

    def shellify(self, command: str) -> list:
        return command.split()

    def err_checking(self, output):
        name = self.name
        name += f"[{self.version}]" if self.version else ""
        name += f"=={self.version}" if self.version else ""
        not_found = f"ERROR: Could not find a version that satisfies the requirement {name} (from versions: {self.version})\
        \nERROR: No matching distribution found for {name}"
        if not_found in output:
            raise errors.PackageNotFoundException(
                f"{self.name} is not a valid package!"
            )
        not_found = f"ERROR: No matching distribution found for {self.name}=={self.version}"
        if not_found in output:
            raise errors.VersionNotFoundException(
                f"{self.version} does not exist!"
            )
        invalid_connection = f"WARNING: Retrying (Retry(total=0, connect=None, read=None, redirect=None, status=None)) \
        after connection broken by "
        not_found = f"ERROR: Could not find a version that satisfies the requirement {name} (from versions: {self.version})\
                \nERROR: No matching distribution found for {name}"
        if invalid_connection in output and not_found in output:
            raise errors.ConnectionException(
                f"PyPi could not be reached! Full error: {output}"
            )
        not_installable = f"ERROR: Directory '{name}' is not installable. Neither setup.py nor 'pyproject.toml' found."
        if not_installable in output:
            raise errors.PackageNotFoundException(
                f"{name} is not a valid package!"
            )

    def install(self, index) -> Package:
        empty = ""
        version = f"=={self.version}"
        command = f"pip install --index-url {index} {self.name}{version if self.version else empty}"
        out = subprocess.run(self.shellify(command), capture_output=True)
        self.err_checking(out.stderr.decode())
        stdout = out.stdout.decode()
        try:
            version = stdout.split(f"{self.name}-")[1]
        except IndexError:
            pass
        return Package(self.name, version)

    def uninstall(self):
        out = subprocess.run(self.shellify(f"pip uninstall {self.name} -y"), capture_output=True)
        out = out.stderr.decode()
        not_installable = f"ERROR: Directory '{self.name}' is not installable. Neither setup.py nor 'pyproject.toml' \
                          found."
        if not_installable in out:
            raise errors.PackageNotFoundException(
                f"{self.name} is not a valid package!"
            )
        invalid_package = f"WARNING: Skipping {self.name} as it is not installed."
        if invalid_package in out:
            raise errors.PackageNotFoundException(
                f"{self.name} is not installed!"
            )

    def __str__(self):
        return f"{self.name}=={self.version}"

    def __repr__(self):
        version = f", {self.version}"
        empty = ""
        return f"pipapi.abc.package.Package({self.name}{version if self.version else empty})"
