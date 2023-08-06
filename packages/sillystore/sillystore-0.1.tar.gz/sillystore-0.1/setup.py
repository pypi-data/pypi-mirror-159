from setuptools import setup, find_packages


setup(
    name='sillystore',
    version='0.1',
    license='MIT',
    author="Chris DD",
    author_email='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    keywords='example project',
)