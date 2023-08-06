import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="kiwicalc",
    version="0.21.1",
    description="Extremely simple interface for mathematics.",
    long_description=README,
    long_description_content_type="text/markdown",
    url='https://www.kiwicalc.com',
    author="Jonathan",
    author_email="kiwicalc@gmail.com",
    package_dir={'': 'src'},
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    install_requires=['numpy ~= 1.21.0', 'matplotlib ~= 3.5.2', 'reportlab ~= 3.6.9', 'googletrans ~= 3.0.0',
                      'anytree ~= 2.8.0', 'defusedxml ~= 0.7.1'],
    keywords='Math Algebra Calculus Matrix Probability Vector Plot Worksheet PDF'
)
