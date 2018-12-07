python3 setup.py sdist bdist_wheel
#only upload the tar.hz, not the .whl
twine upload dist/sleepy_install-0.0.1.tar.gz