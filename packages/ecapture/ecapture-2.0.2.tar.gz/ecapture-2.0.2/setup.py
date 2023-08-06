import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="ecapture",
    version="2.0.2",
    scripts=['ecapture/ecapture.py'],
    description="Webcams made easy",
    install_requires=["opencv-python"],
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/YFOMNN/ecapture",
    author="Mohammmed Yaseen",
    author_email="hmyaseen05@gmail.com",
    license="GNU GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
    packages=["ecapture"],
    include_package_data=True,
)
