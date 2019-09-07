import ast
import io
import re

from setuptools import setup, find_packages

with io.open('README.md', 'rt', encoding="utf8") as f:
    readme = f.read()

_description_re = re.compile(r'description\s+=\s+(?P<description>.*)')

with open('lektor_social_publisher.py', 'rb') as f:
    description = str(ast.literal_eval(_description_re.search(
        f.read().decode('utf-8')).group(1)))

setup(
    author='Aaron Arstman',
    author_email='rootisalone@outlook.com',
    description=description,
    keywords='Lektor plugin',
    license='MIT',
    long_description=readme,
    long_description_content_type='text/markdown',
    name='lektor-social-publisher',
    packages=find_packages(),
    platforms='any',
    py_modules=['lektor_social_publisher'],
    url='https://github.com/Arstman/lektor-social-publisher.git',
    version='0.1',
    install_requires=[
        'Lektor',
        'inifile'
    ],
    classifiers=[
        'Framework :: Lektor',
        'Environment :: Plugins',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'lektor.plugins': [
            'social-publisher = lektor_social_publisher:SocialPublisherPlugin',
        ]
    }
)
