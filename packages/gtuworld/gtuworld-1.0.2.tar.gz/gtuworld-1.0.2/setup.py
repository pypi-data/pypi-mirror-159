from distutils.core import setup
import setuptools

def readme():
    with open(r'README.md') as f:
        README = f.read()
    return README

setup(
    name = 'gtuworld',
    packages = setuptools.find_packages(),

    version = '1.0.2',
    license='MIT',
    description = 'Download GTU papers within seconds.',
    author = 'Dhiraj Beri',
    author_email = 'dhirajberi.official@gmail.com',
    url = 'https://github.com/dhirajberi/gtuworld',
    download_url = 'https://github.com/dhirajberi/gtuworld/archive/refs/tags/v1.0.2.tar.gz',
    keywords = ['gtu paper download', 'gtuworld', 'gtu paper download using python'],
    install_requires=[],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Education',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    ],
)
