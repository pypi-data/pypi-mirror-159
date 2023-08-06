from setuptools import setup, find_packages

setup(
    name="openai-clip",
    version="1.0.1",
    description="",
    author="OpenAI",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        'ftfy',
        'regex',
        'tqdm',
    ],
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)
