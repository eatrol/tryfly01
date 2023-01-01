from calendar import c
from django.http.response import HttpResponse
from django.shortcuts import render
import urllib.request as req
from fly.models import *

import json
from django.http import JsonResponse
#from django.core import serializers 

#from bs4 import BeautifulSoup
import requests
#import time
#import pandas as pd




def lucy(request,pk):
    return render(request,"lucy01.html",locals())

# 99乘法表練習
def lucy99(request):
    return render(request,"lucy99.html",locals())

def lucy02(request,pk):  
    return render(request,"lucy02.html",locals())

def main(request):
    students = dblucy.objects.all().order_by('id')  #讀取資料表, 依 id 遞增排序
    number = range(1,9)
    return render(request,"main.html",locals())

def week(request,pk): 
    students = dblucy.objects.filter(type=pk)  #讀取資料表, 依 id 遞增排序
    return render(request,"main.html",locals())

def cutpic(request):
   
    return render(request,"cutpic.html",locals())


def lucyscore(request,pk1,pk2):
    try:
        unit = dblucy.objects.get(name=pk1)
        unit.data = pk2
        unit.save()
        return HttpResponse("score update!")
    except:
        return HttpResponse("Fail!")
    #return render(request,"main.html",locals())

def lucygame(request): 
    return render(request,"lucygame.html",locals())

def lucygame2(request): 
    return render(request,"lucygame2.html",locals())

def lucygame3(request): 
    return render(request,"lucygame3.html",locals())


def lucyvaca(request): 
    return render(request,"lucy_vaca.html",locals())

# eric game
def ericgame(request,pk): 
    if int(pk) <= 99:
        unit = dbtoeic.objects.filter(level=pk)
    else:
        unit = dbtoeic.objects.filter(wrong=pk)

    print("4")
    clist = []
    dlist = []
    elist = []
    isAniTimeDelta2 = 900    # 設定遊戲速度
    for member in unit:
        clist.append(member.name)
        dlist.append(member.chinese)
        elist.append(member.memo)

    return render(request,"ericgame.html",locals())

def ericgame2(request,pk): 
    if int(pk) <= 99:
        unit = dbtoeic.objects.filter(level=pk)
    else:
        unit = dbtoeic.objects.filter(wrong=pk)

    print("4")
    clist = []
    dlist = []
    elist = []
    isAniTimeDelta2 = 500    # 設定遊戲速度
    for member in unit:
        clist.append(member.name)
        dlist.append(member.chinese)
        elist.append(member.memo)

    return render(request,"ericgame2.html",locals())
    

def ericlearn(request,pk): 
    unit = dbtoeic.objects.filter(wrong=pk)
    clist = []
    dlist = []
    isAniTimeDelta2 = 200   # 設定遊戲速度

    for member in unit:
        clist.append(member.name)
        dlist.append(member.chinese)
    
    return render(request,"ericgame.html",locals())

def ericstudy(request,pk): 
    if int(pk) <= 99:
        unit = dbtoeic.objects.filter(level=pk)
    else:
        unit = dbtoeic.objects.filter(wrong=pk)
    
    clist = []
    dlist = []
    elist = []
    isAniTimeDelta2 = 9999    # 設定遊戲速度
    for member in unit:
        clist.append(member.name)
        dlist.append(member.chinese)
        elist.append(member.memo)

    return render(request,"ericstudy.html",locals())

def ericexcel(request): 
    #dbtoeic.objects.all().delete()
    return render(request,"ericexcel.html",locals())


# 將excel資料寫入資料的方式
def readericexcel(request):
    pk = request.POST['pyjson']

    clist = json.loads(pk)
    #print(clist[0]["Description"])
    for member in clist:
        pk = member["Item"]
        try:
            unit = dbtoeic.objects.get(item=pk)
            unit.name = member["name"]
            unit.chinese = member["chinese"]

            try:
                unit.memo = member["memo"] 
            except:
                unit.memo = ""
            
            try:
                unit.relate = member["relate"]   
            except:
                unit.relate = ""
            
            try:
                unit.level = member["level"]
            except:
                unit.level = ""
                
            try:
                unit.toune = member["toune"]
            except:
                unit.toune = ""

            try:
                unit.sound = member["sound"]
            except:
                unit.sound = ""       

            try:
                unit.wrong = member["wrong"]
            except:
                print("")        
            

            unit.save()
            print("data update !!")
        except:
            item = member["Item"]
            name = member["name"]
            chinese = member["chinese"]
            level = member["level"]

            try:
                memo = member["memo"]
            except:
                memo = ""
            
            try:
                relate = member["relate"]
            except:
                relate = ""

            try:
                sound = member["sound"]
            except:
                sound = ""

            unit = dbtoeic.objects.create(item=item, name=name, chinese=chinese, level=level, memo=memo, relate=relate, sound=sound)
            unit.save()
            print("add"+pk)

    # with req.urlopen(src) as response:
    #      data = json.load(response)
        
    #clist = data["result"]["results"]
    return JsonResponse(clist, safe=False,json_dumps_params={'ensure_ascii':False})



def deleteall(request): 
    dbtoeic.objects.all().delete()
    return render(request,"ericexcel.html",locals())


from django.core import serializers 
def jsontoeic(request): 
    unit = dbtoeic.objects.all().order_by('id')
    data = serializers.serialize('json',unit)
 
    return JsonResponse(data, safe=False,json_dumps_params={'ensure_ascii':False})
    #return JsonResponse({'data':data})
