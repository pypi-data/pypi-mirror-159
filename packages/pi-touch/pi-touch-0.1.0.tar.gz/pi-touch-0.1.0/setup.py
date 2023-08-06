import getpass
import io
import os
import sys
from pathlib import Path
from shutil import rmtree

from setuptools import Command, find_packages, setup

# Package meta-data
NAME = "pi-touch"
DESCRIPTION = "Control PI Touch Screen with GPIO"
URL = ""
EMAIL = "estasney@users.noreply.github.com"
AUTHOR = "Eric Stasney"
REQUIRES_PYTHON = ">=3.9.0"

REQUIRED = ["click", "RPi.GPIO"]

EXTRAS = {}

here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = "\n" + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


class BaseCommand(Command):
    def run(self) -> None:
        raise NotImplementedError

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class BuildCommand(BaseCommand):
    """Build packages"""

    description = "Build package"
    user_options = []

    def run(self):
        self.status("Removing Old Builds")
        try:
            rmtree(os.path.join(here, "build"))
        except OSError:
            pass
        self.status("Removing Old Distributions")
        try:
            rmtree(os.path.join(here, "dist"))
        except OSError:
            pass
        os.system("python setup.py build sdist bdist_wheel")
        self.status("Done")
        sys.exit()


class UploadCommand(BaseCommand):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options = []

    def run(self):
        self.status("Uploading the package to PyPI via Twine...")
        import keyring

        dist_path = str(Path(here) / "dist" / "*")

        os.system(
                f"twine upload -u {getpass.getuser()} -p {keyring.get_password('TWINE', getpass.getuser())} {dist_path}"
                )

        sys.exit()


setup(
        name=NAME,
        version="0.1.0",
        description=DESCRIPTION,
        long_description=long_description,
        long_description_content_type="text/markdown",
        author=AUTHOR,
        author_email=EMAIL,
        python_requires=REQUIRES_PYTHON,
        url=URL,
        packages=find_packages(exclude=("tests",)),
        install_requires=REQUIRED,
        extras_require=EXTRAS,
        include_package_data=False,
        data_files=[],
        license="MIT",
        entry_points="""
    [console_scripts]
    pi-touch-screen=pi_touch.cli:run_manager
    """,
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python",
            ],
        cmdclass={"upload": UploadCommand, "package": BuildCommand},
        )
