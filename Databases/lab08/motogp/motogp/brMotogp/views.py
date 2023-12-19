from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Luthier
from .models import Guitar
from .models import Artist
from .models import GuitarPic
from .models import Recording

from .models import Team
from .models import Moto
from .models import Driver
from .models import MotoPic
from .models import Drives

def index(request):
    template = loader.get_template('brMotogp/index.html')
    context = {
        'numLuthiers':Luthier.objects.all().count(),
        'numGuitars':Guitar.objects.all().count(),
        'numArtists':Artist.objects.all().count(),
        'numRecordings':Recording.objects.all().count(),
        'numGuitarPics':GuitarPic.objects.all().count(),

        'numTeams':Team.objects.all().count(),
        'numMotos':Moto.objects.all().count(),
        'numDrivers':Driver.objects.all().count(),
        'numDrives':Drives.objects.all().count(),
        'numMotoPics':MotoPic.objects.all().count(),

    }
    return HttpResponse(template.render(context, request))

def luthiers(request):
    template = loader.get_template('brGuitars/luthiers.html')
    items = Luthier.objects.order_by('name')[0:]
    context = {
        'luthiers':items
    }
    return HttpResponse(template.render(context, request))

def luthierDetails(request, luthier_id):
    template = loader.get_template('brGuitars/luthierDetails.html')
    try:
        myLuthier = Luthier.objects.get(pk=luthier_id)
        myLuthierGuitars = Guitar.objects.filter(luthier = luthier_id)
        context = {'luthier' : myLuthier, 'guitars' : myLuthierGuitars}
    except Luthier.DoesNotExist:
        raise Http404("Luthier does not exist")

    return HttpResponse(template.render(context, request))


def artists(request):
    template = loader.get_template('brGuitars/artists.html')
    items = Artist.objects.order_by('name')[0:]
    context = {
        'artists':items
    }
    return HttpResponse(template.render(context, request))

def artistDetails(request, artist_id):
    template = loader.get_template('brGuitars/artistDetails.html')
    try:
        myArtist = Artist.objects.get(pk=artist_id)
        myRecs = Recording.objects.filter(artist = artist_id)
        context = {'artist' : myArtist, 'recs' : myRecs}
    except Artist.DoesNotExist:
        raise Http404("Artist does not exist")

    return HttpResponse(template.render(context, request))

def guitars(request):
    template = loader.get_template('brGuitars/guitars.html')
    items = Guitar.objects.order_by('luthier', 'model')[0:]
    context = {
        'guitars':items
    }
    return HttpResponse(template.render(context, request))

def guitarPics(request):
    template = loader.get_template('brGuitars/guitarPics.html')
    items = GuitarPic.objects.order_by('guitar', 'img')[0:]
    context = {
        'guitarPics':items
    }
    return HttpResponse(template.render(context, request))

def guitarDetails(request, guitar_id):
    template = loader.get_template('brGuitars/guitarDetails.html')
    try:
        guitar = Guitar.objects.get(pk = guitar_id)
        myPics = GuitarPic.objects.filter(guitar = guitar_id)
        context = {'guitar' : guitar, 'pics' : myPics}
    except Guitar.DoesNotExist:
        raise Http404("Guitar does not exist")
    return HttpResponse(template.render(context, request))

def recordings(request):
    template = loader.get_template('brGuitars/recordings.html')
    items = Recording.objects.order_by('artist', 'name')[0:]
    context = {
        'recordings':items
    }
    return HttpResponse(template.render(context, request))

def recordingDetails(request, rec_id):
    template = loader.get_template('brGuitars/recordingDetails.html')
    try:
        rec = Recording.objects.get(id = rec_id)
        context = {'rec' : rec}
    except Recording.DoesNotExist:
        raise Http404("Recording does not exist")
    return HttpResponse(template.render(context, request))


def teams(request):
    template = loader.get_template('brMotogp/teams.html')
    items = Team.objects.order_by('name')[0:]
    context = {
        'teams':items
    }
    return HttpResponse(template.render(context, request))

def teamDetails(request, team_id):
    template = loader.get_template('brMotogp/teamDetails.html')
    try:
        myTeam = Team.objects.get(pk=team_id)
        myTeamMotos = Moto.objects.filter(team = team_id)
        context = {'team' : myTeam, 'motos' : myTeamMotos}
    except Team.DoesNotExist:
        raise Http404("Team does not exist")

    return HttpResponse(template.render(context, request))










    
