# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from ..models import Client
from ..forms import CreateClientForm
from django.db import transaction


@login_required
def create(request):

    if request.method == 'GET':

        company = request.user.profile.company_id

        context = {'company': company,
                   'form': CreateClientForm
                   }

        return render(request, 'clients/create.py.jade', context)

    if request.method == 'POST':

        form = CreateClientForm(request.POST)

        if not form.is_valid():
            return render(request, 'clients/create.py.jade', {'form': form})
        else:

            company = request.user.profile.company
            code = form.cleaned_data['code']
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            id_type = form.cleaned_data['id_type']
            id_num = form.cleaned_data['id_num']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            has_credit = form.cleaned_data['has_credit']
            credit_limit = form.cleaned_data['credit_limit']
            debt = form.cleaned_data['debt']
            credit_days = form.cleaned_data['credit_days']

            client = Client(company=company, code=code, name=name, last_name=last_name, id_type=id_type,
                            id_num=id_num, address=address, phone=phone, email=email, has_credit=has_credit,
                            credit_limit=credit_limit, debt=debt, credit_days=credit_days, )

            try:
                with transaction.atomic():

                    client.save()

                    if 'btn-continue' in request.POST:
                        messages.add_message(request, messages.INFO, 'Cliente creado correctamente',
                                             extra_tags="success")
                        return render(request, 'clients/create.py.jade', {'form': form})

                    if 'btn-other' in request.POST:
                        messages.add_message(request, messages.INFO, 'Cliente creado correctamente',
                                             extra_tags="success")
                        return redirect('/clients/add/')

                    if 'btn-save' in request.POST:
                        messages.add_message(request, messages.INFO, 'Cliente creado correctamente',
                                             extra_tags="success")
                        return redirect('/clients/')

            except Exception as e:
                if '.code' in str(e):
                    form.add_error('code', 'El código debe ser único')

                messages.add_message(request, messages.INFO, 'Error al crear el producto, por favor revise los campos' +
                                     ' e intente de nuevo. ' + str(e), extra_tags="danger")
                return render(request, 'clients/create.py.jade', {'form': form})
