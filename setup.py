import time
import setuptools

t = 3

setuptools.setup(
    name="sleepy_install",
    version="0.%d.1" % t,
    author="Jon Peck",
    author_email="peckjon@gmail.com",
    description="Waits for [minor version number] minutes during package install. No other features; use for testing time-dependent automation.",
    long_description="Wait for several minutes during package installation. No other features; use for testing time-dependent automation. Minor version indicates wait time (e.g. for a 2 minute delay, use 0.2.*)",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

print("Begin %d minute wait..." % t)
time.sleep(t*60)
print("End wait.")
