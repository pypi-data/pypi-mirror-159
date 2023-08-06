from setuptools import setup, find_packages

# name: Name of the package to be uploaded in PyPi
# version: Version of the current package.
# packages: Packages that will be used to create the package.
# include_package_data: To include the package data
# install_requires: External dependencies.
# entry_points: Entry point for the package.
# A egg folder is created when we install this package locally.
# To install the local package, run "pip install --editable ."

setup(
    name="password-breach-CLI",
    version='1.0',
    author='Sanjeev Bhusal',
    author_email='bhusalsanjeev23@gmail.com',
    description='Check if a password has been breached in all registered data leaks',
    long_description="It is a command line application which accepts a password as a parameter and checks how many "
                     "times the password was present in a data breach",
    long_description_content_type="text/markdown",
    packages = find_packages(),
    install_requires=['click'],
    keywords=['python', 'click', 'password-breach', 'pwnedpasswords'],

    entry_points={
        'console_scripts': [
            'breach = check_breach_password.cli.cli:cli'
        ]
    }
)
