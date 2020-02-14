import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sequence-", # Replace with your own username
    version="0.0.1",
    author="Andreas B.",
    author_email="andreas@*****************",
    description="Implementation of the provided InterviewTask.pdf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aquaandi/sequence",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='==3.8.1',
)
