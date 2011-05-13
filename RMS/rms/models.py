from django.db import models

# Create your models here.


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    owner = models.CharField(max_length=32)

    def __unicode__(self):
        return self.name

class Backlog(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product)
    stories = models.TextField()
    prioritized = models.IntegerField()
    estimated = models.FloatField()
    value = models.IntegerField()
    how_to_demo = models.TextField()
    committer = models.CharField(max_length=32)
    state = models.CharField(max_length=32)
    gmt_create = models.DateTimeField(auto_now_add=True)
    gmt_last_modify = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.stories
