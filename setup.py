from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='cgrss',
    version='0.1',
    description='RSS feed generator for Comings and Goings',
    long_description=readme(),

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='davis enterprise rss',

    url='https://github.com/ixjlyons/cgrss',
    author='Kenneth Lyons',
    author_email='ixjlyons@gmail.com',
    license='MIT',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'cgrss=cgrss.cgrss:main',
        ],
    },

    install_requires=[
        'requests',
        'beautifulsoup4',
        'feedgen'
    ],

    extras_require={}
)
