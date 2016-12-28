# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from ..models import Client
from ..forms import CreateClientForm
from django.db import transaction
from django.http import Http404

from django.core.exceptions import ObjectDoesNotExist


@login_required
def update(request, pk):

    if request.method == 'GET':

        company = request.user.profile.company_id

        try:
            client = Client.objects.get(company=request.user.profile.company_id, code=pk)

            form = CreateClientForm(initial={'code': client.code,
                                             'name': client.name,
                                             'last_name': client.last_name,
                                             'id_type': client.id_type,
                                             'id_num': client.id_num,
                                             'address': client.address,
                                             'phone': client.phone,
                                             'email': client.email,
                                             'has_credit': client.has_credit,
                                             'credit_limit': client.credit_limit,
                                             'credit_days': client.credit_days,
                                             'debt': client.debt,
                                             })

            context = {'company': company,
                       'form': form
                       }

            return render(request, 'clients/create.py.jade', context)

        except ObjectDoesNotExist:
            raise Http404("Cliente no encontrado")

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

            client = Client.objects.get(company=request.user.profile.company_id, code=pk)

            client.company = company
            client.code = code
            client.name = name
            client.last_name = last_name
            client.id_type = id_type
            client.id_num = id_num
            client.address = address
            client.phone = phone
            client.email = email
            client.has_credit = has_credit
            client.credit_limit = credit_limit
            client.debt = debt
            client.credit_days = credit_days

            try:
                with transaction.atomic():

                    client.save()

                    if 'btn-continue' in request.POST:
                        messages.add_message(request, messages.INFO, 'Cliente actualizado correctamente',
                                             extra_tags="success")
                        return render(request, 'clients/create.py.jade', {'form': form})

                    if 'btn-save' in request.POST:
                        messages.add_message(request, messages.INFO, 'Cliente actualizado correctamente',
                                             extra_tags="success")
                        return redirect('/clients/')

            except Exception as e:
                if '.code' in str(e):
                    form.add_error('code', 'El código debe ser único')

                messages.add_message(request, messages.INFO, 'Error al actualizar el Cliente, por favor revise los campos' +
                                     ' e intente de nuevo. ' + str(e), extra_tags="danger")
                return render(request, 'clients/create.py.jade', {'form': form})
