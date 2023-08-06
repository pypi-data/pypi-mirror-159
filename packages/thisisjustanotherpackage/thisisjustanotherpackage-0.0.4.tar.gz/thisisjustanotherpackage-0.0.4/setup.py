from setuptools import setup

setup(
    name='thisisjustanotherpackage',
    version='0.0.4',
    description='this is just another package',
    author='thisisjust',
    author_email='this@is.just',
    packages=['package'],
    install_requires=[
        'python >= 3.9',
        'urllib3 == 1.25.11'
    ]
)