from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='ArithmeticOptimizer',
    version='0.0.1',
    description='An optimizer tool for ML preprocessing',
    #long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Winslow Conneen',
    author_email='wconneen@patriots.uttyler.edu',
    license='MIT',
    classifiers=classifiers,
    keywords=['Machine Learning', 'Preprocessing', 'Prediction', 'Classification'],
    packages=find_packages(),
    install_requires=['numpy', 'statsmodels']
)