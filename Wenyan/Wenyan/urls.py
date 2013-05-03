from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ArticalManager.views.goHome', name='home'),
    #url('r'^&', 'ArticalManager.views.showArtical'),
    # url(r'^Wenyan/', include('Wenyan.Wenyan.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^edit_artical/', 'ArticalManager.views.editArtical'),
    url(r'^list_artical/', 'ArticalManager.views.listArtical'),
    url(r'^show_artical/(\d+)$', 'ArticalManager.views.showArtical', name='show_artical'),
)
