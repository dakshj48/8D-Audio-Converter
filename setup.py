from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = [req.strip('\n') for req in f.readlines()]

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="eightd_audioconv",
    version="0.1",
    packages=find_packages(),
    author="Daksh Jain, Sharath Ramkumar",
    description="A package to convert audio files (in mp3 format) to 8D audio files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dakshj48/8D-Audio-Converter",
    install_requires=requirements,
    scripts=['bin/8d-audio-converter']
)
