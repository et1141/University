from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #Luthiers
    path('luthiers', views.luthiers, name='luthiers'),
    path('luthiers/<int:luthier_id>/', views.luthierDetails, name='luthierDetails'),
    path('luthiersguitars',views.luthiersguitars, name='luthiersguitars'),  
    path('uploadLuthier',views.uploadLuthier, name='uploadLuthier'),  

    #artists
    path('artists', views.artists, name='artists'),
    path('artists/<int:artist_id>/', views.artistDetails, name='artistDetails'),

    #recordings
    path('recordings', views.recordings, name='recordings'),
    path('recordings/<int:rec_id>/', views.recordingDetails, name='recordingDetails'),

    #guitars
    path('guitars', views.guitars, name='guitars'),
    path('guitars/<int:guitar_id>/', views.guitarDetails, name='guitarDetails'),

    #guitarPics
    path('guitarPics', views.guitarPics, name='guitarPics'),
]
