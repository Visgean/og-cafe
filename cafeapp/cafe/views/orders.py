import datetime

from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import permission_required
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from cafeapp.cafe.models import Product, Order, SubOrder


class OrderForm(ModelForm):
	class Meta:
		model = Order
		exclude = ("selled_by", "sub_orders")

OrderFormset = modelformset_factory(Order, exclude=("selled_by", "sub_orders", "customer"), extra=0, can_delete=True)



@csrf_protect
@permission_required("Cafe.add_order")
def new(request):
	if request.method == 'POST':
		form = OrderForm(request.POST)
		if form.is_valid():
			if request.POST.has_key("order_id"): # if this is old order from order_expand func
				order = Order.objects.get(id=request.POST["order_id"])
				order.selled_by = request.user 
				order.sub_orders.clear() # delete all sub orders because we are going to get them again
				order.save()				
			else:
				order = form.save(commit=False) # we cannot actually save 
												# cause we have to fullfill model before save
				order.selled_by = request.user 
				form.save() # we have to pre-save to get primary key which can be used for back-references
							# for foreign_key
			
			# handling suborders
			sub_orders = zip(request.POST.getlist("products"), request.POST.getlist("quantity"))
			for product_id, quantity in sub_orders:
				if int(quantity):
					product_obj = Product.objects.get(id=int(product_id))
					sub_order_obj = SubOrder(product=product_obj, quantity=int(quantity))   # we actually create new sub order
					sub_order_obj.save()														# so we can add more of similar sub 
					order.sub_orders.add(sub_order_obj)										 # orders on the same time...
																						
				
			order.save()

			return HttpResponseRedirect(reverse("unpaid"))
	else:
		form = OrderForm() # if this is new request
		
	context = {
			   "products" : Product.objects.filter(available=True).order_by("name"),
			   "form": form,
			   }
	
	return direct_to_template(request, "cafe/orders/new.djhtml", context)

@csrf_protect
@permission_required("Cafe.add_order")
def expand(request, order_id):
	order_obj = get_object_or_404(Order, id=order_id)
	form = OrderForm(instance=order_obj) 

	context = {
			   "products" : Product.objects.filter(available=True).order_by("name"),
			   "form": form,
			   }
	
	return direct_to_template(request, "cafe/orders/expand.djhtml", context)

@csrf_protect
@permission_required("Cafe.add_order")
def display_order_formset(request, queryset, redirect=None):	
	if request.method == 'POST':
		formset = OrderFormset(request.POST)
		if formset.is_valid():
			formset.save()
			return HttpResponseRedirect(redirect if redirect else reverse("unpaid"))
	else: # we assume this is new request
		formset = OrderFormset(queryset=queryset)

	context = {
			   "products" : Product.objects.filter(available=True),
			   "formset": formset,
			   }
	
	
	return direct_to_template(request, "cafe/orders/formset.djhtml", context)


def unpaid(request):
	"Manage unpaid orders"
	return display_order_formset(request, Order.objects.filter(paid=False), redirect=reverse("unpaid"))

def today(request):
	return display_order_formset(request, Order.objects.filter(day__startswith=datetime.datetime.today().date()), redirect=reverse("today"))
