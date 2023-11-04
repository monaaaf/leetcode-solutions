class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Handle negative numbers, which are not palindromes
        if x < 0:
            return False

        # Reverse the integer
        reversed_x = 0
        original_x = x
        while x > 0:
            digit = x % 10
            reversed_x = reversed_x * 10 + digit
            x //= 10

        # Check if the reversed integer is equal to the original integer
        return reversed_x == original_x
