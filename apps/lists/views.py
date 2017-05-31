# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, reverse, redirect
from ..logreg.models import User
from .models import Product
from django.contrib import messages

def index(request):
    if 'user_id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'user_wishlist': Product.objects.filter(wanted_by__id=request.session['user_id']),
            'other_wishlist': Product.objects.all().exclude(wanted_by__id=request.session['user_id'])
        }
        return render(request, 'lists/index.html', context)
    else:
        return redirect( reverse( "logreg:index" ) ) 
    
def logout(request):
    del request.session['user_id']
    return redirect( "logreg:index" )

def create(request):
    if 'user_id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
        }
        return render(request, 'lists/create.html', context)
    else:
        return redirect( reverse( "logreg:index" ) ) 

def add_product(request):
    if 'user_id' in request.session:
        if request.method == 'POST':
            response = Product.objects.add_product(request.POST, request.session['user_id'])

            if response['status']:
                return redirect( reverse( "lists:index" ) )
            else:
                for error in response['errors']:
                    messages.error(request, error)
                return redirect('lists:create')
        else:
            return redirect( reverse( "lists:index" ) )
    else:
        return redirect( reverse( "logreg:index" ) ) 


def wish_items(request, id):
    if 'user_id' in request.session:
        context = {
            'user': User.objects.get(id=request.session['user_id']),
            'product': Product.objects.get(id=id),
            'other_users': User.objects.filter(wants=id).exclude(id=request.session['user_id'])
        }
        return render(request, 'lists/wish_items.html', context)
    else:
        return redirect( reverse( "logreg:index" ) ) 

def delete_product(request, id):
    if 'user_id' in request.session:
        Product.objects.get(id=id).delete()
        return redirect( reverse('lists:index') )
    else:
        return redirect( reverse( "logreg:index" ) )

def add_wish(request, id):
    if 'user_id' in request.session:
        Product.objects.add_wish(id, request.session['user_id'])
        return redirect( reverse('lists:index') )
    else:
        return redirect( reverse( "logreg:index" ) )

def remove_wish(request, id):
    if 'user_id' in request.session:
        Product.objects.remove_wish(id, request.session['user_id'])
        return redirect( reverse('lists:index') )
    else:
        return redirect( reverse( "logreg:index" ) )

