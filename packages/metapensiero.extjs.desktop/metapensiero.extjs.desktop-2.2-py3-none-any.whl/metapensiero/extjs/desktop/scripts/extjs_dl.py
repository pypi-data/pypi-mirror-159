# -*- coding: utf-8 -*-
# :Project:   metapensiero.extjs.desktop -- ExtJS downloader
# :Created:   dom 16 feb 2014 13:54:41 CET
# :Author:    Lele Gaifax <lele@metapensiero.it>
# :License:   GNU General Public License version 3 or later
# :Copyright: © 2014, 2016, 2021, 2022 Lele Gaifax
#

from hashlib import md5
from importlib.resources import files
from io import BytesIO
from os import makedirs
from os.path import dirname, exists, expanduser, join, normpath
from shutil import copyfileobj, rmtree
from urllib.request import urlopen
from zipfile import ZipFile


URL = 'http://cdn.sencha.com/ext/gpl/ext-4.2.1-gpl.zip'


def download_and_extract(url, replace=False, cache=None, all=False, src=False):
    "Download and extract ExtJS under assets/extjs."

    d = files('metapensiero.extjs.desktop') / 'assets/extjs'
    if exists(d):
        if replace:
            print('Removing existing %s...' % d)
            rmtree(d)
        else:
            print('%s already present!' % d)
            return

    f = None
    if cache:
        hashurl = md5(url.encode()).hexdigest()
        cache = expanduser(cache)
        cached = normpath(join(cache, hashurl))
        if exists(cached):
            print('Reusing cached archive %s' % cached)
            f = open(cached, 'rb')

    if f is None:
        print('Fetching %s...' % url)
        try:
            f = urlopen(url)
        except OSError:
            print(f'Could not fetch ExtJS archive from {url}!')
            return
        else:
            if cache:
                if not exists(cache):
                    makedirs(cache)
                print('Caching ExtJS archive into %s...' % cached)
                with open(cached, 'wb') as c:
                    copyfileobj(f, c)
                f = open(cached, 'rb')

    print(f'Extracting {url} into {d}...')

    z = ZipFile(BytesIO(f.read()))
    names = z.namelist()

    for n in sorted(names):
        if n.endswith('/'):
            continue
        # Extract just what's needed
        outn = n.partition('/')[2]
        if not outn:
            continue
        if ((all
             or outn.startswith('resources/')
             or (src and (outn.startswith('src/')
                          or outn == 'ext-dev.js')))):
            f = normpath(join(d, outn))
            outd = dirname(f)
            if not exists(outd):
                makedirs(outd)
            with open(f, 'wb') as o:
                o.write(z.read(n))
