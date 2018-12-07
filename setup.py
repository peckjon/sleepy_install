import time
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sleepy_install",
    version="0.0.1",
    author="Jon Peck",
    author_email="peckjon@gmail.com",
    description="Waits for 60 seconds during package install. No other features; use for testing time-dependent automation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: WTFPL",
        "Operating System :: OS Independent",
    ],
)

import time
# wait for 1 minute
t = 60
print("Begin %d second wait..." % t)
time.sleep(t)
print("End wait.")