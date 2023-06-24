"""mirbase URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mir1.views import *
from reports.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name = "home"),
    path('Login/', loginpage, name = "login"),
    path('Register/', registerpage, name = "register"),
    path('Benefits/', reportspage, name="reports"),
    path('Reports/water', reportspage, name="water"),
    path('Reports/area', reportspage, name="area"),
    path('Reports/state', reportspage, name="state"),
    path('Reports/sort',reportspage,name="Sort"),
    path('Reports/max',reportspage,name="max"),
    path('Reports/min',reportspage,name="min"),
    path('Reports/visuals.html',reportsvisualspage,name='visuals'),
    path('Benefits/deletebenefits/<str:state_idb>', deletebenefitsrow,name="deletebenefits"),
    path('Benefits/deletebenefits/', deletebenefitsrow,name="deletebenefits"),
    path('Reports/deletewater/<str:state_idw>', deletewaterrow,name="deletewater"),
    path('Reports/deletewater/', deletewaterrow,name="deletewater"),
    path('Reports/deletestate/<str:state_ids>]', deletestaterow,name="deletestate"),
    path('Reports/deletestate/', deletestaterow,name="deletestate"),
    path('Reports/deletearea/<str:state_ida>', deletearearow,name="deletearea"),
    path('Reports/deletearea/', deletearearow,name="deletearea"),
    path('Contacts/', contactspage, name = "contacts"),
    path('Logout/', logoutuser, name = "logout"),
    
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

