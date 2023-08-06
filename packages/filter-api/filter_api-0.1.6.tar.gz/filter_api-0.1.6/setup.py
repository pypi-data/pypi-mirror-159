from setuptools import setup, find_packages


setup(
    name='filter_api',
    version='0.1.6',
    license='MIT',
    author="Pratyush Makkar",
    author_email='pratyushmakkar@gmail.com',
    packages=find_packages(),
    url='https://github.com/PratyushMakkar/fastapi-filter',
    keywords='Implement request path level filtering for HTTP Requests in FastAPI',
    install_requires=[
          'fastapi',
          'starlette',
          'uvicorn'
      ],
)