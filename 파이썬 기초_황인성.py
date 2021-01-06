#!/usr/bin/env python
# coding: utf-8

# In[6]:


3+2


# In[9]:


a = 'hi'
print(a)


# In[10]:


#나머지
40%3


# In[11]:


"his"


# In[12]:


'his'


# In[13]:


"hi there"


# In[14]:


"hi there + his"


# In[15]:


"the" + "his"


# In[19]:


"hi".upper() #upper메소드(대문자로 바꿔주는 메소드)


# In[18]:


len('ola') #길이를 알려주는 함수(자주 쓰이는 함수)


# In[21]:


len('3455555')


# In[22]:


len(str(3455555))


# In[24]:


name = "his"


# In[25]:


name


# In[26]:


name = "hisssss"


# In[27]:


name


# In[28]:


len(name)


# ## print 함수

# In[29]:


#여러 개의 값을 한 번에 확인할 때


# In[30]:


print(name)


# ## 데이터 보관소 : 리스트, 딕셔너리

# # 리스트

# In[34]:


lottery = [3, 42, 12, 19, 30, 59]

lottery


# In[35]:


len(lottery)


# In[36]:


# 오름 차순 정렬 함수
lottery.sort()


# In[39]:


# 내림 차순 정렬 함수
lottery.reverse()


# In[40]:


lottery


# In[42]:


# home, end, tab 키의 활용


# ### append 함수

# In[43]:


lottery.append(5)


# In[45]:


lottery


# In[46]:


lottery[0]


# ### 리스트 인덱싱
# #위치 0은 첫 번째

# In[48]:


lottery[3]


# In[49]:


# 리스트 안에 요소 삭제
lottery.pop(0)


# In[50]:


lottery


# # 딕셔너리

# In[ ]:


# 리스트 vs 딕셔너리
  순서가 있고  순서가 없다
    인덱싱       key값으로 value값을 찾는다


# In[53]:


{}


# In[59]:


participant = {'name':'Ola', 'country':'Poland', 'favorite_numbers':[7, 42, 92]}
participant


# In[55]:


len(participant)


# In[57]:


participant['mame']


# In[60]:


participant


# In[61]:


participant['favorite_numbers']


# In[ ]:


1. 자료형
2. 데이터 저장소 : 리스트, 딕셔너리


# ## 튜플

# 튜플 : 데이터 수정이 안된다

# In[62]:


monitor = (1920, 1080)

monitor


# In[64]:


m2 = 1920, 1080
m2


# In[65]:


a, b = 1, 2


# In[66]:


a


# ## 참거짓(불리언, boolean) 자료형

# 자료형 : 숫자형, 문자형, 불리언(True, False)

# In[67]:


5 > 2


# In[68]:


3 < 1


# = 변수에 값을 입력할 때
# == 값이 같다

# In[70]:


5 == 2


# In[72]:


5!=2


# 내일은 크롤링 직접

# In[ ]:





# In[ ]:





# In[ ]:




