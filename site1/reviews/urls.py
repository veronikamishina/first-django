from django.urls import path, include
from .views import *

urlpatterns = [
    path('', reviews_page),
    path('add_comment/', add_comment_page),
    path('thanks/', thanks_page, name="thanks_page"),
]