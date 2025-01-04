


class Solution:
    def palindrome_with_recursion(self, string):
        
        # using recursion slicing
        if len(string) <= 1:            # base case
            return True
        else:
            if string[0] == string[-1]:
                return self.palindrome_with_recursion(string[1:-1])
            else:
                return False
            
    # without recursion
    def palindrome_without_recursion(self, string):
        return string == string[::-1]
    
    def palindrome(self, string):
        left = 0
        right = len(string)-1

        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1
        return True


string = "TENET"
solution = Solution()
print(solution.palindrome_without_recursion(string))
print(solution.palindrome_with_recursion(string))
print(solution.palindrome(string))










# my_str = "hello"
# The slice my_str[1:-1] does the following:
# 1 (start): Refers to the second character, 'e'.
# -1 (stop): Refers to the last character, 'o', but this character is excluded.


# my_str = "Python"
# print(my_str[0:-1])    Output: "Pytho"
# print(my_str[-1])      Output: "n"

# my_list = [10, 20, 30, 40, 50]
# print(my_list[0:-1])   Output: [10, 20, 30, 40]
# print(my_list[-1])     Output: 50

