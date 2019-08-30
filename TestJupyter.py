#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense


# In[19]:


#cargamos las 4 combinaciones de las compuertas XOR
training_data = np.array([[0,0],[0,1],[1,0],[1,1]], "float32")

# y estos son los resultados que se obtienen, en el mismo orden
target_data = np.array([[0],[1],[1],[0]], "float32")


# In[20]:


model = Sequential()
model.add(Dense(16, input_dim=2, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# In[21]:


model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['binary_accuracy'])


# In[22]:


model.fit(training_data, target_data, epochs=1000)


# In[24]:


#evaluamos el modeloab
scores = model.evaluate(training_data, target_data)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


# In[25]:


print (model.predict(training_data).round())


# In[ ]:




