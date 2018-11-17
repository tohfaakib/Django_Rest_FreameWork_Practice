from django.urls import path


from . import views


urlpatterns = [
    path('', views.QuoteCategoryAPIView.as_view()),
    path('quotes/', views.QuoteAPIView.as_view()),
    path('quotes/<int:pk>/', views.QuoteAPIDetailView.as_view()),
    path('quotes/new/', views.QuoteAPINewView.as_view()),

]
