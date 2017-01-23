# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from ...models.products import Product
from ...models.recipies import Recipe, RecipeDetail
from ...forms.products.createSingle import CreateSingleProductForm
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
                                                    'barcode': product.barcode,
                                                    'unit': product.unit,
                                                    'description': product.description,
                                                    'department': product.department,
                                                    'subdepartment': product.subdepartment,
                                                    'cost': product.cost,
                                                    'hasforsale': product.hasforsale,
                                                    'utility': product.utility,
                                                    'price': product.price,
                                                    'usetaxes': product.usetaxes,
                                                    'taxes': product.taxes,
                                                    'discount': product.discount,
                                                    'sellprice': product.sellprice,
                                                    'minimum': product.minimum,
                                                    'useinventory': product.useinventory,
                                                    'isComposed': product.iscomposed,
                                                    })

            context = {'company': company,
                       'form': form
                       }

            return render(request, 'sales/products/create.py.jade', context)

        except Product.DoesNotExist:
            raise Http404("Producto no encontrado")

    if request.method == 'POST':

        form = CreateSingleProductForm(request.POST)

        if not form.is_valid():
            return render(request, 'sales/products/create.py.jade', {'form': form})
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
            recipeDetail = form.cleaned_data['recipe']

            if useinventory:
                minimum = form.cleaned_data['minimum']

            product = Product.objects.get(company=request.user.profile.company_id, code=pk)

            product.code = code
            product.barcode = barcode
            product.unit = unit
            product.description = description
            product.department = department
            product.subdepartment = subdepartment
            product.cost = cost
            product.minimum = minimum
            product.hasforsale = hasforsale
            product.utility = utility
            product.price = price
            product.usetaxes = usetaxes
            if usetaxes:
                product.taxes = taxes
            else:
                product.taxes = 0
            product.discount = discount
            product.sellprice = sellprice

            try:
                with transaction.atomic():

                    product.save()

                    if isComposed:
                        try:
                            recipe = Recipe.objects.get(company=company, product=product)
                            recipe.company = company
                            recipe.product = product
                            recipe.save()

                        except ObjectDoesNotExist:
                            recipe = Recipe(company=company, product=product)
                            recipe.save()

                    if 'btn-continue' in request.POST:
                        messages.add_message(request, messages.INFO, 'Producto actualizado correctamente',
                                             extra_tags="success")
                        return render(request, 'sales/products/create.py.jade', {'form': form})

                    if 'btn-save' in request.POST:
                        messages.add_message(request, messages.INFO, 'Producto actualizado correctamente',
                                             extra_tags="success")
                        return redirect('/admin/sales/product/')

            except Exception as e:
                if '.code' in str(e):
                    form.add_error('code', 'El código debe ser único')
                if '.barcode' in str(e):
                    form.add_error('barcode', 'El código de barras debe ser único')

                messages.add_message(request, messages.INFO, 'Error al crear el producto, por favor revise los campos' +
                                     ' e intente de nuevo. ' + str(e), extra_tags="danger")
                return render(request, 'sales/products/create.py.jade', {'form': form})
