#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

# Run pre-built py.tests as described at
# https://pytest.org/latest/goodpractises.html#integrating-with-distutils-python-setup-py-test
class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess
        import sys
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='bossdata',
    version='0.1.0',
    description="Tools to access SDSS BOSS data.",
    long_description=readme + '\n\n' + history,
    author="David Kirkby",
    author_email='dkirkby@uci.edu',
    url='https://github.com/dkirkby/bossdata',
    packages=[
        'bossdata',
    ],
    package_dir={'bossdata':
                 'bossdata'},
    scripts = [
        # TODO: list installable scripts here, which should start with #!/usr/bin/env python
        # bin/myscript1,
        # bin/myscript2
    ],
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='bossdata',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    cmdclass = {'test': PyTest},
    #test_suite='tests',
    #tests_require=test_requirements
)
