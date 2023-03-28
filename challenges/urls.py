# i created this file in my appdata-> challenges
from django.urls import path
from .import views

urlpatterns = [
    # /challenge/january/->
    # <month> -> this is dynamicplace holder and monthly_challenges indicate the function under views file
    path('<int:month>', views.monthly_challenge_by_number,),
    path('<str:month>', views.monthly_challenge,name='month-challenge'),
    path('',views.index, name='index'),
  
   
    
    


]
# here we are making urlConfig
# so for connecting Challenges appdata and main Monthely_challenges we should go to the monthly_challenges and add this url path in that url(in the Monthely_Challenges)
