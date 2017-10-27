
# coding: utf-8

# In[88]:


import httplib2
import requests
import lxml.html
import random
from PIL import Image

def downld_img(url, path):
    h = httplib2.Http('.cache')
    response, content = h.request(url)
    out = open(path+'.webp', 'wb')
    out.write(content)
    out.close()
    im = Image.open(path+".webp").convert("RGB")
    im.save(path+".jpg","jpeg")

def rnd_img_parsed(query):
    url = 'https://yandex.ru/images/search?text='+str(query)
    r = requests.get(url)
    html = lxml.html.fromstring(r.text)
    img = html.xpath("//img/@src")
    return 'http://'+random.choice(img[1:])[2:]

def comp(query, path = 'photos/'):
    x = rnd_img_parsed(query)
    name = path+str(random.randint(10*10,(10**10)*9))
    downld_img(x, name)
    
    return name, True

