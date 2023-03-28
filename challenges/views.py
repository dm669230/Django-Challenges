from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
import os
import webbrowser
from django.template.loader import render_to_string
# Create your views here.


monthly_task = {"january ": "my name is vibhu",
                "february ": "my work is study",
                "march ": "call me web!",
                "april ": "drink more water",
                "may ": "goto Gym Everyday",
                "june ": "make your diet healthy",
                "july ": "make yourself happy",
                "august ": "make others happy",
                "september ": "enjoy your every moment ",
                "october ": "celebrate gandhi jayanti ",
                "novemer ": "make yourself happy",
                "december ": None}


def index(request):
  
    months = list(monthly_task.keys())
    return render(request,"challenges/index.html",{ 
        "months":months
        })


def monthly_challenge_by_number(request, month):
    months = list(monthly_task.keys())
   

    if month > len(months):
        return HttpResponseNotFound("invalid month")
    else:
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
        
def monthly_challenge(request, month):
   
    # try:

    challenge_text = monthly_task[month]
    
    return render(request,"challenges/challenge.html",{
        "text":challenge_text,
        "month_name": month.capitalize()
    })
        
    # except:
    #     response_data=render_to_string("404.html")
    #     return HttpResponseNotFound(response_data)



