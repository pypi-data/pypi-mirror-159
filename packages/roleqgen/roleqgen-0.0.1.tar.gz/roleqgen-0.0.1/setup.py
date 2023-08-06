import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="roleqgen",
    version = "0.0.1",
    author="Valentina Py",
    url="https://github.com/rubenwol/RoleQGeneration",
    packages=setuptools.find_packages(),
    install_requires=[
        'spacy',
        'unidecode',
        'jsonlines',
        'pytorch_lightning',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
