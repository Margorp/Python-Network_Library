import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="Network_Library",
    version="1.0.0",
    author="Margorp",
    author_email="margorp2012@gmail.com",
    description="Network_Library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
    
