from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.contrib.auth.decorators import permission_required
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect

from Lisculea.Cafe.models import Product



class ProductForm(ModelForm):
    class Meta:
        model = Product

product_formset = modelformset_factory(Product, extra=0)

@permission_required("Cafe.add_product")
def new(request):
    "view for adding new product"
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/cafe/products/new")
    else:
        form = ProductForm()
    
    context = {
               "form" : form,
               }

    return direct_to_template(request, "cafe/products/new.djhtml", context)

@permission_required("Cafe.delete_product")
def manage(request):
    if request.method == 'POST':
        formset = product_formset(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/cafe/products/manage")
    else: # we assume this is new request
        formset = product_formset(queryset = Product.objects.all())

    context = {
               "formset": formset,
               }
    
    return direct_to_template(request, "cafe/products/manage.djhtml", context)
