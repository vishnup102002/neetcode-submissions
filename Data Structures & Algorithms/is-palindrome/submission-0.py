class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=""
        for c in s:
            if c.isalnum():
                st += c.lower()
        a=0
        b=len(st)-1
        while a<=b:
          if st[a]==st[b]:
            a+=1
            b-=1
          else:
            return False
        return True
