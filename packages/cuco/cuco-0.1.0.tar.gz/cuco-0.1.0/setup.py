from setuptools import setup

setup(
    name='cuco',
    version='0.1.0',
    description='Project for making it easier to write configuration files which may be automatically converted into a set of alternative system setups',
    url='https://github.com/zeionara/cuco',
    author='Zeio Nara',
    author_email='zeionara@gmail.com',
    packages=[
        'cuco',
        'cuco.utils'
    ],
    install_requires=[
        'yaml',
        'ruamel.yaml'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.9',
    ]
)
