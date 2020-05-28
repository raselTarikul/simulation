from django.urls import path
from .views import CreateSimulation, GetSimulation, GetSimulationActive, GetSimulationReActive

urlpatterns = [
    path('simulations/', CreateSimulation.as_view(),
         name='create-simulation'),
    path('simulations/<int:id>/', GetSimulation.as_view(),
         name='get-simulation'),
    path('simulations/<int:id>/active/', GetSimulationActive.as_view(),
         name='get-simulation-active'),
    path('simulations/<int:id>/reactive/', GetSimulationReActive.as_view(),
         name='get-simulation-reactive'),
]
