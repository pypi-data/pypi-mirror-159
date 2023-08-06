"""Setup for pip package."""

from setuptools import find_namespace_packages
from setuptools import setup


def _get_version():
  with open('vizier/__init__.py') as fp:
    for line in fp:
      if line.startswith('__version__'):
        g = {}
        exec(line, g)  # pylint: disable=exec-used
        return g['__version__']
    raise ValueError('`__version__` not defined in `vizier/__init__.py`')


def _parse_requirements(requirements_txt_path):
  with open(requirements_txt_path) as fp:
    return fp.read().splitlines()


_VERSION = _get_version()

setup(
    name='google-vizier',
    version=_VERSION,
    url='https://github.com/google/vizier',
    license='Apache License 2.0',
    author='Vizier Team',
    description='Vizier: Distributed service framework for blackbox optimization and research.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author_email='oss-vizier-dev@google.com',
    # Contained modules and scripts.
    packages=find_namespace_packages(
        include=['vizier*'], exclude=['*_test.py', 'examples']),
    install_requires=_parse_requirements('requirements.txt'),
    extras_require={
        'jax': _parse_requirements('requirements-jax.txt'),
        'tf': _parse_requirements('requirements-tf.txt'),
        'misc': _parse_requirements('requirements-misc.txt')
    },
    # tests_require=_parse_requirements('requirements-test.txt'),
    requires_python='>=3.9',
    include_package_data=True,
    zip_safe=False,
    # PyPI package information.
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='ai machine learning hyperparameter blackbox optimization framework',
)
