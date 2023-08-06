#!/usr/bin/env python

from setuptools import setup

setup(name='hfmonthlyreport',
      version='0.1',
      description='Send monthly file count only to monthly report server',
      author='VishalJain_NIOT',
      author_email='vishaljain9516@gmail.com',
      packages=['hfmonthlyreport'],
      install_requires=['requests','PyAutoGUI==0.9.53','pyperclip==1.8.2','qrcode'])

