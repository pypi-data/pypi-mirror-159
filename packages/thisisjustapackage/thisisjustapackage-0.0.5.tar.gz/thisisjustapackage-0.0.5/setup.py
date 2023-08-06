from setuptools import setup

setup(
    name='thisisjustapackage',
    version='0.0.5',
    description='this is just a package',
    author='thisisjust',
    author_email='this@is.just',
    packages=['package'],
    install_requires=[
        'python >= 3.9',
        'urllib3 == 1.26.9'
    ]
)