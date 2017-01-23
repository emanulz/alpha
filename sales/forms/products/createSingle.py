# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ...models.products import ProductDepartment, ProductSubDepartment

from django import forms


class CreateSingleProductForm(forms.Form):

    code = forms.IntegerField(min_value=0, )
    description = forms.CharField(max_length=255)
    department = forms.ModelChoiceField(queryset=ProductDepartment.objects.all())
    subdepartment = forms.ModelChoiceField(queryset=ProductSubDepartment.objects.all())
    unit = forms.CharField(max_length=3)
    cost = forms.DecimalField(min_value=0)

    useinventory = forms.BooleanField(required=False)
    inventory = forms.FloatField(initial=0, required=False)
    minimum = forms.FloatField(initial=0, required=False)

    hasforsale = forms.BooleanField(required=False)
    barcode = forms.IntegerField(min_value=0, required=False)
    utility = forms.DecimalField(min_value=0, required=False)
    price = forms.DecimalField(min_value=0, required=False)
    usetaxes = forms.BooleanField(initial=False, required=False)
    taxes = forms.DecimalField(min_value=0, max_value=100, required=False)
    discount = forms.DecimalField(min_value=0, max_value=99.99, initial=0, required=False)
    sellprice = forms.DecimalField(min_value=0, required=False)

    isComposed = forms.BooleanField(required=False)
    recipe = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(CreateSingleProductForm, self).__init__(*args, **kwargs)
        for k, field in self.fields.items():

            if 'out_of_range' in field.error_messages:
                field.error_messages['out_of_range'] = 'Error en Valor'
            if 'required' in field.error_messages:
                field.error_messages['required'] = 'Obligatorio'

    def clean(self):

        cleaned_data = super(CreateSingleProductForm, self).clean()

        useinventory = cleaned_data.get("useinventory")
        inventory = cleaned_data.get("inventory")
        minimum = cleaned_data.get("minimum")

        hasforsale = cleaned_data.get("hasforsale")
        barcode = cleaned_data.get("barcode")
        utility = cleaned_data.get("utility")
        price = cleaned_data.get("price")
        discount = cleaned_data.get("discount")
        sellprice = cleaned_data.get("sellprice")

        usetaxes = cleaned_data.get("usetaxes")
        taxes = cleaned_data.get("taxes")

        isComposed = cleaned_data.get("isComposed")
        recipe = cleaned_data.get("recipe")

        if isComposed:
            if not recipe:
                self.add_error('recipe', "Obligatorio")

        if useinventory:
            # Only do something if both fields are valid so far.
            if not inventory:
                self.add_error('inventory', "Obligatorio")
            if not minimum:
                self.add_error('minimum', "Obligatorio")

        if hasforsale:
            # Only do something if both fields are valid so far.
            if not barcode:
                self.add_error('barcode', "Obligatorio")
            if not utility and utility != 0:
                self.add_error('utility', "Obligatorio")
            if not price and price != 0:
                self.add_error('price', "Obligatorio")
            if not discount and discount != 0:
                self.add_error('discount', "Obligatorio")
            if not sellprice:
                self.add_error('sellprice', "Obligatorio")
            if usetaxes:
                if not taxes:
                    self.add_error('taxes', "Obligatorio")
