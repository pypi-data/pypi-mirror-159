from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "Pypi.md").read_text()

setup(
    name='Py-SPW',
    version='1.0',
    packages=['pyspw'],
    url='https://github.com/teleport2/Py-SPW',
    license='MIT License',
    author='Stepan Khozhempo',
    author_email='stepan@m.khoz.ru',
    description='Python library for spworlds API',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
