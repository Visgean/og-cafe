from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.contrib.auth.views import password_change, password_change_done, login, logout_then_login

from cafeapp import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    
	(r'^general/login/$', login, {"template_name" : "base.djhtml"}),
	(r'^general/logout/$', logout_then_login),
	(r'^general/change_pass/$', password_change, {"template_name" : "general/changePass.djhtml",
									   "post_change_redirect" : "/cafe/general/pass_changed/"}),
	(r'^general/pass_changed/$', password_change_done, {"template_name" : "general/passChanged.djhtml"}),

   
   )

urlpatterns += patterns('cafeapp.cafe.views',

	url(r'^$', view="orders.new", name="new_order"),
	
	url(r'^order/new$', view="orders.new"),
	url(r'^order/expand/(?P<order_id>\d*)$', view="orders.expand", name="order_expand"),
	url(r'^order/unpaid$', view="orders.unpaid", name="unpaid"),
	url(r'^order/today$', view="orders.today", name="today"),
	
	url(r'^products/new$', view="products.new", name="new_product"),
	url(r'^products/manage$', view="products.manage", name="manage_product"),
	
	url(r'^cashbox/state$', view="cash.new", name="new_cash"),
	url(r'^cashbox/view$', view="cash.view", name="view_cash"),
	url(r'^cashbox/manager$', view="cash.manager", name="manage_cash"),
	
	url(r'^expanse/new$', view="expense.new", name="new_expense"),
	url(r'^expanse/view$', view="expense.view", name="view_expense"),
)

urlpatterns += patterns('',
    (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
