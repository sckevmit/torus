import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [req.strip() for req in open('requirements.pip')]
if sys.version_info[:2] <= (2, 6):
    requirements = [req.strip() for req in open('requirements_py26.pip')]

exec([v for v in open('torus/__init__.py') if '__version__' in v][0])

setup(
    name='torus',
    version=__version__,
    author='Aaron Westendorf',
    author_email="aaron@agoragames.com",
    packages = ['torus'],
    install_requires = requirements,
    url='https://github.com/agoragames/torus',
    license="LICENSE.txt",
    description='Carbon and Graphite replacement using Kairos for timeseries storage',
    long_description=open('README.rst').read(),
    keywords=['python', 'redis', 'time series', 'statistics'],
    scripts=['bin/karbon', 'bin/torus'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Topic :: Communications",
        "Topic :: System :: Distributed Computing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ]
)
