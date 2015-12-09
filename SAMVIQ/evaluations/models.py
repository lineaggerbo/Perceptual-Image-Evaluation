from django.db import models

# Create your models here.
class Observer(models.Model):
	name = models.CharField(max_length = 100)
	dateTime = models.DateTimeField('date created')

	def __unicode__(self):
		return 'Observer: ' + str(self.name)

class Image(models.Model):
	scene = models.IntegerField(default = 0)
	image_file = models.ImageField(default = 'Null', upload_to = 'images')
	reference = models.BooleanField(default = False)

	def __str__(self):
		return self.image_file

class Rating(models.Model):
	observer = models.ForeignKey(Observer, on_delete = models.CASCADE)
	image = models.ForeignKey(Image, on_delete = models.CASCADE)
	dateTime = models.DateTimeField('date rated')
	rating = models.IntegerField(default = 0)
