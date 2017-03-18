from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from ..models.reports import Report
from .filters.reports import ReportFilter

# API


class ReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ('id', 'company', 'name', 'header', 'accountsToSum', 'accountsToShow', 'template')


class ReportViewSet(viewsets.ModelViewSet):

    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    lookup_field = 'id'
    filter_class = ReportFilter
