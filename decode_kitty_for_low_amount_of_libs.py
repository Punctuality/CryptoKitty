
# coding: utf-8

# In[1]:


from PIL import Image
import numpy as np
import random as rnd

filein = str(input('Input FileIn name (without .format):'))+".bmp"

def extracting_from_image(img):
    img_r = img.reshape(-1,3)
    arr = np.array([x for x in range(1,len(img_r))])
    for i in (range(1,len(img_r)-1)):
        arr[i] = int(sum(img_r[i])) % 2
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
    for i in range(0,len(x),8):
        if x[i:i+7] == finish:
            x = x[:i]
    return x

ex_out = extracting_from_image(np.array(Image.open(filein)))
out = extract_from_extracted(ex_out, '00000000'[:-1])

res = to_chr(out)

print(res)

