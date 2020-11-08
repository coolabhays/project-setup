from setuptools import find_packages, setup
from os import path

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

setup(
    name='setproj',
    version='0.0.3',
    packages=find_packages('src'),
    description='create projects in cli',
    author='Abhay Shanker Pathak',
    author_email='abhaysp9955@gmail.com',
    keywords="project programming language",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",  # set if not reStructuredText
    url="https://github.com/coolabhays/project-setup",
    license="MIT",
    package_dir={'': 'src'},
    py_modules=["setupProject"],
    install_requires=[
        'Click',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Topic :: Terminals",
        "Operating System :: POSIX"
    ],
    entry_points={
        'console_scripts': [
            'setproj=src.setupProject:main',
        ],
    },
)
