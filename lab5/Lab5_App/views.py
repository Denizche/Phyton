from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View


data = {'orders': []}
for i in range(1, 40):
    data['orders'].append(
        {
            'id': i,
            'title': '{0}{1}'.format('Order N', i),
            'description': 'Very useful description №{}'.format(i),
            'text': 'Very useful text №{}'.format(i),
            'date': '29.12.2017'
        }
    )


def function_view(request):
    return HttpResponse('response from func view')


class ClassBased(View):
    def get(self, request):
        return HttpResponse('response from class based view')


def main_page(request):
    return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data_order = {
            'order': data['orders'][int(id)-1]
        }
        return render(request, 'order.html', data_order)
