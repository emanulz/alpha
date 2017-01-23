# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from ...models.recipies import Recipe, RecipeDetail
from ...models.products import Product, ProductDepartment, ProductSubDepartment
from ...forms.products.createSingle import CreateSingleProductForm
from django.db import transaction


@login_required
def product_create(request):

    if request.method == 'GET':

        company = request.user.profile.company_id
        departments = ProductDepartment.objects.filter(company=request.user.profile.company_id)
        subdepartments = ProductSubDepartment.objects.filter(company=request.user.profile.company_id)

        context = {'departments': departments,
                   'subdepartments': subdepartments,
                   'company': company,
                   'form': CreateSingleProductForm
                   }

        return render(request, 'sales/products/create.py.jade', context)

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

            useinventory = form.cleaned_data['useinventory']
            minimum = 0

            isComposed = form.cleaned_data['isComposed']
            hasforsale = form.cleaned_data['hasforsale']
            recipeDetail = form.cleaned_data['recipe']

            if useinventory:
                minimum = form.cleaned_data['minimum']

            product = Product(company=company, code=code, barcode=barcode, unit=unit, description=description,
                              department=department, subdepartment=subdepartment, cost=cost, minimum=minimum,
                              useinventory=useinventory, utility=utility, price=price, usetaxes=usetaxes, taxes=taxes,
                              discount=discount, sellprice=sellprice, hasforsale=hasforsale, iscomposed=isComposed)

            # productforsale = ProductForSale(company=company, product=product, code=code, barcode=barcode,
            #                                 description=description, department=department, subdepartment=subdepartment,
            #                                 unit=unit, utility=utility, price=price, usetaxes=usetaxes, taxes=taxes,
            #                                 discount=discount, sellprice=sellprice)
            try:
                with transaction.atomic():

                    product.save()

                    # if form.cleaned_data['hasforsale']:
                    #
                    #     product.hasforsale = form.cleaned_data['hasforsale']
                    #     product.save()

                    if isComposed:
                        recipe = Recipe(product=product, isComposed=isComposed, company=company)
                        recipe.save()

                    if 'btn-continue' in request.POST:
                        messages.add_message(request, messages.INFO, 'Producto creado correctamente', extra_tags="success")
                        return render(request, 'sales/products/create.py.jade', {'form': form})

                    if 'btn-other' in request.POST:
                        messages.add_message(request, messages.INFO, 'Producto creado correctamente', extra_tags="success")
                        return redirect('/sales/products/add/')

                    if 'btn-save' in request.POST:
                        messages.add_message(request, messages.INFO, 'Producto creado correctamente', extra_tags="success")
                        return redirect('/admin/sales/product/')

            except Exception as e:
                if '.code' in str(e):
                    form.add_error('code', 'El código debe ser único')
                if '.barcode' in str(e):
                    form.add_error('barcode', 'El código de barras debe ser único')

                messages.add_message(request, messages.INFO, 'Error al crear el producto, por favor revise los campos' +
                                     ' e intente de nuevo. ' + str(e), extra_tags="danger")
                return render(request, 'sales/products/create.py.jade', {'form': form})
