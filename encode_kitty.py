
# coding: utf-8

# In[103]:


from PIL import Image
import numpy as np
import random as rnd

filein = str(input('Input FileIn path:'))

def transforming_the_image(text, img):
    img_r = img.reshape(-1,3)
    im = img_r
    #print(text+'00100011')
    for i in range(1,len(text+'00000000')):
        #print(int((text+'00100011')[i-1]),int(sum(img_r[i])) % 2, i-1)
        if int((text+'00000000')[i-1]) == int(sum(img_r[i])) % 2:
            continue
        else:
            img_r[i][rnd.randint(0,2)] += 1
    return img_r.reshape(img.shape)

def append(text,k = 8):
    if len(text) != 8:
        x = ""
        for i in range(8-len(text)):
            x += '0'
        text = x+text
    return text

def to_bin(text): #Результат: 1100001 1100010 1100011 
    res = ""
    for i in text:
        res += append(bin(ord(i))[2:])
    return res

Img = np.array(Image.open(filein))#mpimg.imread(filein, format = "jpg")
print('You could write ',str(len(Img.reshape(-1,1))/8/1024)+' kb of text.')
print('Amount of symbols: ', str(int(len(Img.reshape(-1,1))/8/2)))
fileout = str(input('Input FileOut name (without .format):'))+'.bmp'
s = str(input("Text to crypt into kitty:"))
to_crypt = to_bin(s)
print(to_crypt)
Img_write = transforming_the_image(to_crypt, Img)
imm = Image.fromarray(Img_write)
imm.save(fileout)
print("Jobs Finished.")

