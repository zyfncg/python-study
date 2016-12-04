#-*- coding:utf-8 -*-
class Solution():
    def describe(self, a):
        sums=0.0
        leng=len(a)
        for x in a:
            sum+=x
        ave=sums*1.0/leng
        v2=0.0
        v3=0.0
        v4=0.0
        for x in a:
            v2+=(x-ave)**2
            v3+=(x-ave)**3
            v4+=(x-ave)**4
        if leng<2:
            return [ave,None,0,-3]
        var=v2/(leng-1)
        skew=v3*(leng**0.5)/(v2**1.5)
        kurt=v4*leng/(v2**2)-3
        return [round(ave,6),round(var,6),round(skew,6),round(kurt,6)]
solu=Solution()
print solu.describe([1,2,3])