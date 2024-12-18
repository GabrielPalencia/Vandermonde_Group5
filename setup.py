from setuptools import setup, find_packages

setup(
    name="vandermonde_lib",              # Nombre del paquete
    version="1.0.0",                     # Versión inicial
    author="Gabriel Palencia",  
    author_email="gepalencia@uninorte.edu.p",
    description="Librería para generar matrices de Vandermonde e interpolación polinómica. Fin académico.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GabrielPalencia/Vandermonde_Group5.git",  # Reemplaza con tu URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
