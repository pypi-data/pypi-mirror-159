from setuptools import setup, find_packages

requirements : list = ["pycryptodome" , "pillow"]

setup(
    name = "shython",
    version = "1.0",
    author = "Shayan Heidari",
    author_email = "snipe4kill.tg@gmail.com",
    description = "This is a library or tool for working with files, urls, encryption and decryption, etc.!",
    long_description = "Loading...",
    long_description_content_type = "text/markdown",
    url = "https://github.com/snipe4kill/shython/",
    packages = find_packages(),
    install_requires = requirements,
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ],
)