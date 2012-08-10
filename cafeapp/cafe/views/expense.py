from django.forms import ModelForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import permission_required
from django.views.generic.simple import direct_to_template
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


from cafeapp.cafe.models import Expanse

Expanse.objects.filter()

class ExpanseForm(ModelForm):
    class Meta:
        model = Expanse
        exclude = ("user")

@csrf_protect
@permission_required("Cafe.add_expanse")
def new(request):
    if request.method == 'POST':
        form = ExpanseForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False) 
            order.user = request.user 
            form.save()
            return HttpResponseRedirect(reverse("new_expense"))
    else:
        form = ExpanseForm()
    
    context = {
               "form" : form,
               }

    return direct_to_template(request, "cafe/expense/new.djhtml", context)


@permission_required("Cafe.add_expanse")
def view(request):
    context = {
               "expanses" : Expanse.objects.all()
               }

    return direct_to_template(request, "cafe/expense/view.djhtml", context)
