#!/usr/bin/env python
# coding: utf-8

# ## Lecture 5: Graphics and Animation, Part 1 + Markdown/Latex 

# In[3]:


from pylab import plot,show
y = [ 1.0, 2.4, 1.7, 0.3, 0.6, 1.8]
plot (y)
show()


# In[4]:


from pylab import plot,show
x = [ 0.5, 1.0, 2.0, 4.0, 7.0, 10.0 ] 
y = [ 1.0, 2.4, 1.7, 0.3, 0.6, 1.8] 
plot(x,y)
show()


# In[5]:


from pylab import plot, show 
from numpy import linspace, sin
x =linspace(0,10,100) 
y = sin(x)
plot(x,y)
show()


# In[15]:


from pylab import plot, show 
from numpy import linspace, sin, cos
x =linspace(0,10,100) 
y = cos(x)
plot(x,y)
show()


# In[14]:


from pylab import plot,show 
from math import sin
from numpy import linspace

xpoints = []
ypoints = []
for x in linspace(0,10,100):
    xpoints.append(x) 
    ypoints.append(sin(x))

plot(xpoints,ypoints) 
show()


# In[24]:


from pylab import plot,ylim,show, xlabel, ylabel
from numpy import linspace,sin

x = linspace(0,10,100) 
y = sin(x)

plot(x,y)
ylim(-1.1, 1.1)
xlabel("x axis") 
ylabel("y = sin x") 
show()


# ### Graph styling 

# In[25]:


from pylab import plot,ylim,show, xlabel, ylabel
from numpy import linspace,sin

x = linspace(0,10,100) 
y = sin(x)

plot(x,y, "g--")
ylim(-1.1, 1.1)
xlabel("x axis") 
ylabel("y = sin x") 
show()


# 

# In[27]:


from pylab import plot,ylim,show, xlabel, ylabel
from numpy import linspace,sin

x = linspace(0,10,100) 
y = sin(x)

plot(x,y, "ks")
ylim(-1.1, 1.1)
xlabel("x axis") 
ylabel("y = sin x") 
show()


# In[29]:


from pylab import plot,ylim,xlabel,ylabel,show 
from numpy import linspace,sin,cos

x =linspace(0,10,100) 
y1 = sin(x)
y2 =cos(x) 
plot(x,y1,"k-")
plot (x,y2, "b--")
ylim(-1.1, 1.1)
xlabel("x axis")
ylabel("y =sin x or y cos x") 
show()


# In[2]:


with open("/Users/bayodeibironke/Downloads/cpresources/sunspots.txt") as file:
    data = file.readlines()
    
# Do something with the data
for line in data:
    print(line)


# In[4]:


import matplotlib.pyplot as plt

# Read the data into the script
time = []
sunspots = []
with open("/Users/bayodeibironke/Downloads/cpresources/sunspots.txt") as file:
    for line in file:
        # Split the line into two parts: time and sunspot count
        parts = line.split()
        time.append(float(parts[0]))
        sunspots.append(float(parts[1]))
        
# Make the graph
plt.plot(time, sunspots)
plt.xlabel("Time (in months)")
plt.ylabel("Sunspot count")
plt.title("Sunspots as a function of time")
plt.show()


# In[9]:


import matplotlib.pyplot as plt

# Read the data into the script
time = []
sunspots = []
with open("/Users/bayodeibironke/Downloads/cpresources/sunspots.txt") as file:
    for line in file:
        # Split the line into two parts: time and sunspot count
        parts = line.split()
        time.append(float(parts[0]))
        sunspots.append(float(parts[1]))
        
# Only display the first 1000 data points
time = time[:1000]
sunspots = sunspots[:1000]

# Make the graph
plt.plot(time, sunspots)
plt.xlabel("Time (in months)")
plt.ylabel("Sunspot count")
plt.title("Sunspots as a function of time (first 1000 data points)")
plt.show()


# In[10]:


import matplotlib.pyplot as plt

# Read the data into the script
time = []
sunspots = []
with open("/Users/bayodeibironke/Downloads/cpresources/sunspots.txt") as file:
    for line in file:
        # Split the line into two parts: time and sunspot count
        parts = line.split()
        time.append(float(parts[0]))
        sunspots.append(float(parts[1]))
        
# Truncate the data to the first 1000 data points
time = time[:1000]
sunspots = sunspots[:1000]

# Calculate the running average of the data
r = 5
running_average = []
for i in range(len(sunspots)):
    start = max(0, i - r)
    end = min(len(sunspots), i + r + 1)
    window = sunspots[start:end]
    average = sum(window) / len(window)
    running_average.append(average)

# Make the graph
plt.plot(time, sunspots, label="Original data")
plt.plot(time, running_average, label="Running average")
plt.xlabel("Time (in months)")
plt.ylabel("Sunspot count")
plt.title("Sunspots and Running Average as a Function of Time")
plt.legend()
plt.show()

