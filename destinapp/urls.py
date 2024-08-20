from django.urls import path
from .views import *
from .import views
urlpatterns=[
    path('create/',DestinCreateView.as_view(),name='create-destination'),
    path('details/<int:pk>/',DestinDetailView.as_view(),name='details-destination'),
    path('update/<int:pk>/',DestinUpdateView.as_view(),name='update-destination'),
    path('delete/<int:pk>/',DestinDeleteView.as_view(),name='delete-destination'),
    path('search/<str:PlaceName>/',DestinSearch.as_view(),name='search-destination'),
    path('create_destin/',views.create_destin,name='create_destin'),
    path('fetch_tour/<int:id>/',views.fetch_tour,name='fetch_tour'),
    path('update_tour/<str:pk>/',views.update_tour,name='update_tour'),
    path('delete_tour/<int:id>/',views.delete_tour,name='delete_tour'),
    path('search_tour/',views.search_tour,name='search'),
    path('packages/',views.packages),
    path('',views.indexs)
]