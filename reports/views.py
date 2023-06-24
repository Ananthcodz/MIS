from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from .models import benefits,water,area,state
from .forms import addbenefit
from django.urls import reverse,resolve

# Create your views here.


def reportspage(request):
    if request.method =="POST":
        Data = request.POST
        
        if resolve(request.path_info).url_name == 'water':
            w = water(state_idw=Data['State ID'],state_namew = Data['State Name'],source = Data['Source'],litres_prov = Data['Litres provided (Tmcft)'],litres_benefit = Data['Litres Benefited (Tmcft)'])
            w.save()
            wobj = water.objects.all()
            return render(request,"reports.html",{'Dict2':wobj})

        elif resolve(request.path_info).url_name == 'area':
            a = area(state_ida=Data['State ID'],state_namea = Data['State Name'],area_target = Data['Area Target (Ha)'],area_saved = Data['Area saved (Ha)'])
            a.save()
            aobj = area.objects.all()
            return render(request,"reports.html",{'Dict3':aobj})

        elif resolve(request.path_info).url_name == 'state':
            s = state(state_ids=Data['State ID'],state_names = Data['State Name'],cum_budget = Data['Cum-Budget (Cr)'],achieved = Data['Achieved (Cr)'])
            s.save()
            sobj = state.objects.all()
            return render(request,"reports.html",{'Dict4':sobj})
        
        

        else:
            b = benefits(state_idb=Data['stateid'],state_nameb = Data['statename'],target = Data['Target'],profit_amt = Data['Profit amount'],)
            b.save() 
            obj = benefits.objects.all()
            return render(request,"reports.html",{'Dict1':obj})
    elif request.method =="GET":
        return render(request,"reports.html")

def deletebenefitsrow(request, state_idb=None):
        objd = benefits.objects.get(state_idb=state_idb)
        objd.delete()
        return HttpResponseRedirect(reverse("reports"))

def deletearearow(request, state_ida=None):
        objz = area.objects.get(state_ida = state_ida)
        objz.delete()
        return HttpResponseRedirect(reverse("reports"))

def deletestaterow(request, state_ids=None):
        objz = state.objects.get(state_ids = state_ids)
        objz.delete()
        return HttpResponseRedirect(reverse("reports"))

def deletewaterrow(request, state_idw=None):
        objz = water.objects.get(state_idw = state_idw)
        objz.delete()
        return HttpResponseRedirect(reverse("reports"))

def reportsvisualspage(request):
    return render(request,"visuals.html")