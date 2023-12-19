from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #Luthiers
    path('luthiers', views.luthiers, name='luthiers'),
    path('luthiers/<int:luthier_id>/', views.luthierDetails, name='luthierDetails'),

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

    #Teams
    path('teams', views.teams, name='teams'),
    path('teams/<int:team_id>/', views.teamDetails, name='teamDetails'),

]
