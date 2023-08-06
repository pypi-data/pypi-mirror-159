from setuptools import setup, find_packages

setup(
    name='sequence_annotation',
    version='0.0.6',
    url='https://github.com/BioinformaticaUNQ/sequence_annotation.git',
    author='BioInformatico UNQ',
    author_email='author@gmail.com',
    description='Proteins info mapper',
    packages=find_packages(),   
    entry_points ={
            'console_scripts': [
                'sequence_annotation = sequence_annotation:main'
            ]
        }, 
    install_requires=['requests >= 2.13.0'],
)