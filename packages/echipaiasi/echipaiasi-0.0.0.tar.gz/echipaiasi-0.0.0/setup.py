from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python'
]


setup(
    name='echipaiasi',
    versions='0.0.1',
    description='echipaiasi package',
    Long_description=open('README.txt').read() + '\n\n' + open ('CHANGELOG.txt').read(),
    url='',
    author='bro designs',
    author_email='alexandru_ifrim92@yahoo.com',
    License='MIT',
    classifiers=classifiers,
    keywords='iasi',
    packages=find_packages(),
    install_requires=['']
)