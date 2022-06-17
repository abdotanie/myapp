from importlib.resources import path
from django.http import JsonResponse
from django.shortcuts import render
from.A_star import main,add,addHeuristics
# Create your views here.
def Home(request):
   if 'add_con' in request.GET:
      nan = request.GET.get('city1')
      nan2 = request.GET.get('city2')
      connect=request.GET.get('connect')
      add(nan,nan2,connect)
      print(nan,nan2,connect)
   if 'add_inf' in request.GET:
          c = request.GET.get('city_inf')
          n = request.GET.get('Inference')
          addHeuristics(c,n)
          print(c,n)
   if 'showbtn' in request.GET:
          start = request.GET.get('start')
          end= request.GET.get('end')
          print(start,end)
          
          pp=main(start,end)
          print(pp)
          return JsonResponse(
             {
             'result': pp,
             }
               )                 
   return render(request,'home/Home.html')