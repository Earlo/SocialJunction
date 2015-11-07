from django.db import models

# Create your models here.

class Project( models.Model ):
    name = models.CharField( max_length = 64 )
    description = models.CharField( max_length = 2000 )
    pub_date = models.DateTimeField( 'date published' )

    def view(self):
        return HttpResponse( description )



class Event( models.Model ):
    description = models.CharField( max_length = 2000 )
    pub_date = models.DateTimeField( 'Date of happening' )
    event = models.ForeignKey( Project )

    
#    def add_date()
 #   def was_published_recently(self):
  #      return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
