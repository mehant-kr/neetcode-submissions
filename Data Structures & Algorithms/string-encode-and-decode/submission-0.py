class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # Write your encoding logic here
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        # Write your decoding logic here
        l = len(s)
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            # "3#abc"
            length = int(s[i:j])
            r = s[j+1: j + length + 1]
            res.append(r)
            i = j + length + 1
        return res