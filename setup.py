import setuptools


with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
    
with open("requirements.txt", "r") as fin:
    REQUIRED_PACKAGES = fin.read()

setuptools.setup(
    name="gpsexif",
    version="0.3",
    author="geoyee",
    author_email="geoyee@yeah.net",
    description="Writing / Reading GPS coordinates in photo's EXIF by Python.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/geoyee/GPS-EXIF",
    packages=setuptools.find_packages(),
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)