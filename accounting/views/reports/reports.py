# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from accounting.models.reports import Report
from accounting.models.entries import EntryDetail
from accounting.models.catalog import Account


@login_required
def report_create(request):

    company = request.user.profile.company

    report = request.GET['report']
    date_ini = request.GET['dateini']
    date_end = request.GET['dateend']

    if report:
        reportObj = Report.objects.get(id=report)

        details = EntryDetail.objects.filter(company=company)
        accounts = Account.objects.order_by('level__level').filter(company=company)

        if reportObj.template == 'tmp1':

            details = details.filter(date__range=[date_ini, date_end])

            results = []

            for account in accounts:

                account = AccountToShow(account, getDebe(account, details), getHaber(account, details), getCode(account, details) )
                results.append(account)

            print results

            context = {
                'header': reportObj.header,
                'dateini': date_ini,
                'dateend': date_end,
                'report': report,
                'results': results,
                }

            return render(request, '../templates/accounting/reports/template1/template.py.jade', context)

        raise Http404

    raise Http404


class AccountToShow:

    def __init__(self, account, debe, haber, code):
        self.id = account.id
        self.account = account
        self.debe = debe
        self.haber = haber
        self.code = code

def getDebe(account, details):

    details = details.filter(account=account)
    return True

def getCode(account, details):

    details = details.filter(account=account)
    return True

def getHaber(account, details):

    details = details.filter(account=account)
    return True
