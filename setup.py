from setuptools import setup

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="eiopaPy",
    version="0.0.1",
    description="This package provides data produced by EIOPA. Please note that the author of this package is not affiliated with EIOPA.",
    author="Mehdi Yacoubi",
    author_email="mehdiyacoubi95@gmail.com",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
    ],
    url="https://github.com/MYACOUBI/eiopaPy",
    license="MIT",
    packages=["eiopaPy"],
    install_requires=[]

)