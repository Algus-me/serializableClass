from setuptools import setup, find_packages
from os.path import join, dirname

import serializableClass

setup(
    name='serializableClass',
    description='This project makes saving/loading procedure easier for classes with inheritance.',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    version=serializableClass.__version__,
    url='https://github.com/Valtonis/serializableClass.git',
    author='Alexander Gusarin',
    author_email='alex.gusarin@gmail.com',
    license='MIT',
    packages=find_packages()
)