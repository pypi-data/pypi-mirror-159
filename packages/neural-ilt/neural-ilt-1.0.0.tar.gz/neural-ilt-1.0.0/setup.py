from pathlib import Path
from typing import List

from setuptools import find_packages, setup

# Package meta-data.
NAME = "neural-ilt"
AUTHOR = ""
EMAIL = ""
URL = "https://github.com/cuhk-eda/neural-ilt"
DESCRIPTION = "Litography mask generation with neural networks"
REQUIRES_PYTHON = ">=3.6.0"

# Load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).absolute().parent
REQUIREMENTS_DIR = ROOT_DIR / "requirements"
PACKAGE_DIR = ROOT_DIR / "neural_ilt_package"

with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version


def list_reqs(fname: str = "requirements.txt") -> List[str]:
    with (REQUIREMENTS_DIR / fname).open(encoding="utf-8") as fd:
        return fd.read().splitlines()



def get_long_description() -> str:
    base_dir = ROOT_DIR
    with (base_dir / "README.md").open(encoding="utf-8") as f:
        return f.read()


setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    install_requires=list_reqs(),
    package_data={"neural_ilt_package": ["VERSION"]},
    extras_require={},
    include_package_data=True,
    license="CU-SD LICENSE",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
