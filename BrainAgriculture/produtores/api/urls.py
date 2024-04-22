from django.urls import path
from produtores.api.view import ProdutorViewesets, DashboardTotalsViewesets

urlpatterns = [
    path('produtores/', ProdutorViewesets.as_view(), name='produtores'),
    path('produtores/<int:pk>/', ProdutorViewesets.as_view(), name='produtor-detail'),
    path('dashboard-totals/', DashboardTotalsViewesets.as_view(), name='dashboard_totals'),
]
