class Solution:
    # 잘 안쓰이는 문자열을 delimiter로 씀.
    # 아예 non-ASCII character를 delimiter로 쓰는 방법도 있음.
    # -> π
    def encode(self, strs: List[str]) -> str:
        return "`''`".join(strs) if len(strs) >= 1 else "`''`empty`''`"
    def decode(self, s: str) -> List[str]:
        
        return s.split("`''`") if s != "`''`empty`''`" else []
