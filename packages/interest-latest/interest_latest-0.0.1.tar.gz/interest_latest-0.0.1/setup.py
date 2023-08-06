
import setuptools
setuptools.setup(
    name='interest_latest',
    version='0.0.1',
    description='Interest Calculator can use for calculate interest in the from of days,monthly and yearly ',
    author= 'Akshay Thakare',
    url = 'https://github.com/Akshay311/Simple-Interest-Calculator',
    packages=setuptools.find_packages(),
    keywords=['interest', 'calculator', 'loan calculator'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=['interest_latest'],
    package_dir={'':'src'},
    install_requires = []
)