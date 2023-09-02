import os
from importlib.machinery import SourceFileLoader

from setuptools import find_packages, setup

module_name = "sortphoto"
module = SourceFileLoader(
    module_name, os.path.join(module_name, "__init__.py")
).load_module()


def load_requirements(fname):
    with open(fname) as f:
        line_iter = (line.strip() for line in f.readlines())
        return [
            line
            for line in line_iter
            if line and (not line.startswith("#"))
        ]


setup(
    name=module_name.replace("_", "-"),
    version=module.__version__,
    author=module.__author__,
    license=module.__license__,
    description=module.package_info,
    platforms="all",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=load_requirements("requirements.txt"),
    extras_require={"develop": load_requirements("requirements.dev.txt")},
    entry_points={
        "console_scripts": [
            "{0} = {0}.main:main".format(module_name),
        ]
    },
)
