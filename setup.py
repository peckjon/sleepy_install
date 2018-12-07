import time
import setuptools

t = 60*5

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sleepy_install",
    version="0.0.2",
    author="Jon Peck",
    author_email="peckjon@gmail.com",
    description="Waits for %d seconds during package install. No other features; use for testing time-dependent automation." % t,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

print("Begin %d second wait..." % t)
time.sleep(t)
print("End wait.")
