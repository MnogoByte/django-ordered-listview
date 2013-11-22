# -*- coding: utf-8 -*-
from distutils.core import setup


setup(name='django-ordered-listview',
      version='0.0.2',
      description='This library is aimed to simplify creation of user sorted lists.',
      author='Alexander Klimenko',
      author_email='alex@erix.ru',
      long_description = open('README.rst').read(),
      url='https://github.com/meteozond/django-ordered-listview',
      packages=['ordered_listview', 'ordered_listview.templatetags'],
      classifiers=[
            "Framework :: Django",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Topic :: Software Development"
      ],
      license="BSD",
      )
