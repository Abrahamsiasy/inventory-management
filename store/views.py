from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from users.models import User
from .models import (
    Supplier,
    Buyer,
    Type,
    Drop,
    Product,
    Order,
    Delivery
)
from .forms import (
    SupplierForm,
    BuyerForm,
    TypeForm,
    DropForm,
    ProductForm,
    OrderForm,
    DeliveryForm
)


# Supplier views
@login_required(login_url='login')
def create_supplier(request):
    forms = SupplierForm()
    if request.method == 'POST':
        forms = SupplierForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            phone = forms.cleaned_data['phone']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(
                    username=username, password=password,
                    email=email, is_supplier=True
                )
                Supplier.objects.create(user=user, name=name, address=address, phone=phone)
                return redirect('supplier-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_supplier.html', context)


class SupplierListView(ListView):
    model = Supplier
    template_name = 'store/supplier_list.html'
    context_object_name = 'supplier'


# Buyer views
@login_required(login_url='login')
def create_buyer(request):
    forms = BuyerForm()
    if request.method == 'POST':
        forms = BuyerForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            address = forms.cleaned_data['address']
            phone = forms.cleaned_data['phone']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            retype_password = forms.cleaned_data['retype_password']
            if password == retype_password:
                user = User.objects.create_user(
                    username=username, password=password,
                    email=email, is_buyer=True
                )
                Buyer.objects.create(user=user, name=name, address=address, phone=phone)
                return redirect('buyer-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_buyer.html', context)


class BuyerListView(ListView):
    model = Buyer
    template_name = 'store/buyer_list.html'
    context_object_name = 'buyer'


# Type views
@login_required(login_url='login')
def create_type(request):
    forms = TypeForm()
    if request.method == 'POST':
        forms = TypeForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('type-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_type.html', context)


class TypeListView(ListView):
    model = Type
    template_name = 'store/type_list.html'
    context_object_name = 'type'


# Drop views
@login_required(login_url='login')
def create_drop(request):
    forms = DropForm()
    if request.method == 'POST':
        forms = DropForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('drop-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_drop.html', context)


class DropListView(ListView):
    model = Drop
    template_name = 'store/drop_list.html'
    context_object_name = 'drop'


# Product views
@login_required(login_url='login')
def create_product(request):
    forms = ProductForm()
    if request.method == 'POST':
        forms = ProductForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_product.html', context)



class ProductListView(ListView):
    model = Product
    template_name = 'store/product_list.html'
    context_object_name = 'product'


# Order views
@login_required(login_url='login')
def create_order(request):
    forms = OrderForm()
    if request.method == 'POST':
        forms = OrderForm(request.POST)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            design = forms.cleaned_data['design']
            amount = forms.cleaned_data['amount']
            buyer = forms.cleaned_data['buyer']
            type = forms.cleaned_data['type']
            drop = forms.cleaned_data['drop']
            Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                amount=amount,
                buyer=buyer,
                type=type,
                drop=drop,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_order.html', context)



# Edit order views
@login_required(login_url='login')
def update_order(request,item_id):
    forms = OrderForm()
    order_object = Order.objects.get(id=item_id)
    if request.method == 'POST':
        forms = OrderForm(request.POST or None, instance=order_object)
        if forms.is_valid():
            supplier = forms.cleaned_data['supplier']
            product = forms.cleaned_data['product']
            design = forms.cleaned_data['design']
            amount = forms.cleaned_data['amount']
            buyer = forms.cleaned_data['buyer']
            type = forms.cleaned_data['type']
            drop = forms.cleaned_data['drop']
            Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                amount=amount,
                buyer=buyer,
                type=type,
                drop=drop,
                status='pending'
            )
            return redirect('order-list')
    context = {
        'form': forms,
        'order_object':order_object
    }
    return render(request, 'store/create_order.html', context)

class OrderListView(ListView):
    model = Order
    template_name = 'store/order_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.all().order_by('-id')
        return context


# Delivery views
@login_required(login_url='login')
def create_delivery(request):
    forms = DeliveryForm()
    if request.method == 'POST':
        forms = DeliveryForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms
    }
    return render(request, 'store/create_delivery.html', context)

# Delivery edit views
@login_required(login_url='login')
def update_delivery(request, item_id):
    forms = DeliveryForm()
    delivery_object = Delivery.objects.get(id=item_id)
    if request.method == 'POST':
        forms = DeliveryForm(request.POST or None, instance=delivery_object)
        if forms.is_valid():
            forms.save()
            return redirect('delivery-list')
    context = {
        'form': forms,
        'delivery_object':delivery_object
    }
    return render(request, 'store/create_delivery.html', context)

# update Product views
@login_required(login_url='login')
def update_product(request, item_id):
    forms = ProductForm()
    product_object = Product.objects.get(id=item_id)
    if request.method == 'POST':
        forms = ProductForm(request.POST or None, instance=product_object)
        if forms.is_valid():
            forms.save()
            return redirect('product-list')
    context = {
        'form': forms,
        'product_object':product_object
    }
    return render(request, 'store/create_product.html', context)

class DeliveryListView(ListView):
    model = Delivery
    template_name = 'store/delivery_list.html'
    context_object_name = 'delivery'
