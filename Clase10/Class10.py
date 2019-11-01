#!/usr/bin/env python
# coding: utf-8

# In[18]:


import io
import requests
import pandas as pd
from zipfile import ZipFile
r = requests.get('http://www.contextures.com/SampleData.zip')
ZipFile(io.BytesIO(r.content)).extractall()
df = pd.read_excel('SampleData.xlsx', sheet_name='SalesOrders')

df.head()


# In[19]:


# tensorflow
import tensorflow
print('tensoflow: %s' %tensorflow.__version__)
#keras
import keras
print('keras: %s' % keras.__version__)


# In[20]:


import io
import lxml.html as lh
import pandas as pd
url='http://pokemondb.net/pokedex/all'

page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')
[len(T) for T in tr_elements[:12]]


# In[26]:


tr_elements = doc.xpath('//tr')
col=[]
i=0
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    print ('%d:"%s"'%(i,name))
    col.append((name,[]))
[len(C) for (title,C) in col]
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
df.head()


# In[ ]:




