from setuptools import setup

setup(
    name='web-scraper',
    version="0.0.4",
    author="Tomasz Dobrzycki",
    author_email="dobrzycki.tomasz@gmail.com",
    license='BSD',
    description="Sainsbury's website scraper. Console application that will find all products and create a summary.",
    long_description=open('README.md').read(),
    url='https://github.com/tomashenco/web-scraper',
    install_requires=['requests>=2.8.1',
                      'lxml>=3.4.4'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Web Environment",
        "License :: OSI Approved :: BSD License"
    ]
)
