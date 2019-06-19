from django.shortcuts import render
from django.http import HttpResponse
from xml.dom.minidom import parse,Node
import xml.dom.minidom
import  wget
import os


def home(request):
    return render(request,"main.html")
    
def bbc(request):
    url = "http://feeds.bbci.co.uk/news/world/rss.xml"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\bbc.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\bbc.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\bbc.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'bbc.html',context=context)
def washington(request):
    url = "https://www.washingtontimes.com/rss/headlines/news/national/"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\washing.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\washing.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\washing.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'washing.html',context=context)

def reuters(request):
    url = "http://feeds.reuters.com/Reuters/worldNews"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\reuters.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\reuters.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\reuters.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,"reuters.html",context=context)

def aljazeera(request):
    url = "https://www.aljazeera.com/xml/rss/all.xml"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\aljazeera.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\aljazeera.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\aljazeera.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'aljazeera.html',context=context)

def cnn(request):
    url = "http://rss.cnn.com/rss/edition.rss"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\cnn.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\cnn.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\cnn.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'cnn.html',context=context)
def dw(request):
    url = "http://rss.dw.com/rdf/rss-en-all"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\dw.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\dw.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\dw.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'dw.html',context=context)
def espn(request):
    url = "https://www.espn.com/espn/rss/news"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\espn.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\espn.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\espn.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'espn.html',context=context)

def greatgoals(request):
    url = "https://www.101greatgoals.com/feed/ "
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\great-goals.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\great-goals.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\great-goals.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'great-goals.html',context=context)
def skysports(request):
    url = "https://www.espn.com/espn/rss/news"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\sky-sports.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\sky-sports.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\sky-sports.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'sky-sports.html',context=context)

def soccernews(request):
    url = "https://www.espn.com/espn/rss/news"
    default_path = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\soccernews.xml"
    if os.path.exists(default_path):
        os.remove(default_path)
    else:
        print("FileNotPresentError")
    wget.download(url,"C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\soccernews.xml")
    
    location = "C:\\Users\\dell\\Desktop\\rssfeeds\\feeds\\xmls\\soccernews.xml"
    data_source = open(location)
    dom1  = parse(data_source)
    r= dom1.documentElement
    tv = r.getElementsByTagName("item")
    d = dict()
    
    
    
    for items in tv:
        title = items.getElementsByTagName('title')[0]
        w  = title.childNodes[0].data
        description = items.getElementsByTagName('description')[0]
        k  = description.childNodes[0].data
        link = items.getElementsByTagName('link')[0]
        web_link  = link.childNodes[0].data
        d[w] = [k,web_link]
    context  = {
        "title" : d.items()
        # "link": b.items()
        }
    return render(request,'sky-sports.html',context=context)