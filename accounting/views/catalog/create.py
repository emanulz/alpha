# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def account_create(request):

    if request.method == 'GET':

        company = request.user.profile.company_id

        context = {'company': company,
                   }

        return render(request, 'accounting/catalog/create.py.jade', context)
