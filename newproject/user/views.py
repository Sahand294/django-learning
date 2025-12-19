from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@method_decorator(csrf_exempt,name='dispatch')
class UserView(View):
    def get(self,request):
        return HttpResponse(f'get user')

    def post(self,request):
        return HttpResponse(f'post user')

    def put(self,request):
        return HttpResponse(f'put user')

    def delete(self,request):
        return HttpResponse(f'delete user')
