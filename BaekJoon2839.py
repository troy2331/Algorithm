#!/usr/bin/env python
# coding: utf-8

# In[ ]:


N = int(input())
if N == 7:
    print(-1)
elif N >= 5:
    Num1 = (N//5)
    B =(N % 5)
    if B == 0:
        print(Num1)
    elif B == 3 or B == 1:
        print(Num1 + 1)
    elif B == 4 or B == 2:
        print(Num1 + 2)
    else:
        print(-1)
elif N == 3:
    print(1)
elif N == 4:
    print(-1)
else:
    print(-1)

