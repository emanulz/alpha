# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def entry_create(request):

    if request.method == 'GET':

        company = request.user.profile.company_id

        context = {'company': company,
                   }

        return render(request, 'accounting/entries/create.py.jade', context)
