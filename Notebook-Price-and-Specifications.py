#!/usr/bin/env python
# coding: utf-8

# 
# 將Google雲端硬碟掛載到Colab環境中的
# '/content/drive'路徑
# 

# In[5]:


from google.colab import drive
drive.mount('/content/drive')


# 更改當前工作目錄

# In[6]:


get_ipython().run_line_magic('cd', '/content/drive/MyDrive/Github')


# 版本控制
# 安裝

# In[ ]:


get_ipython().system('apt-get install git')


# 初始化一個本地git儲存庫

# In[38]:


get_ipython().system('git init Notebook-Price-and-Specifications')


# In[39]:


get_ipython().run_line_magic('cd', 'Notebook-Price-and-Specifications/')


# In[40]:


get_ipython().run_line_magic('ls', '-a')


# In[44]:


get_ipython().system('git status')


# In[58]:


get_ipython().system('git add .')


# In[46]:


get_ipython().system('git status')


# In[59]:


get_ipython().system('git commit -m "init"')


# In[54]:


get_ipython().system('git status')


# 配置

# In[50]:


username = "Hsu-Linda"
git_token = "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"
repository = "Notebook-Price-and-Specifications"


# 告訴git儲存庫 遠程儲存庫i.e.github 
# 設置一個名為origin的地址 URL

# In[52]:


# 正常程序 !git remote add origin url
# 如果remote url設定錯誤 把add 換成 set-url
get_ipython().system('git remote set-url origin https://{git_token}@github.com/{username}/{repository}.git')
get_ipython().system('git remote -v')


# 把變更推送到遠程庫 github

# In[60]:


get_ipython().system('git push origin master')


# 嘗試逐行

# In[2]:


get_ipython().system('pip install jupyter')
get_ipython().system('pip install nbconvert')


# In[ ]:





# In[7]:


get_ipython().system('jupyter nbconvert Notebook-Price-and-Specifications.ipynb --to python')

