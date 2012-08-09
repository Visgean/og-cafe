from django.conf.urls.defaults import *
from django.contrib.auth.views import password_change, password_change_done, login, logout_then_login

urlpatterns = patterns('',
    (r'^login/$', login, {"template_name" : "base.djhtml"}),
    (r'^logout/$', logout_then_login),
    
    (r'^changePass/$', password_change, {"template_name" : "general/changePass.djhtml", 
                                       "post_change_redirect" : "/general/passChanged/"}),
    (r'^passChanged/$', password_change_done, {"template_name" : "general/passChanged.djhtml"}),
    
    
    )