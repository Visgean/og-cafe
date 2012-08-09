from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^$', "Lisculea.Cafe.views.orders.new"),
    
    (r'^order/new$', "Lisculea.Cafe.views.orders.new"),
    (r'^order/expand/(?P<order_id>\d*)$', "Lisculea.Cafe.views.orders.expand"),
    (r'^order/unpaid$', "Lisculea.Cafe.views.orders.unpaid"),
    (r'^order/today$', "Lisculea.Cafe.views.orders.today"),
    
    (r'^products/new$', "Lisculea.Cafe.views.products.new"),
    (r'^products/manage$', "Lisculea.Cafe.views.products.manage"),
    
    (r'^cashbox/state$', "Lisculea.Cafe.views.cash.new"),
    (r'^cashbox/view$', "Lisculea.Cafe.views.cash.view"),
    (r'^cashbox/manager$', "Lisculea.Cafe.views.cash.manager"),
    
    (r'^expanse/new$', "Lisculea.Cafe.views.expense.new"),
    (r'^expanse/view$', "Lisculea.Cafe.views.expense.view"),
    
)
