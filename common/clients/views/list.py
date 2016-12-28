# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..models import Client


@login_required
def list(request):

    company = request.user.profile.company_id

    clients = Client.objects.filter(company=company)

    return render(request, 'clients/list.py.jade', {'clients': clients})
