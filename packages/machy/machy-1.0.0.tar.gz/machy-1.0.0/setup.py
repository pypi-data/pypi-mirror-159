from setuptools import find_packages, setup


setup(
    name='machy',
    packages=find_packages(include=['machy']),
    version='1.0.0',
    description='Web scraper utils',
    url='https://github.com/Ennoriel/machy',
    author='Maxime Dupont',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)