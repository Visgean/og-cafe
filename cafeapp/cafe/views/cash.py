from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.views.generic.simple import direct_to_template
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect

from cafeapp.cafe.models import CashboxState




class CashboxStateForm(ModelForm):
    class Meta:
        model = CashboxState
        exclude = ("day_of_the_counting","accounted_by", "predicted_result")
        
cashbox_formset = modelformset_factory(CashboxState, extra = 0, can_delete = True)

@csrf_protect
@permission_required("Cafe.add_cashboxstate")
def new(request):
    "view for adding new states of cashbox machine"   
    if request.method == 'POST':
        form = CashboxStateForm(request.POST)
        if form.is_valid():
            state = form.save(commit=False) # we cannot actually save 
                                            # cause we have to fullfill model before save
            state.accounted_by = request.user
            state.predicted_result = CashboxState.predict_result() 
            form.save()
            
            return HttpResponseRedirect("/")
    else:
        form = CashboxStateForm()
           
    context = {
               "form" : form,
               "CashboxState" : CashboxState, # this is used to display profit and expanses in 
                                              # templates through the static methods
               }

    return direct_to_template(request, "cafe/cash/new.djhtml", context)

@csrf_protect
@permission_required("Cafe.add_cashboxstate")
def view(request):     
    states = CashboxState.objects.all().order_by("-day_of_the_counting")
    
    context = {
               "states":states,
               }
    
    return direct_to_template(request, "cafe/cash/view.djhtml", context)

@csrf_protect
@permission_required("Cafe.delete_cashboxstate")
def manager(request):    
    if request.method == 'POST':
        formset = cashbox_formset(request.POST)
        if formset.is_valid():
            formset.save()

    else: # we assume this is new request
        formset = cashbox_formset(queryset = CashboxState.objects.all())
    
    context = {
               "formset":formset,
               }
    
    return direct_to_template(request, "cafe/cash/manager.djhtml", context)
