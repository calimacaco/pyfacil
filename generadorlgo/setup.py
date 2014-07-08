# -*- coding: iso-8859-1 -*-
from distutils.core import setup
import py2exe

setup(name="ConvertLgo",
version="1.0",
description="F2S Conversor de logos",
author="SimpleSoft.com ltda",
author_email="soportesimplesoft@gmail.com",
url="www.cali2s.com",
license="GNU",
scripts=["convert_lgo.py"],
windows=["convert_lgo.py"],
options={"py2exe": {"bundle_files": 1}}, 
zipfile=None
 )

