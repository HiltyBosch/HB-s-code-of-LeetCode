#coding=utf-8
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longestBefore = [1]     #list for longest length of the palindrome when end by the before char
        longestCurrent = [1]    #same above but for the current char
        longest = 1
        returnStr = s[0]
        for i in xrange(1, s.__len__()):
            if s[i] == s[i-1]:
                longestCurrent[0] = longestBefore[0]+1
                if longestCurrent[0] > longest:
                    longest = longestCurrent[0]
                    returnStr = s[i-longestBefore[0]:i+1]
            for length in longestBefore:
                if i - length  > 0 and s[i] == s[i-length-1]:
                    longestCurrent.append(length+2)
                    if length+2 > longest:
                        longest = length+2
                        returnStr = s[i-length-1:i+1]
            longestBefore = longestCurrent
            longestCurrent =[1]
        return returnStr


if __name__ == '__main__':
    solution = Solution()
    print solution.longestPalindrome('abcbd')
    print solution.longestPalindrome('aaaaa')
    print solution.longestPalindrome('baaacaaap')
    print solution.longestPalindrome('bcbaabcba')
