from setuptools import find_packages, setup

setup(
    name='ez-toolkits',
    version='1.20.6',
    author='septvean',
    author_email='septvean@gmail.com',
    description='Easy toolkits',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    python_requires='>=3.10'
)
