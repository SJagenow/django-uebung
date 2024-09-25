from django.urls import path
from .views import start_page_view,single_gadget_int_view, GadgetView ,RedirectToGadgetView, start_page_manufacturers_view ,RedirectToManufacturersView, ManufacturersView, single_manufacturers_int_view


urlpatterns = [
    
    path('start/', start_page_view),
    path('' , RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path('gadget/', GadgetView.as_view()),
    path('gadget/<int:gadget_id>', single_gadget_int_view),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),
    

    path('start/', start_page_manufacturers_view),  
    path('manufacturers/', RedirectToManufacturersView.as_view()), 
    path('manufacturers/list/', ManufacturersView.as_view()), 
    path('manufacturers/<int:manufacturers_id>/', single_manufacturers_int_view),  
    path('manufacturers/<slug:manufacturers_slug>/', ManufacturersView.as_view(), name="manufacturers_slug_url"),  


    ]   

