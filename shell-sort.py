#!/usr/bin/env python
# coding: utf-8

# In[10]:


def find_replace(arr,n):  # given indices separated by n apart its just replacing the min of the 2 numbers ahead in array
    
    for i in range(len(arr)-1,-1,-1):
        j=i-n
        
       
   
        if j >=0:
            if arr[i]<arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                
    return (arr)
        

def shell_sortify(arr): # ud
    m=int(len(arr)/2)
    for k in range(m,0,-1):
        arr=find_replace(arr,k)
    return(arr)


# In[11]:


find_replace([4,53,2,7,9,8],2)


# In[12]:


find_replace([4,53,2,7,9,8],1)


# In[17]:


def shell_sortify(arr):
    m=int(len(arr)/2)
    for k in range(m,0,-1):
        arr=find_replace(arr,k)
    return(arr)


# In[18]:


shell_sortify([4,53,2,7,9,8])


# In[ ]:




