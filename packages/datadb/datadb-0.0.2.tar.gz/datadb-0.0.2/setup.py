from setuptools import setup

setup(
    # name of package
    name='datadb',

    version='0.0.2',
    description='tool to assess data',

    # which folders will be uploaded
    packages=["datadb"],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ],

    install_requires=[
        "pandas",
        "bokeh",
        "notebook",
        "scikit-learn"
    ],

    license='MIT',

    author='Rens Jochemsen',
    author_email='rensjochemsen@gmail.com'
)
