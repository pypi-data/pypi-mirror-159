import setuptools
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setuptools.setup(
    name='tree-print',
    version='0.0.0',
    author='Max Curzi',
    author_email='massimiliano.curzi@gmail.com',
    description='A CLI utility to print directory structure.',
    license='MIT',
    packages=["pytree"],
    zip_safe=False,
    python_requires='>=3.5',
    long_description=long_description,
    long_description_content_type='text/markdown',
)