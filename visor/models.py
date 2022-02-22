from django.db import models

# Create your models here.
class Text:
     def __init__(self, pages, fromPage, toPage):
        self.content = pages
        self.fromPage = fromPage
        self.toPage = toPage