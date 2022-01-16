from setuptools import setup

setup(
    name='merge_all_csv_in_directory',
    version='0.0.2',
    description='A python package to merge all csv files data in a directory into one file and output that file',
    py_modules=["merge_all_csv_in_directory"],
    package_dir={'':'src'},
    home="https://github.com/Muhammad-Bilal-7896/read_all_csv_files_and_merge_into_one",
    author="https://github.com/Muhammad-Bilal-7896",
    author_email="bilalmohib7896@gmail.com",
    platforms="Windows,Ubunto,Linux",
    install_requires=[
        "numpy",
        "pandas"
    ]
)