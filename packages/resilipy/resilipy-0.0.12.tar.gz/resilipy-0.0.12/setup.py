import setuptools

with open("README.md", "r") as fh:
    description = fh.read()
    setuptools.setup(
        name="resilipy",
        version="0.0.12",
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
            # "datetime",
            # "pickle",
            # "os",
        ],
        package_data={
            "resilipy": ["models/XGBoost C57 mice.model", "ui/builder.ui", "ui/labeler.ui", "ui/preprocessor.ui", "ui/resilipy.ui", "ui/stylesheet.txt"]
        },
        # data_files=[
        #     ("ui", ["./resilipy/ui/builder.ui", "./ui/labeler.ui", "./ui/preprocessor.ui", "./ui/resilipy.ui", "./ui/stylesheet.txt"]),
        # ],
        classifiers=[
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Topic :: Scientific/Engineering :: Bio-Informatics"
        ]
    )

