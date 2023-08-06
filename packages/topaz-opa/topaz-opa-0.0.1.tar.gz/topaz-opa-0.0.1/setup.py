from setuptools import setup, find_packages

setup(
    name='topaz-opa',
    version='0.0.1',
    author='Oleksii Demennikov',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    keywords='opa rego packagemanager',
    install_requires = [
        'gitpython'
    ],
)
