# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ...models.products import Product


@login_required
def product_list(request):

    company = request.user.profile.company_id

    products = Product.objects.filter(company=company)

    return render(request, 'sales/products/list.py.jade', {'products': products})
