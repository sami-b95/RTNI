from setuptools import setup, find_packages

setup(
    name="rtni",
    description="Random Tensor Network Integrator",
    author="Motohisa Fukuda and Robert Koenig and Ion Nechita",
    version="1.0",
    packages=["RTNI"],
    install_requires=["matplotlib", "networkx", "numpy", "sympy"]
)