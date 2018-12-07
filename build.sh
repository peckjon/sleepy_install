#!/usr/bin/env bash
rm dist/*
python3 setup.py sdist bdist_wheel
#only upload the tar.hz, not the .whl, or the installation delay gets eliminated
twine upload dist/*.gz
