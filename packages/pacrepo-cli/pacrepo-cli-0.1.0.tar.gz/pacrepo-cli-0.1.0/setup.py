from setuptools import setup, find_packages

__version__ = "0.1.0"

with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()

setup(
    name='pacrepo-cli',
    version=__version__,
    author='James C Kimble',
    author_email='me@jckimble.com',
    license='ISC',
    description='Quick Tool for managing user repos in pacman.conf',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/jckimble/pacrepo-cli',
    py_modules=['cli'],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    keywords='archlinux unofficial pacman pacman.conf user repo repository',
    install_requires=['click'],
    entry_points={
        'console_scripts': [
            'pacrepo-cli = cli:main',
        ],
    },
)
