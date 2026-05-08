class Solution:

    def encode(self, strs: List[str]) -> str:
        return "`''`".join(strs) if len(strs) >= 1 else "`''`empty`''`"
    def decode(self, s: str) -> List[str]:
        
        return s.split("`''`") if s != "`''`empty`''`" else []
