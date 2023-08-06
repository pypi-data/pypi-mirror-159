from setuptools import setup

setup(
    name='PyTgSend',
    version='1.2',
    author='Alex Tamilin',
    author_email='popovalex402@gmail.com',
    license='MIT',

    description='Lightweight function to send telegram messages',
    keywords='telegram tg',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    url='https://github.com/aptac01/PyTgSend.git',

    packages=['PyTgSend'],
    install_requires=[
        'requests',
    ],

    zip_safe=True
)
