from setuptools import setup, find_packages

setup(
    name="attendance_exam_performance",
    version="0.1",
    description="A project to study the correlation between student attendance and their performance in competitive exams.",
    author="Minal Madankar Devikar",
    author_email="meenal.madankar@gmail.com", 
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.23.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.2",
        "scipy>=1.7.0",
        "scikit-learn>=1.1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
