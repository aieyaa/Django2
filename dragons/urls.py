from django.urls import path
from .views import DragonViewSet, liste_dragons
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'dragons', DragonViewSet)

urlpatterns = [
    path("", liste_dragons, name="liste_dragons"),

]
