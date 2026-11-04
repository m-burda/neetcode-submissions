class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s)))
            encoded.append("#")
            encoded.append(s)
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoded = []
        i = 0
        while i < len(s) - 1:
            next_len = 0
            while s[i].isnumeric():
                next_len *= 10
                next_len += int(s[i])
                i += 1
            i += 1
            decoded.append(s[i:i+next_len])
            i += next_len
        
        return decoded



