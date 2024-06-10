from setuptools import find_packages, setup

DISTNAME = "PyTeLo"

DESCRIPTION = "A Flexible and Efficient Temporal Logic Tool for Python"

INSTALL_REQUIRES = ["antlr4-python3-runtime==4.7.1",
                    "scipy",
                    "gurobipy"]

setup(
    name=DISTNAME,
    author="ERL Lehigh",
    description=DESCRIPTION,
    url="https://github.com/erl-lehigh/PyTeLo",
    python_requires=">=3.7, <3.11",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    # extras_require=EXTRAS_REQUIRES,
)

# to install:
# pip install .
