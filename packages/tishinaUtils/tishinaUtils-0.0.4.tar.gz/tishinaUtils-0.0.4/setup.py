from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    name='tishinaUtils',
    version='0.0.4',
    packages=find_packages(where="src"),
    url='https://pypi.org/project/tishinaUtils/',
    license='MIT',
    author='tishinaDev',
    author_email='TopLadAce@outlook.com',
    description='For reusable snippets of code',
    long_description=readme,
    long_description_content_type="text/markdown",
    install_requires=["setuptools~=63.2.0"],
    python_requires=">=3.10.*",
    # install_requires=[], # comment it out if you do not require external libraries
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10"
    ]
)
