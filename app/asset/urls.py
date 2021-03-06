"""AutoCmdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from asset import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),

    # --- homepage ---

    url(r'^$', views.home_redirect),

    # --- asset ---
    url(r'^asset/$', views.asset, name="asset"),
    url(r'^asset/index$', views.asset_index, name="asset_index"),
    url(r'^asset/add', views.asset_add, name="asset_add"),
    url(r'^asset/edit/(?P<pk>\d+)', views.asset_edit, name="asset_edit"),
    url(r'^asset/input', views.asset_input, name="asset_input"),
    url(r'^asset/output', views.asset_output, name="asset_output"),
    url(r'^asset/busunit', views.asset_busunit, name="asset_busunit"),

    # --- asset_repair ---
    url(r'^asset/repair$', views.asset_repair, name='asset_repair'),
    url(r'^asset/repair/add$', views.asset_repair_add, name='asset_repair_add'),
    url(r'^asset/repair/detail/(?P<pk>\d+)', views.asset_repair_detail, name="asset_repair_detail"),

    url(r'^asset_file$', views.asset_file, name='asset_file'),

    # --- asset_repair_detail ---
    url(r'^asset_repair_detail/add/$', views.asset_repair_detail_add, name="asset_repair_detail_add"),
    url(r'^asset_repair_detail/edit/$', views.asset_repair_detail_edit, name="asset_repair_detail_edit"),
    url(r'^asset_repair_detail/del/$', views.asset_repair_detail_del, name="asset_repair_detail_del"),

    # --- Asset_relation_Assets

    url(r'^asset/ara$', views.ara, name="ara_index"),


    # --- department ---
    url(r'^department/$', views.department, name="department"),
    url(r'^department/input', views.department_input, name="department_input"),
    url(r'^department/output', views.department_output, name="department_output"),

    # --- category ---
    url(r'^category/$', views.category, name="category"),
    url(r'^category/input', views.category_input, name="category_input"),
    url(r'^category/output', views.category_output, name="category_output"),

    # --- user ---
    url(r'^user/$', views.user, name="user"),
    url(r'^user/(\d+)', views.user_info, name="user_info"),
    url(r'^user/add', views.user_add, name="user_add"),
    url(r'^user/edit/(?P<pk>\d+)/$', views.user_edit, name="user_edit"),
    url(r'^user/input', views.user_input, name="user_input"),
    url(r'^user/output', views.user_output, name="user_output"),

    # --- userprofile ---
    url(r'^userprofile/$', views.userprofile, name="userprofile"),

    # --- bus ---
    url(r'^busunit/$', views.busunit, name="busunit"),

    # --- news ---
    url(r'^news/index$', views.news, name="news"),
    url(r'^news/add$', views.news_add, name="news_add"),
    url(r'^news/edit/(?P<pk>\d+)/$', views.news_edit, name="news_edit"),
    url(r'^news/(?P<pk>\d+)/$', views.news_info, name="news_info"),






    # test

    url(r'^test1/', views.test1, name="test1"),
    url(r'^test2/', views.test2, name="test2"),
    url(r'^user_permissions/', views.user_permission, name="user_permissions"),
    url(r'^formatdata/', views.formatdata, name="formatdata"),

]
