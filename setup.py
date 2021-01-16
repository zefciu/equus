from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='equus',
    version='0.0.1',
    author="Szymon Pyżalski",
    author_email="szymon@pythonista.net",
    description="A versatile configuration tool",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    entry_points={
        'equus.loader': [
            'cp = equus.loaders.cp:config_parser_loader',
            'environ = equus.loaders.environ:environ_loader',
        ]
    }
)