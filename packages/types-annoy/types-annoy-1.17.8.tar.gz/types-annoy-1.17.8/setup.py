from setuptools import setup

name = "types-annoy"
description = "Typing stubs for annoy"
long_description = '''
## Typing stubs for annoy

This is a PEP 561 type stub package for the `annoy` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `annoy`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/annoy. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `e3d4bdc91a792bcef5d8eae2c1abab3d4ba27541`.
'''.lstrip()

setup(name=name,
      version="1.17.8",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/annoy.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['annoy-stubs'],
      package_data={'annoy-stubs': ['__init__.pyi', 'annoylib.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
