from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='vislib',
      version='0.1',
      description='Reusable html-based python visualization library',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/mshafir/vislib',
      author='Michael Shafir',
      author_email='michael.shafir@gmail.com',
      license='MIT',
      packages=['vislib'],
      install_requires=[
            'ipython',
            'Jinja2'
      ],
      classifiers=(
            "Programming Language :: Python",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Framework :: IPython"
      ),
      zip_safe=False)
