from .serializers import IapSerializer
from .models import Iap


import csv
import pandas

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

excel_data_df = pandas.read_excel('/Users/rahultyagi/Downloads/iap_requirements.xlsx', sheet_name="Input")
# ma=excel_data_df['macaddr'][0]
# new_ma = ':'.join(ma[i:i+2] for i in range(0,12,2))
# print(new_ma.lower())
# json_data = excel_data_df.to_dict()
print(excel_data_df)

# print(type(json_data))

# print(json_data["macaddr"])

class IapViewSet(viewsets.ModelViewSet):
    queryset = Iap.objects.all()
    serializer_class = IapSerializer


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def site_list(self,request):
    list = [
        #breakpoint()
        Iap(
            site_id = df['site_id'],
            site_name = df['site_name'],
            country = df['country'],
            order_id = df['order_id'],
            purchase_id = df['purchase_id'],
            csm_name = df['csm_name'],
            serial = df['serial'].lower(),
            ip_address = df['ip_address'],
            model = df['model'],
            macaddr = ':'.join(df['macaddr'][i:i+2] for i in range(0,12,2))
        )
        for i, df in excel_data_df.iterrows()
    ]
    # breakpoint()
    Iap.objects.bulk_create(list)

    return Response("Successfully")

