from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.6',
  'Programming Language :: Python :: 3.7'
]

# Delete all files in the dist folder.

# Update the version number in the setup.py file.

# Re-create the wheels:

# python3 setup.py sdist bdist_wheel
# Re-upload the new files:

# twine upload dist/*
 
setup(
  name='arrotechtools',
  version='0.0.9',
  description='Library with most of the useful methods in the world of programming',
  long_description=long_description,
  long_description_content_type="text/markdown",
  url='',  
  author='Harun Gachanja',
  author_email='arrotechdesign@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='roles', 
  packages=find_packages(),
  install_requires=['flask-jwt-extended'] 
)