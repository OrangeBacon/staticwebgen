import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name = "staticwebgen",
    version = "0.0.3",
    author = "OrangeBacon",
    author_email = "computer.backup.15@gmail.com",
    description = "A custom static site generator",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/OrangeBacon/staticwebgen",
    license = "MIT",

    packages = ["staticwebgen"],
    entry_points = {
        'console_scripts': ["staticwebgen = staticwebgen.command_line:main"]
    },

    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Internet"
    ]
)