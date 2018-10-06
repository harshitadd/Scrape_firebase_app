
# coding: utf-8

# In[52]:


import requests 
page = requests.get('https://www.ndtv.com/')
from bs4 import BeautifulSoup as BS
soup = BS(page.content, 'html.parser')
list = soup.find_all('a',{'class' : 'item-title'})
list_ref=[item["href"] for item in soup.find_all('a',{'class' : 'item-title'}) if "href" in item.attrs]
list_ref
temp=[]
whole_temp=[]
n= len(list_ref)
l=0
print("The list length is :"+str(n))
for i in range (0,n,1):
    whole_temp.append(temp.append(list_ref[i].split('/')))
    print(whole_temp)
    #n_temp=len(whole_temp)
    #print(n_temp)
    #for j in range(0,n,1):
     #   for l in range(0,4,1):
      #         print(list_ref[i])
       #     l=0
print('over')
#cat_ref_dict={}
#n=len(list_ref)
#for i in range(2,n,1):
#    cat_ref_dict[list_cat[i]]=list_ref[i]
#print(cat_ref_dict)
    


# In[82]:


import requests 
page = requests.get('https://www.ndtv.com/')
from bs4 import BeautifulSoup as BS
soup = BS(page.content, 'html.parser')
list = soup.find_all('a',{'class' : 'item-title'})
list_ref=[item["href"] for item in soup.find_all('a',{'class' : 'item-title'}) if "href" in item.attrs]
#list_ref
#n=len(list_ref)
#print(n)
for i in range (0,n):
    t=list_ref[i].split()
    n_t=t[0].split('/')
    #print(n_t)
    n_n_t=n_t[4].split('-')
    size=len(n_n_t)
    for j in range (0,size):
        if(n_n_t[j]=='woman' or n_n_t[j]=='women' or n_n_t[j]=='girl'):
            print(list_ref[i]+", ")
print('over')

