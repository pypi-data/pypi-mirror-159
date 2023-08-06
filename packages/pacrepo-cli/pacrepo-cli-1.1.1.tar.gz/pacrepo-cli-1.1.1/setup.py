from setuptools import setup, find_packages
import os, subprocess

with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()

if os.path.isdir(".git"):
    ver=subprocess.check_output("git describe --tags --abbrev=0 | sed 's/^v//;'",shell=True).decode('utf-8').replace('\n','')
    with open("version","w",encoding="utf-8") as fh:
        fh.write(ver)
elif os.path.isfile("version"):
    with open("version","r",encoding="utf-8") as fh:
        ver=fh.read().replace('\n','')
else:
    ver="0.0.0"

setup(
    name='pacrepo-cli',
    version=ver,
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
