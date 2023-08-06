import setuptools

with open("README.md", "r") as fh:
    description = fh.read()

setuptools.setup(
    name="resilipy",
    version="0.0.9",
    author="Vincent Dietrich",
    author_email="vdietric@students.uni-mainz.de",
    packages=setuptools.find_packages(),
    description="ResiliPy - A machine-learning based Mouse labelling GUI.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/dietvin/resilipy",
    license='MIT',
    python_requires='>=3.8',
    install_requires=[
        "PyQt6",
        "xgboost",
        "scikit-learn",
        "numpy",
        "pandas",
        "Levenshtein",
        "pyqtgraph"
    ],
    package_data={
        "resilipy": ["resilipy/models/XGBoost C57 mice.model"]
    },
    data_files=[
        ("ui", ["resilipy/ui/builder.ui", "resilipy/ui/labeler.ui", "resilipy/ui/preprocessor.ui", "resilipy/ui/resilipy.ui", "resilipy/ui/stylesheet.txt"]),
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
    ]
)