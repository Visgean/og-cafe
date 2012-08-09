from django.conf.urls.defaults import url, patterns, include
from django.contrib import admin
from django.contrib.auth.views import password_change, password_change_done, login, logout_then_login

from ogcafe import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    
    
	(r'^login/$', login, {"template_name" : "base.djhtml"}),
	(r'^logout/$', logout_then_login),
	(r'^change_pass/$', password_change, {"template_name" : "general/changePass.djhtml",
									   "post_change_redirect" : "/general/pass_changed/"}),
	(r'^pass_changed/$', password_change_done, {"template_name" : "general/passChanged.djhtml"}),

   
   )

urlpatterns += patterns('Lisculea.Cafe.views',

	url(r'^$', view="orders.new", name="new_order"),
	
	url(r'^order/new$', view="orders.new"),
	url(r'^order/expand/(?P<order_id>\d*)$', view="orders.expand", name="order_expand"),
	url(r'^order/unpaid$', view="orders.unpaid"),
	url(r'^order/today$', view="orders.today"),
	
	url(r'^products/new$', view="products.new"),
	url(r'^products/manage$', view="products.manage"),
	
	url(r'^cashbox/state$', view="cash.new"),
	url(r'^cashbox/view$', view="cash.view"),
	url(r'^cashbox/manager$', view="cash.manager"),
	
	url(r'^expanse/new$', view="expense.new"),
	url(r'^expanse/view$', view="expense.view"),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
