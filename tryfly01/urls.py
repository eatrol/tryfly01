"""tryfly01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fly import views
from fly import views_lucy


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.homePageView, name="home"),

    # 從 views_lucy 載入相關程序
    path('lucy/<str:pk>',views_lucy.lucy),
    path('lucy02/<str:pk>',views_lucy.lucy02),
    path('main/',views_lucy.main),
    path('main/<str:pk>',views_lucy.week),
    path('lucyscore/<str:pk1>/<str:pk2>',views_lucy.lucyscore),
    path('lucygame/',views_lucy.lucygame),
    path('lucygame2/',views_lucy.lucygame2),
    path('lucygame3/',views_lucy.lucygame3),
    path('lucyvaca/',views_lucy.lucyvaca),
    path('cutpic/',views_lucy.cutpic),
    path('',views_lucy.main),

    path('ericgame/<str:pk>',views_lucy.ericgame2),      # 依照多益關卡 (先改成練習版)
    path('ericgame2/<str:pk>',views_lucy.ericgame2),      # 依照多益關卡
    #path('ericwrong/<str:pk>',views_lucy.ericwrong),    # 自己設定group, 經常錯字
    path('ericlearn/<str:pk>',views_lucy.ericlearn),    # 學習板,速度會變快
    path('ericstudy/<str:pk>',views_lucy.ericstudy),    # 學習板,速度會變快
    path('ericexcel/',views_lucy.ericexcel),
    path('readericexcel/',views_lucy.readericexcel),
    path('deleteall/',views_lucy.deleteall),
    path('jsontoeic/',views_lucy.jsontoeic),
    
]






