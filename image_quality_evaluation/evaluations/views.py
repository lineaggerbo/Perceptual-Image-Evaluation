from django.http import HttpResponse
from .models import Image
from .models import Observer
from django.template import loader
from datetime import datetime


def index(request):
	template = loader.get_template('evaluations/index.html')
	return HttpResponse(template.render(request))

def scene(request, scene_id):
	scene_reference_image = Image.objects.get(scene=scene_id, reference=True)
	scene_image_list = Image.objects.filter(scene=scene_id, reference=False)
	scene_letter_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
	num_scenes = Image.objects.values_list('scene',flat = True).order_by('-scene')[:1][0]
	template = loader.get_template('evaluations/scene.html')
	next_scene_id = int(scene_id)+1

	if(int(scene_id) == num_scenes):
		last_scene = True
	else:
		last_scene = False

	context = {	'scene_reference_image': scene_reference_image,
				'scene_image_list': scene_image_list,
				'scene_letter_list': scene_letter_list,
				'num_scenes': num_scenes, 
				'scene_id': scene_id ,
				'next_scene_id': next_scene_id,
				'last_scene': last_scene,}
	return HttpResponse(template.render(context, request))

def end(request):
	template = loader.get_template('evaluations/end.html')
	return HttpResponse(template.render(request))