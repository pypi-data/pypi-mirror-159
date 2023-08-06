import setuptools

# pylint: disable=all
"""
python -m pip install --upgrade setuptools wheel twine
python setup.py sdist bdist_wheel
python -m twine upload dist/*
"""
setuptools.setup(
    name="pytorch-sdk",
    version="0.0.1",
    author="Anton Gorinenko",
    author_email="anton.gorinenko@gmail.com",
    description="",
    long_description="",
    keywords='python, pytorch, torch, machine, learning',
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics"
    ],
    install_requires=[
        "torch",
        "torchvision",
        "torchaudio",
    ],
    extras_require={
        'test': [
            'pytest',
            'pylint',
        ]
    },
    python_requires='>=3.7',
)
