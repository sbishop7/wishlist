# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User

class ProductManager(models.Manager):
    def add_product(self, postData, user_id):
        errors = []
        if len(postData['product']) < 3:
            errors.append('Item/Product name is too short!')
        response_to_views = {}

        if errors:
            response_to_views['status'] = False
            response_to_views['errors'] = errors
        else:
            new_item = self.create(product=postData['product'], creator=User.objects.get(id=user_id))
            self.get( id = new_item.id ).wanted_by.add( User.objects.get( id = user_id ) )
            response_to_views['status'] = True
        return response_to_views

    def add_wish(self, product_id, user_id):
        self.get( id = product_id ).wanted_by.add( User.objects.get( id = user_id ) )

    def remove_wish(self, product_id, user_id):
        self.get( id = product_id ).wanted_by.remove( User.objects.get( id = user_id ) )
        

class Product(models.Model):
    product = models.CharField(max_length=100)
    creator = models.ForeignKey(User, related_name="created")
    wanted_by = models.ManyToManyField(User, related_name="wants")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ProductManager()