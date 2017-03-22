# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from accounting.models.reports import Report
from accounting.models.entries import EntryDetail
from accounting.models.catalog import Account
from datetime import datetime


@login_required
def report_create(request):

    company = request.user.profile.company

    report = request.GET['report']
    dateini = request.GET['dateini']
    dateend = request.GET['dateend']
    date_ini = datetime.strptime(request.GET['dateini'], '%Y-%m-%d')
    date_end = datetime.strptime(request.GET['dateend'], '%Y-%m-%d')

    totalDebe = 0
    totalHaber = 0

    if report:
        reportObj = Report.objects.get(id=report)

        details = EntryDetail.objects.filter(company=company)
        accounts = Account.objects.order_by('level__level').filter(company=company)

        if reportObj.template == 'tmp1':

            details = details.filter(date__range=[dateini, dateend])

            results = []

            for account in accounts:

                code = getCode(account, accounts)

                resAccount = AccountToShow(account, getDebe(account, details), getHaber(account, details),
                                           code, getDifference(account, details))
                results.append(resAccount)

            for result in results:

                totalDebe = 0
                totalHaber = 0

                totalDebe += result.debe
                totalHaber += result.haber

            def getKey(item):
                return item.code

            orderedResults = sorted(results, key=getKey)

            context = {
                'header': reportObj.header,
                'dateini': date_ini,
                'dateend': date_end,
                'report': report,
                'results': orderedResults,
                'company': company,
                'debe': totalDebe,
                'haber': totalHaber,
                'difference': totalDebe - totalHaber,
                }

            return render(request, '../templates/accounting/reports/template1/template.py.jade', context)

        raise Http404

    raise Http404


class AccountToShow:

    def __init__(self, account, debe, haber, code, difference):
        self.id = account.id
        self.account = account
        self.debe = debe
        self.haber = haber
        self.code = code
        self.difference = difference


def getDebe(account, details):

    debe = 0
    details = details.filter(account=account)
    for detail in details:
        debe += detail.debe
    return debe


def getCode(account, accounts):

    if account.parent is None:
        print account.name + 'code:' + account.identifier + '.'
        return account.identifier + '.'

    parentAccount = accounts.get(id=account.parent.id)
    return getCode(parentAccount, accounts) + account.identifier + '.'


def getHaber(account, details):

    haber = 0
    details = details.filter(account=account)
    for detail in details:
        haber += detail.haber
    return haber


def getDifference(account, details):

    debe = getDebe(account, details)
    haber = getHaber(account, details)

    return debe - haber
