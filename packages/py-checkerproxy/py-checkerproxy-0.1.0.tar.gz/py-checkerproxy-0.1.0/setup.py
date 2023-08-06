import setuptools

setuptools.setup(
    name="py-checkerproxy",
    version="0.1.0",
    author="Yassine Amjad",
    author_email="Yassine.amjad001@gmail.com",
    description="A simple checkerproxy library",
    packages=["checkerproxy"],
    install_requires=["requests", "contextlib"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    )