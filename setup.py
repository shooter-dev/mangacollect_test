from setuptools import setup, find_packages

setup(
    name='mangacollect_test',
    version='0.1',
    packages=find_packages(),
    description='connexion à l\'api de mangacollect',
    url='https://github.com/shooter-dev/mangacollect_test',
    author='shooterdev',
    author_email='vincentbleach@gmail.com',
    license='MIT',
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
