#
# pip setup
# Thanks to: https://dev.classmethod.jp/articles/pip-install-via-github-command/
#

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colab_cameracapture",
    version="0.1.0",
    author="uranishi",
    author_email="uranishi@gmail.com",
    description="Colab camera capture module with pip installation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/uranishi/colab_cameracapture",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)