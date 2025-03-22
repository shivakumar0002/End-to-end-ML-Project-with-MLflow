from setuptools import setup, find_packages

setup(
    name='end_to_end_ml_project_with_mlflow',
    version='0.1.0',
    description='End-to-End Machine Learning Project with MLflow Tracking and Deployment',
    author='Shivakumar',
    url='https://github.com/shivakumar0002/End-to-end-ML-Project-with-MLflow',
    packages=find_packages(exclude=['tests*', 'notebooks']),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'mlflow',
        'dvc',
        'fastapi',
        'uvicorn',
        'joblib',
        'python-dotenv'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'train-model=scripts.train_model:main',
            'evaluate-model=scripts.evaluate_model:main'
        ]
    },
    include_package_data=True,
    zip_safe=False
)