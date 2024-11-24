from setuptools import setup, find_packages

setup(
    name="vandermonde_lib",
    version="1.0",
    author="Gabriel Palencia",
    author_email="gepalencia@uninorte.edu.p",
    description="Librería para generar matrices de Vandermonde e interpolación polinómica. Fin académico.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GabrielPalencia/Vandermonde_Group5.git",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
