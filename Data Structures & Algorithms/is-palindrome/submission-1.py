class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=s.lower()
        c = ""
        for ch in s1:
            if ch.isalnum():
                c+=ch
        return c == c[::-1]
        