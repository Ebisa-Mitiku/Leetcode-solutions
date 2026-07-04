class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
     
        processorTime.sort(reverse=True)
        tasks.sort()
        ans=0

        for i in range(len(processorTime)):
            ans=max(ans, processorTime[i]+tasks[4*i+3])

        return ans
    
      
                
