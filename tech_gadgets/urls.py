from django.urls import path
from .views import single_gadget_view, start_page_view


urlpatterns = [
    path('', start_page_view),
    path('gadget/', single_gadget_view)

]