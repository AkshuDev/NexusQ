from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nexusQ",
    version="0.1.0",
    author="Pheonix Studios | AkshuDev",
    author_email="akshobhyasasun@gmail.com",
    description="A Python framework for hybrid quantum-classical application development.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AkshuDev/NexusQ",  # Replace with your GitHub repo URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Adjust as needed
    install_requires=[
        # Add your dependencies here (see requirements.txt)
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0"
        ],
    },
)