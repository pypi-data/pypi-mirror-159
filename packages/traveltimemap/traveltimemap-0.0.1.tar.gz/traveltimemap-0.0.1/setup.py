import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="traveltimemap",
    version="0.0.1",
    author="Huong Nguyen",
    author_email="huongmng@usc.edu",
    description="Travel Time Map",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nguyen-huong/traveltime/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)