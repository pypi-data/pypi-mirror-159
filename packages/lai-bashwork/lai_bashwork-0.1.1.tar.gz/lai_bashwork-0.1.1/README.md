A LightingWork that uses subprocess.Popen()

- uses shell=True to allow arbitrary commands to be run
- Drive is use to pull and push data before and after the run
- flag to just pull and push data if a background process is running

# Update PyPi

## Test
python -m pip install twine
python -m pip install setuptools wheel
python setup.py sdist bdist_wheel



python -m twine upload - repository testpypi dist/*
python -m pip install -i https://test.pypi.org/quicksample/ lai-bashwork

## Prod
python -m twine upload dist/*