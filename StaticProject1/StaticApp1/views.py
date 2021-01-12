from django.shortcuts import render

# Create your views here.
def view(request):
    myname='dimpana'
    favplayer='dhoni'
    favanimal='lion'
    favsub='python'
    d={'name':myname,'player':favplayer,'animal':favanimal,'sub':favsub}
    return render(request,'1.html',d)
