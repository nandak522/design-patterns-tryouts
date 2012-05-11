from setuptools import setup, find_packages

setup(
    name='design-patterns-tryouts',
    version='1.0.0',
    long_description=open('README.md', 'r').read(),
    author='NandaKishore',
    author_email='madhav.bnk@gmail.com',
    packages=find_packages(exclude=["tests"]),
    install_requires=['lxml',
                      'zope.interface',
                      'zope.component',
                      ],
    )
