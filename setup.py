from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

with open("requirements.txt") as req_file:
    all_requirements = list(filter(None, req_file.read().split("\n")))

# Separate GitHub dependencies
install_requires = [req for req in all_requirements if not req.startswith("git+")]
dependency_links = [req for req in all_requirements if req.startswith("git+")]

__version__ = None
with open("utime/version.py") as version_file:
    exec(version_file.read())
if __version__ is None:
    raise ValueError("Did not find __version__ in version.py file.")

setup(
    name='utime',
    version=__version__,
    description='A deep learning framework for automatic PSG sleep analysis.',
    long_description=readme + "\n\n" + history,
    long_description_content_type='text/markdown',
    author='Mathias Perslev',
    author_email='map@di.ku.dk',
    url='https://github.com/kenhding/sleepUT',
    license="LICENSE.txt",
    packages=find_packages(),
    package_dir={'utime': 'utime'},
    include_package_data=True,
    setup_requires=["setuptools_git>=0.3"],
    entry_points={
       'console_scripts': [
           'ut=utime.bin.ut:entry_func',
       ],
    },
    install_requires=install_requires,
    dependency_links=dependency_links,  # Add this to handle Git dependencies
    classifiers=[
        'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License'
    ]
)
