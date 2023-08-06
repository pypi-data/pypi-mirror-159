"""Installation script for sixrunr application."""
from pathlib import Path
from setuptools import setup, find_packages
from sixbox.cli import __version__

DESCRIPTION = (
    "python library for sixoclock's softwares to run"
)
APP_ROOT = Path(__file__).parent
# README = (APP_ROOT / "README.md").read_text(encoding='utf-8')
AUTHOR = "sixoclock"
AUTHOR_EMAIL = "r_d@sixoclock.net"
PROJECT_URLS = {
    "Documentation": "https://docs.sixoclock.net/clients/sixbox-linux.html",
    "Bug Tracker": "https://github.com/6-oclock/Bug-Tracker/issues",
    "Source Code": "https://github.com/6-oclock/sixbox-linux",
}

VERSION = __version__

INSTALL_REQUIRES = [
    "pyyaml",
    "paramiko",
    "python-daemon",
    "prettytable",
    "colorlog",
    "tqdm"

]
EXTRAS_REQUIRE = {
    ':sys_platform == "win32"': ['cwltool==3.0.20210124104916', 'schema-salad==7.0.20210124093443'],
    ':"linux" in sys_platform': [ "cwltool", "rdflib-jsonld"],
    "dev": [
        "pre-commit",
        "pydocstyle",
        "pytest",
        "tox",
    ]
}

setup(
    name="sixbox",
    description=DESCRIPTION,
    # long_description=README,
    long_description_content_type="text/markdown",
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=AUTHOR,  
    maintainer_email=AUTHOR_EMAIL,
    license="Apache-2.0 License",
    url="https://docs.sixoclock.net/clients/sixbox-linux.html",
    project_urls=PROJECT_URLS,
    packages=find_packages(),
    # package_dir={"": "sixbox"},
    python_requires=">=3.6",
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    entry_points={
          'console_scripts': [ "sixbox=sixbox.cli._main:main" ]
      },
)
