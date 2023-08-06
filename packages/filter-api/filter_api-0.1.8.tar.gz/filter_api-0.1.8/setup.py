from setuptools import setup, find_packages


setup(
    name='filter_api',
    version='0.1.8',
    license='MIT',
    author="Pratyush Makkar",
    author_email='pratyushmakkar@gmail.com',
    packages=find_packages(),
    url='https://github.com/PratyushMakkar/fastapi-filter',
    description="Implement filters for each request path before they are handled by the main function.",
    long_description= 'README.md',
    keywords='fastapi filter Starlette uvicorn',
    install_requires=[
          'fastapi',
          'starlette',
          'uvicorn'
      ],
)