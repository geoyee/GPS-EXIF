import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gpsexif",
    version="0.1",
    author="geoyee",
    author_email="geoyee@yeah.net",
    description="Writing / Reading GPS coordinates in photo's EXIF by Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geoyee/GPS-EXIF",
    packages=setuptools.find_packages(),
    install_requires=["piexif"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)