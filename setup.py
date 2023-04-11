from setuptools import setup, find_packages

setup(
    name='mangacollect_test',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    url='https://github.com/shooter-dev/mangacollect_test.git',
    license='',
    author='shooter',
    author_email='shooter.dev@gmail.com',
    description='A Python package for interacting with the MangaCollect API'
)