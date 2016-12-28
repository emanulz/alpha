# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms


class CreateClientForm(forms.Form):

    person = 'per'
    juridic = 'jur'
    passport = 'pas'

    ID_TYPE_CHOICES = ((person, 'Cédula Física'),
                       (juridic, 'Cédula Jurídica'),
                       (passport, 'Pasaporte'),
                       )

    name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    code = forms.IntegerField(min_value=0, )
    id_type = forms.ChoiceField(choices=ID_TYPE_CHOICES, initial=person)
    id_num = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255, required=False)
    phone = forms.CharField(max_length=255, required=False)
    email = forms.EmailField(required=False)
    has_credit = forms.BooleanField(required=False)
    credit_limit = forms.DecimalField(min_value=0, required=False)
    debt = forms.DecimalField(min_value=0, required=False)
    credit_days = forms.IntegerField(min_value=0, required=False)

    def __init__(self, *args, **kwargs):
        super(CreateClientForm, self).__init__(*args, **kwargs)
        for k, field in self.fields.items():

            if 'out_of_range' in field.error_messages:
                field.error_messages['out_of_range'] = 'Error en Valor'
            if 'required' in field.error_messages:
                field.error_messages['required'] = 'Obligatorio'

    def clean(self):

        cleaned_data = super(CreateClientForm, self).clean()

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
            if not utility:
                self.add_error('utility', "Obligatorio")
            if not price:
                self.add_error('price', "Obligatorio")
            if not discount:
                self.add_error('discount', "Obligatorio")
            if not sellprice:
                self.add_error('sellprice', "Obligatorio")
            if usetaxes:
                if not taxes:
                    self.add_error('taxes', "Obligatorio")
