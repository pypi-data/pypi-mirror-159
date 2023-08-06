from setuptools import setup, find_packages

setup(
    name='firebaseaio',
    version='0.1.0',
    license='MIT',
    author="09ghostrider",
    description="A simple async python wrapper for the [Firebase API](https://firebase.google.com).",
    packages=find_packages(),
    url='https://github.com/09ghostrider/firebase-aio',
    keywords='firebaseaio, firebase-aio',
    install_requires=[
        "setuptools>=61.0",
        "oauth2client>=3.0.0",
        "aiohttp>=3.7.4",
    ],
    project_urls={
        "Homepage": "https://github.com/09ghostrider/firebase-aio",
        "Bug Tracker": "https://github.com/09ghostrider/firebase-aio/issues",
    },
)