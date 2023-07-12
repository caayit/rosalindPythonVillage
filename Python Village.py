#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[1]:


import this


# # Question 2
# 
# Problem
# Given: Two positive integers a
#  and b
# , each less than 1000.
# 
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a
#  and b
# .
# 
# Notes:
# 
# The dataset changes every time you click "Download dataset".
# We check only your final answer to the downloaded dataset in the box below, not your code itself. If you would like to provide your code as well, you may use the upload tool. Please also note that the correct answer to this problem will not in general be 34; it is simply an example of what you should return in the specific case that the legs of the triangle have length 3 and 5.

# In[6]:


def q2(a,b):
    
    c = a**2 + b**2
    
    return c


# In[7]:


q2(3,5)


# # Question 3
# 
# Problem
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# 
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

# In[12]:


s = "EHneRzVDg1jSs0ZDQDnRgPXxq3Dbhj2pzOp6JhyOxyuraf23ta7kYoVrSQYBJjGxzjpClatiscutatusqWg8fq1wI2bFRAQSR9ammm4sIIKsQTHJunm9QZh8JnTIAoxE8aJTjdM8MSN3j6tpfLO1lYno5zACi1vpORO3RIdqVFIk4S7DIF3cfPaAAtYi"
a,b,c,d = 39, 44, 68, 79


# In[14]:


print(s[a:b+1], s[c:d+1])


# # Question 4
# 
# Given: Two positive integers a and b (a<b<10000)
# 
# Return: The sum of all odd integers from a through b, inclusively.

# In[20]:


a = 4361 
b = 9197


# In[21]:


sum = 0
for i in range(a, b+1, 2):
    sum += i


# In[23]:


print(sum)


# # Question 5
# 
# Given: A file containing at most 1000 lines.
# 
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# In[76]:


f = open('../../../Downloads/rosalind_ini5.txt', 'r')
f = f.readlines()


# In[77]:


evenLineNumbers = range(1, len(f)+1, 2)


# In[78]:


evenLines = []
for i in evenLineNumbers:
    evenLines.append(f[i].strip())


# In[79]:


for i in evenLines:
    print(i)


# # Question 6
# 
# Given: A string s of length at most 10000 letters.
# 
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

# In[69]:


s = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'


# In[70]:


words = s.split()
word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1


# In[75]:


for word in set(words):
    print(word, word_counts[word])

