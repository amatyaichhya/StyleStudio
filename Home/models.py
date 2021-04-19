from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="image/")


class Trending(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="image/")
    price = models.IntegerField(blank=True, null=True)


class Style(models.Model):
    style = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="image/")


class New(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="image/")
    price = models.IntegerField(blank=True, null=True)


class Top(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="image/")
    price = models.IntegerField(blank=True, null=True)


class Recommend(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to="image/")
    price = models.IntegerField(blank=True, null=True)