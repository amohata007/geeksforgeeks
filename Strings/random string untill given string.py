import random
import string
import time
a = input("Enter string:")
alp = string.ascii_lowercase + string.ascii_uppercase + string.digits
ans = ''.join(random.choice(alp) for i in range(len(a)))
res = ''
cnt = 0
flag = 0
while flag==0:
    print(ans)
    flag=1
    res = ''
    for i in range(len(a)):
        if a[i]==ans[i]:
            res += a[i]
        else:
            flag=0
            res += random.choice(alp)
    cnt+=1
    ans = res
    time.sleep(0.2)
print(cnt)

