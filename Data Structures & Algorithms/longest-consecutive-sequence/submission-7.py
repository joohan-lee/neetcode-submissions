class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Way 1. Sort. => Time: O(nlogn), Space: O(n)
        # Way 2. Hash Set => Time: O(n), Space: O(n)
        # Way 3. Hash Map => Time: O(n), Space: O(n)

        # mp = {
        #    숫자(key): 그 숫자를 포함하는 연속 구간의 길이(value)
        # }
        mp = defaultdict(int)
        longest = 0

        for num in nums:
            # - 중간 값들은 나중에 방문 안 함 (`if not mp[num]`으로 차단)
            if not mp[num]:
                mp[num] = mp[num-1] + mp[num+1] + 1 # 기존 길이 + 자기자신(+1)
                mp[num - mp[num-1]] = mp[num] # 현재 구간의 끝 부분만 업데이트. 중간값은 어차피 다시 안보니까 부정확해도 됨.
                mp[num + mp[num+1]] = mp[num] # 이어질 때 내 좌우측을 보는데, 그들은 그전 sequence의 끝값중 하나
                longest = max(longest, mp[num])
        
        return longest