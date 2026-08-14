class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        longest=0
        left=0
        cnt=defaultdict(int)

        for right in range(len(s)):
            if cnt[s[right]]!=2:
                cnt[s[right]]=cnt.get(s[right],0)+1
            else:
                longest=max(longest,right-left)

                while cnt[s[right]]==2:
                    cnt[s[left]]-=1
                    if cnt[s[left]]==0:
                        del cnt[s[left]]
                    left+=1
                cnt[s[right]]+=1
        longest=max(longest,(right-left)+1)
        return longest









        