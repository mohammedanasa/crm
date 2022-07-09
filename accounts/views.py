from django.shortcuts import render, redirect 
from django.http import HttpResponse

from accounts.models import Customer, Product, Order
from .forms import OrderForm 
from .filters import OrderFilter


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

def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders =  Order.objects.all()
    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs
    order_count = orders.count()
    context = {'customer':customer, 'orders':orders, 'order_count':order_count, 'myFilter':myFilter }
    return render(request,'accounts/customers.html',context)

def createOrder(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing Post:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        #print('Printing Post:', request.POST)
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item':order}
    return render(request, 'accounts/delete.html', context)


