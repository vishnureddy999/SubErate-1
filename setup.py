from setuptools import setup, find_packages

setup(
    version="1.0",
    name="SubErate",
    packages=find_packages(),
    py_modules=["SubErate"],
    author="Polapragada Yashwant",
    install_requires=[
        'openai-whisper',
    ],
    description="Automatically generate and embed subtitles into your videos",
    entry_points={
        'console_scripts': ['SubErate=SubErate.cli:main'],
    },
    include_package_data=True,
)
