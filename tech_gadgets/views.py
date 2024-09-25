
from django.shortcuts import redirect, render
from django.http import  JsonResponse ,HttpResponseNotFound ,Http404 
import json
from django.utils.text import slugify
from django.urls import reverse
from .dummy_data import gadgets , manufacturers
#Create your views here.
# wearabletracker-x10
from django.views import View
from django.views.generic import View
from django.views.generic.base import RedirectView

def start_page_view(request):
    return render(request, 'tech_gadgets/test.html', {'gadget_liest': gadgets} )



class RedirectToGadgetView(RedirectView): 
    pattern_name ="gadget_slug_url"


    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(gadgets[kwargs.get("gadget_id", 0)]["name"])
        new_kwargs ={"gadget_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)

def single_gadget_int_view(request, gadget_id):
    if len(gadgets) > gadget_id:
      new_slug = slugify(gadgets[gadget_id]["name"]) 
      new_url = reverse("gadget_slug_url", args=[new_slug])
      return redirect(new_url)
    return HttpResponseNotFound("not found by me")


class GadgetView(View):
     
     def get(self, request, gadget_slug):
         gadget_match = None
         for gadget in gadgets:
           if slugify(gadget["name"]) == gadget_slug:
              gadget_match = gadget
             

         if gadget_match:
          return JsonResponse(gadget_match)
         raise Http404("Gadget not found") 
         
     def post(self, request, *args, **kwargs):
        try:
             data = json.loads(request.body)
             print(f"recived data: {data["test"]}")
             return JsonResponse({"response": "Das war was"})
        except:
             return JsonResponse({"response": "Das war wohl nix"})





def start_page_manufacturers_view(request):
    return render(request, 'tech_gadgets/test2.html', {'manufacturers_list': manufacturers})


class RedirectToManufacturersView(RedirectView): 
    pattern_name = "manufacturers_slug_url"

    def get_redirect_url(self, *args, **kwargs):
        slug = slugify(manufacturers[kwargs.get("manufacturers_id", 0)]["name"])
        new_kwargs = {"manufacturers_slug": slug}
        return super().get_redirect_url(*args, **new_kwargs)

def single_manufacturers_int_view(request, manufacturers_id):
    if len(manufacturers) > manufacturers_id:
        new_slug = slugify(manufacturers[manufacturers_id]["name"])
        new_url = reverse("manufacturers_slug_url", args=[new_slug])
        return redirect(new_url)
    return HttpResponseNotFound("Manufacturer not found")


class ManufacturersView(View):
     
    def get(self, request, manufacturers_slug, *args, **kwargs):
        manufacturer_match = next((manufacturer for manufacturer in manufacturers if slugify(manufacturer["name"]) == manufacturers_slug), None)      

        if manufacturer_match:
            return JsonResponse(manufacturer_match)
        raise Http404("Manufacturer not found") 
         
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            return JsonResponse({"response": "Data received successfully"})
        except json.JSONDecodeError:
            return JsonResponse({"response": "Invalid JSON data"})


    #ZU der next schleife 
# 4. Zusammengefasst
# Also, der gesamte Code macht Folgendes:
# Er durchläuft die Liste der Hersteller.
# Er schaut für jeden Hersteller, ob sein "slug" mit dem gegebenen manufacturers_slug übereinstimmt.
# Wenn er einen passenden Hersteller findet, gibt next() diesen zurück und speichert ihn in manufacturer_match.
# Wenn es keinen passenden Hersteller gibt, wird ein Fehler geworfen (das kannst du durch einen Standardwert oder einen try-except-Block abfangen).