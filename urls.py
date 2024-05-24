from django.urls import path
from . import views
urlpatterns=[
    path('sign/Register/',views.Register,name="Register"),
    path('login/',views.login,name="login"),
    path('login/Selling.html',views.Sell,name="Selling"),
    path('login/Buying.html/',views.Buy,name="Buying"),
    path('sign/',views.sign,name="sign"),
    path('log',views.log,name="log"),
    path('login/buy.html',views.showbuy,name="showbuy"),
    path('login/sell.html',views.showsell,name="showsell"),
    path('login/requesthome',views.requesthome,name="requesthome"),
    path('login/sellhome',views.sellhome,name="sellhome")
]