
# coding: utf-8

# In[1]:
from PIL import Image
import numpy as np
import random as rnd

#filein = str(input('Input FileIn name (without .format):'))+".bmp"
#fileout = str(input('Input FileOut name (if is bigger than 20000 symb itll be used):'))

def extracting_from_image(img):
    finish = '00000000'
    img_r = img.reshape(-1,3)
    arr = np.array([x for x in range(1,len(img_r))])
    p = 0
    for i in (range(1,len(img_r)-1)):
        arr[i] = int(sum(img_r[i])) % 2
        if arr[i] == 0:
            p += 1
            if p == 8:
                break
        else:
            p = 0
    return arr[1:]

def to_chr(bin_text):
    arr = ''
    for i in range(0,len(bin_text),8):
        arr += str(chr(int(bin_text[i:i+8], 2)))
    return arr

def extract_from_extracted(ex_text, finish = '00000000'):
    x = ''
    for i in ex_text:
        x += str(i)
    #print(x[0:16]) #
    #if not x[0:8] == '00000000':
    #    return False
    for i in range(0,len(x),8):
        if x[i:i+7] == finish:
            x = x[:i]
    return x