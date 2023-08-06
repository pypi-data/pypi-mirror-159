from setuptools import setup, find_packages


setup(
    name='ProxyFinder',
    version='2022.06.16.1',
    packages=find_packages(),
    url='https://github.com/ulbwazhine/ProxyFinder',
    license='MIT',
    author='Ulbwazhine',
    author_email='ulbwa@icloud.com',
    description='',
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    long_description=open('readme.md', 'r').read(),
    long_description_content_type='text/markdown',
    include_package_data=True
)
