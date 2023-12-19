from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import Luthier
from .models import Guitar
from .models import Artist
from .models import GuitarPic
from .models import Recording

admin.site.register(Luthier)
admin.site.register(Guitar)
admin.site.register(Artist)
admin.site.register(GuitarPic)
admin.site.register(Recording)
