from setuptools import setup

setup(
    # name of package
    name='datadb3',

    version='0.0.1',
    description='tool to assess data',

    py_modules = ['datadb3', 'minidb'],


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
