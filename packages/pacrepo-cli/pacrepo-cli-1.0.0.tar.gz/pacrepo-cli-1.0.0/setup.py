from setuptools import setup, find_packages

with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()

setup(
    name='pacrepo-cli',
    version='1.0.0',
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
