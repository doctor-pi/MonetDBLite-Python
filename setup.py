#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy
from distutils.core import setup, Extension

basedir = os.path.dirname(os.path.realpath(__file__))

try:
    import pypandoc
    long_description = pypandoc.convert_file(os.path.join(basedir, 'README.md'), 'rst')
except(IOError, ImportError):
    long_description = ''

sources = []
includes = [numpy.get_include()]
excludes = ['strptime.c', 'inlined_scripts.c', 'decompress.c', 'fsync.c']

def generate_sources_includes(dir):
    includes.append(dir)
    for root, dirs, files in os.walk(dir):
        for name in files:
            if name.endswith('.c') and not name in excludes:
                sources.append(os.path.join(root, name))
        for name in dirs:
            includes.append(os.path.join(root, name))

generate_sources_includes('src/monetdblite/src')
generate_sources_includes('src/embeddedpy')


libmonetdb5 = Extension('monetdblite.libmonetdb5',
    define_macros = [('LIBGDK',              None),
                     ('LIBMAL',              None),
                     ('LIBOPTIMIZER',        None),
                     ('LIBSTREAM',           None),
                     ('LIBSQL',              None),
                     ('LIBPYAPI',            None),
                     ('MONETDBLITE_COMPILE', None)],
    include_dirs = includes,
    sources = sources,
    extra_compile_args=['-std=c99'],
    language='c')

setup(
    name = "monetdblite",
    version = '0.6.0.post6',
    description = 'Embedded MonetDB Python Database.',
    author = 'Mark Raasveldt, Hannes Mühleisen',
    author_email = 'm.raasveldt@cwi.nl',
    keywords = 'MonetDB, MonetDBLite, Database',
    packages = ['monetdblite'],
    url="https://github.com/hannesmuehleisen/MonetDBLite-Python",
    long_description = long_description,
    install_requires=[
        'numpy',
    ],
    zip_safe = False,
    ext_modules = [libmonetdb5]
)
