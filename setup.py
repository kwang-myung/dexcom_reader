#!/usr/bin/python
from setuptools import find_packages, setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="dexcom_reader",
    version="0.2.0",  # http://semver.org/
    description="Audit, and inspect data from Dexcom G4, G5, and G6 receivers.",
    long_description=readme(),
    author="Will Nowak",
    # I'm just maintaining the package, @compbrain authored it.
    author_email="compbrain+dexcom_reader@gmail.com",
    maintainer="Ben West",
    maintainer_email="bewest+dexcom_reader@gmail.com",
    url="https://github.com/openaps/dexcom_reader",
    packages=find_packages(),
    install_requires=["pyserial"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development :: Libraries",
    ],
    package_data={"dexcom_reader": ["etc/udev/rules.d/*"]},
    data_files=[
        # installing to system locations breaks things for virtualenv based
        # environments.
        # ('/etc/udev/rules.d', ['dexcom_reader/etc/udev/rules.d/80-dexcom.rules'] ),
    ],
    zip_safe=False,
    include_package_data=True,
)

#####
# EOF
