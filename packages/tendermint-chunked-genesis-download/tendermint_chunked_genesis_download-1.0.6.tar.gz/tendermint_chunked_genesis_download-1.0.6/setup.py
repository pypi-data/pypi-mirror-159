from setuptools import setup

setup(
    name='tendermint_chunked_genesis_download',
    version='1.0.6',
    description='Package for easily downloading a chunked Tendermint genesis from a RCP enabled node.',
    url='https://github.com/dclaudiud/tendermint-chunked-genesis-download',
    author='dclaudiud',
    author_email='dclaudiud@proton.me',
    packages=['tendermint_chunked_genesis_download'],
    install_requires=[
        'requests==2.26.0',
        'click==7.1.2',
        'setuptools==57.0.0'
    ],
    entry_points={
        'console_scripts': ['download-tendermint-genesis=tendermint_chunked_genesis_download.cli:main']
    },
    license='MIT'
)
