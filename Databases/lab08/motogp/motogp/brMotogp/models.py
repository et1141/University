from django.db import models

class Luthier(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=200, null=True, blank=True)
    birth = models.IntegerField(null=True, blank=True)
    death = models.IntegerField(null=True, blank=True)
    pic = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name
    def isAlive(self):
        return death==False

class Guitar(models.Model):
    luthier = models.ForeignKey(Luthier, on_delete=models.CASCADE)
    model = models.CharField(max_length = 200, null=False, blank=False)
    year = models.IntegerField(null=True, blank=True)
    top = models.CharField(max_length=200, null=True, blank=True)
    bottom = models.CharField(max_length=200, null=True, blank=True)
    sides = models.CharField(max_length=200, null=True, blank=True)
    neck = models.CharField(max_length=200, null=True, blank=True)
    fretboard = models.CharField(max_length=200, null=True, blank=True)
    sadle = models.CharField(max_length=200, null=True, blank=True)
    tuningMachines = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.luthier.name+"-"+self.model

class GuitarPic(models.Model):
    img = models.URLField(max_length=500, null=False, blank=False)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    def __str__(self):
        return self.img

class Artist(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=200, null=True, blank=True)
    birth = models.IntegerField(null=True, blank=True)
    death = models.IntegerField(null=True, blank=True)
    pic = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name
    def isAlive(self):
        return death==False

class Recording(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    year = models.IntegerField(null=True, blank=True)
    composer = models.CharField(max_length=200)
    arrangement = models.CharField(max_length=200, null=True, blank=True)
    audio = models.URLField(max_length=500, null=False, blank=False)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=200, null=True, blank=True)
    pic = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name

class Moto(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    model = models.CharField(max_length = 200, null=False, blank=False)
    brand = models.CharField(max_length = 200, null=False, blank=False)
    size = models.IntegerField(null=True, blank=True)
    cc = models.IntegerField(null=True, blank=True)
    hp = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.team.name+"-"+self.model

class MotoPic(models.Model):
    img = models.URLField(max_length=500, null=False, blank=False)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE)
    def __str__(self):
        return self.img

class Driver(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    country = models.CharField(max_length=200, null=True, blank=True)
    birth = models.IntegerField(null=True, blank=True)
    death = models.IntegerField(null=True, blank=True)
    pic = models.URLField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.name
    def isAlive(self):
        return death==False

class Drives(models.Model):
    dateSTART = models.IntegerField(null=True, blank=True)
    dateEND = models.IntegerField(null=True, blank=True)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

