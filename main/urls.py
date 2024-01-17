from django.urls import path
from . import views

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('/contact', views.contact, name='contact'),
    path('/news', views.news, name='news'),
    path('/category',views.category,name='category'),
    path('/appeal',views.appeal,name='appeal'),
    # dashboard
    path('dashboard', views.dashboard, name='dashboard'),
    # region
    path('dashboard/region/create', views.create_region, name='create_region'),
    path('dashboard/region/list', views.regions, name='regions'),
    path('dashboard/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', views.region_delete, name='region_delete'),
    # categorys
    path('dashboard/category/create', views.create_category, name='create_category'),
    path('dashboard/category/list', views.categorys, name='categorys'),
    path('dashboard/category/update/<int:id>/', views.category_update, name='category_update'),
    path('dashboard/category/delete/<int:id>/', views.category_delete, name='category_delete'),
    # itms
    path('dashboard/item/create', views.item_create, name='item_create'),
    path('dashboard/item/list', views.items, name='items'),
    path('dashboard/item/update/<int:id>/', views.item_update, name='item_update'),
    path('dashboard/item/delete/<int:id>/', views.item_delete, name='item_delete'),
    #contact
    path('dashbord/appeal/list',views.appeal_dashboard, name='appeal_dashboard')

]