#!/usr/bin/env python3

from distutils.core import setup, Extension

module1 = Extension('k1a',
                    sources=['src/demo.c'])

setup(name='k1a',
      version='1.0',
      description='Accelerated functionalities for k1lib',
      author="Quang Ho",
      author_email="157239q@gmail.com",
      ext_modules=[module1])
