from setuptools import setup

long_description = (
    open('README.txt').read()
    + '\n' +
    open('LICENSE').read()
    + '\n')

setup(
    name="pyoperacionesmonzon",
    version="0.2",
    description="A tool to perform mathematical operations.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="pyoperacionesmonzon math operations",
    author="Jose Manuel Monzón",
    author_email="jmmonzonn@gmail.com",
    license="GNU GPLv3",
    packages=["pyoperacionesmonzon"]
)