class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum())
        cleaned = cleaned.lower()
        start = 0
        stop = len(cleaned) - 1
        print(cleaned)

        while (start <= stop):
            if (start == stop):
                return True
            if (cleaned[start] != cleaned[stop]):
                return False

            start = start + 1
            stop = stop - 1
        
        return True