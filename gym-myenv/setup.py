from setuptools import setup

setup(name='gym_myenv',
    version = '0.1',
    install_requires=['gym'],
    packages=setuptools.find_packages(),
    python_requires='>=3.5',
)