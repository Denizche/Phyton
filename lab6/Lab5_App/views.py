from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from datetime import datetime
from Lab5_App.models import Test, User

data = {'orders': []}


def function_view(request):
    return HttpResponse('response from func view')


class ClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


def main_page(request):
    data = {'orders': []}
    try:
        if int(request.GET["count"]) > 0:
            count=int(request.GET["count"])
    except:
        count=10
    for i in range(1, count + 1):
                data['orders'].append(
                    {
                        'id': i ,
                        'title': '{0}{1}'.format('Order N', i),
                        'description': 'Very useful description №{}'.format(i),
                        'text': 'Very useful text №{}'.format(i),
                        'date': '{}'.format(datetime.now())
                    }
        )
    return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data = {'orders': []}
        i = id
        for j in range(1, int(i) + 1):
            data['orders'].append(
                {
                    'id': j,
                    'title': '{0}{1}'.format('Order N', j),
                    'description': 'Very useful description №{}'.format(j),
                    'text': 'Very useful text №{}'.format(j),
                    'date': '{}'.format(datetime.now())
                }
            )
        data_order = {
            'order': data['orders'][int(id)-1]
        }
        return render(request, 'order.html', data_order)


class TestView(ListView):
    model = Test
    context_object_name = 'tests'

    def get_queryset(self):
        q = super().get_queryset()
        return q

class UserView(View):

    def get(self, request):
        users = User.objects.all()
        return render(request, 'users.html')