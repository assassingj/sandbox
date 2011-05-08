__author__ = 'gaojian'

from django.contrib import admin
from casestudy.models import Publisher, Author, Book

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
  