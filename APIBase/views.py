from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .models import Standard, ResourceRequirement
from .serializers import StandardSerializer, StandardMiniSerializer


class Base(View):

    standarts = Standard.objects.order_by('-pk')

    def get(self, response):
        return render(self.request, 'first_test.html', {'data': self.standarts})


class BaseViewSet(viewsets.ModelViewSet):
    serializer_class = StandardMiniSerializer
    queryset = Standard.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StandardSerializer(instance)
        return Response(serializer.data)


    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, )

def index(response):
    res = Standard.objects.all()
    data = ''
    for item in res:
        data += f'{item.searchCode}<br>'
        for r in item.must.all():

            data += f'{r} {r.expenditure.unit} {r.consumptionRate}<br>'
        data += '<br><br><br>'
        print(item.must.all())
    return HttpResponse(data)