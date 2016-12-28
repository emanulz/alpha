# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from common.recipes.models import Recipe, RecipeDetail
from ..models import Product, ProductForSale
from ..forms import CreateSingleProductForm
from django.db import transaction
from django.http import Http404

from django.core.exceptions import ObjectDoesNotExist


@login_required
def product_update(request, pk):

    if request.method == 'GET':

        company = request.user.profile.company_id

        try:
            product = Product.objects.get(company=request.user.profile.company_id, code=pk)

            form = CreateSingleProductForm(initial={'code': product.code,
                                                    'unit': product.unit,
                                                    'description': product.description,
                                                    'department': product.department,
                                                    'subdepartment': product.subdepartment,
                                                    'cost': product.cost,
                                                    'hasforsale': product.hasforsale
                                                    })

            context = {'company': company,
                       'form': form
                       }

            return render(request, 'products/create.py.jade', context)

        except Product.DoesNotExist:
            raise Http404("Producto no encontrado")

    if request.method == 'POST':

        form = CreateSingleProductForm(request.POST)

        if not form.is_valid():
            return render(request, 'products/create.py.jade', {'form': form})
        else:

            company = request.user.profile.company
            code = form.cleaned_data['code']
            unit = form.cleaned_data['unit']
            description = form.cleaned_data['description']
            department = form.cleaned_data['department']
            subdepartment = form.cleaned_data['subdepartment']
            cost = form.cleaned_data['cost']

            barcode = form.cleaned_data['barcode']
            utility = form.cleaned_data['utility']
            price = form.cleaned_data['price']
            usetaxes = form.cleaned_data['usetaxes']
            taxes = form.cleaned_data['taxes']
            discount = form.cleaned_data['discount']
            sellprice = form.cleaned_data['sellprice']

            hasforsale = form.cleaned_data['hasforsale']

            useinventory = form.cleaned_data['useinventory']
            minimum = 0

            isComposed = form.cleaned_data['isComposed']
            recipe = form.cleaned_data['recipe']

            if useinventory:
                minimum = form.cleaned_data['minimum']

            product = Product.objects.get(company=request.user.profile.company_id, code=pk)

            product.code = code
            product.unit = unit
            product.description = description
            product.department = department
            product.subdepartment = subdepartment
            product.cost = cost
            product.minimum = minimum
            product.hasforsale = hasforsale

            if form.cleaned_data['hasforsale']:

                try:

                    productforsale = ProductForSale.objects.get(company=request.user.profile.company_id, code=pk)

                    productforsale.company = company
                    productforsale.product = product
                    productforsale.code = code
                    productforsale.barcode = barcode
                    productforsale.description = description
                    productforsale.department = department
                    productforsale.subdepartment = subdepartment
                    productforsale.unit = unit
                    productforsale.utility = utility
                    productforsale.price = price
                    productforsale.usetaxes = usetaxes
                    productforsale.taxes = taxes
                    productforsale.discount = discount
                    productforsale.sellprice = sellprice

                except ObjectDoesNotExist:

                    productforsale = ProductForSale(company=company, product=product, code=code, barcode=barcode,
                                                    description=description,
                                                    department=department, subdepartment=subdepartment, unit=unit,
                                                    utility=utility, price=price, usetaxes=usetaxes, taxes=taxes,
                                                    discount=discount, sellprice=sellprice)

            try:
                with transaction.atomic():

                    product.save()

                    if form.cleaned_data['hasforsale']:
                        productforsale.save()

                    if not isComposed:
                        try:
                            recipeObj = Recipe.objects.get(product=product)
                            recipeObj.product = product
                            recipeObj.save()

                        except ObjectDoesNotExist:
                            recipeObj = Recipe(product=product, isComposed=isComposed)
                            recipeObj.save()

                    if 'btn-continue' in request.POST:
                        messages.add_message(request, messages.INFO, 'Producto actualizado correctamente',
                                             extra_tags="success")
                        return render(request, 'products/create.py.jade', {'form': form})

                    if 'btn-save' in request.POST:
                        messages.add_message(request, messages.INFO, 'Producto actualizado correctamente',
                                             extra_tags="success")
                        return redirect('/products/')

            except Exception as e:
                if '.code' in str(e):
                    form.add_error('code', 'El código debe ser único')
                if '.barcode' in str(e):
                    form.add_error('barcode', 'El código de barras debe ser único')

                messages.add_message(request, messages.INFO, 'Error al crear el producto, por favor revise los campos' +
                                     ' e intente de nuevo. ' + str(e), extra_tags="danger")
                return render(request, 'products/create.py.jade', {'form': form})
