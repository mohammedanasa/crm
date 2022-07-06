from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Customer, Product, Order


def home(request):
    orders = Order.objects.all()
    customers=Customer.objects.all()
    total_customer = customers.count()
    total_order = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    context = {'orders':orders,'customers':customers,'total_order':total_order,'delivered':delivered, 'pending':pending}
    return render(request,'accounts/dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request,'accounts/products.html', {'products':products})

def customer(request):
    return render(request,'accounts/customers.html')


