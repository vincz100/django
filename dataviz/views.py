from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.template.response import TemplateResponse
from django.http import HttpResponse, JsonResponse

from datetime import datetime
import pygal

from dataviz.models import Statistiques
# from dataviz.chart import LineChart

# page d'accueil "acceuil" avec la fonction render qui prend 3 arguments en paramètre : 
# la requête HTTP initiale
# le template home.html 
# un dictionnaire reprenant les variables qui seront accessibles dans le template

# class IndexView(TemplateView):
# 	template_name = 'home.html'

# 	def get_context_data(self, **kwargs):
# 		context = super(IndexView, self).get_context_data(**kwargs)

# 		chart1 = LineChart(
# 			height=600,
#             width=800,
#             explicit_size=True
# 		)

# 		context['chart1'] = chart1.generate()
# 		return context

def accueil(request):
	filtre = Statistiques.objects.values_list("d68_pop", "d75_pop", "d82_pop", "d90_pop", "d99_pop", "p10_pop", "p15_pop").filter(codgeo='39518')
	data = [el for el in filtre[0]]

	line_chart = pygal.Line(width=500, height=400, explicit_size=True)
	line_chart.title = 'Evolution de la population depuis 1968'
	line_chart.add("population", data)

	return HttpResponse(line_chart.render())
	
	# data = Statistiques.objects.all()
	# return TemplateResponse(request, "templates/home.html", { "data": data })
	# return render(request, "templates/home.html", {"date": datetime.now()})

# page index avec la méthode HttpResponse(text) qui prend comme paramètre une chaîne de caractères et renvoie le HTML au navigateur. 

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'home.html', {})

def get_data(request, *args, **kwargs):
	data = (Statistiques.objects.values("d68_pop", "d75_pop", "d82_pop", "d90_pop", "d99_pop", "p10_pop", "p15_pop").filter(codgeo='39538'))[0]
	return JsonResponse(data)

def index2(request):
    return HttpResponse("""
        <h1>SOCIO DEMO</h1>
        """)

def index3(request):
    return HttpResponse("""
        <h1>ECO EMPLOI<h1>
        """)

