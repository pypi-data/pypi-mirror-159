from setuptools import setup

name = "types-xxhash"
description = "Typing stubs for xxhash"
long_description = '''
## Typing stubs for xxhash

This is a PEP 561 type stub package for the `xxhash` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `xxhash`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/xxhash. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `85077b273d15eb837cddc7e9ed5bcaf5661c2f3e`.
'''.lstrip()

setup(name=name,
      version="3.0.4",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/xxhash.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['xxhash-stubs'],
      package_data={'xxhash-stubs': ['__init__.pyi', 'version.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
