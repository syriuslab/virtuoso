from setuptools import setup, find_packages

setup(
    name='virtuoso',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas>=1.2.4',
        'numpy>=1.20.3',
        'scikit-learn>=0.24.2',
        'xgboost>=1.4.2',
        'lightgbm>=3.2.1',
        'catboost>=0.26.1',
        'tensorflow>=2.5.0',
        'pyyaml>=5.4.1',
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='VIRTUOSO: Advanced Multilayer Architecture for Cloud Security',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/virtuoso',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
