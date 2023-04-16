from django.urls import path
import views

app_name = 'shope'

urlpatterns = [
    path('', views.allProdCat, name='allProdCat'),
    path('<slug:c_slug>/', views.allProdCat, name='products_by_category'),
]
