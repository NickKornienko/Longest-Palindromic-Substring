class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestPal = ""
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if len(longestPal) >= j-i:
                    break
                elif self.isPalindrome(s[i:j]):
                    longestPal = s[i:j]
                    break
        return longestPal

    def isPalindrome(self, s):
        return s == s[::-1]


def main():
    testString = "babad"
    sol = Solution()
    print(sol.longestPalindrome(testString)) 

if __name__ == "__main__":
    main()
