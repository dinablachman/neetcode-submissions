class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding = ""
        for s in strs:
            encoding += (str(len(s)) + '#' + s)
        return encoding

    def decode(self, s: str) -> List[str]:
        length = s.count("#")
        decoded = []
        i = 0
        while (i < len(s)):
            str_len = ''
            while s[i] != '#' and s[i] != '':
                str_len += s[i]
                i = i + 1

            # we are at a '#' char, now read str_len chars forward
            i = i + 1 # move to first char of string
            j = i + int(str_len)
            string = s[i:j]
            decoded.append(string)

            # move ahead to next string
            i = j
        return decoded

        

        
