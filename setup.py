from distutils.core import setup

setup(
    name='SEHW1',
    version='0.1dev',
    packages=['code',],
    license='MIT',
    long_description=open('README.txt').read(),
    install_requires=[
        'pytest'
    ]
)