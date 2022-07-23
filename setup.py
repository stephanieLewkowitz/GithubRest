import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="githubrest", 
    version="0.0.1",
    #package_dir={'': 'src'},  
    author="stephanie",
    author_email="author@example.com",
    description="rest gitub wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(), #where='src'),
    #packages=["src"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
