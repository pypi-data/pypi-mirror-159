import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='python-aioweb',  
    version='0.0.1',
    author='Davy Wybiral',
    author_email="davy.wybiral@gmail.com",
    description='A barebones asyncio http library.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wybiral",
    packages=['aioweb'],
    install_requires=[],
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
