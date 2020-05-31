from django.urls import path

from my_financial_app import views

urlpatterns = [
    path("account/", views.ListAccountView.as_view()),
    path("account/<int:pk>/", views.DetailAccountView.as_view(), name='account-detail'),
    path("card/", views.ListCardView.as_view()),
    path("card/<int:pk>/", views.DetailCardView.as_view(), name="card-detail"),
]
