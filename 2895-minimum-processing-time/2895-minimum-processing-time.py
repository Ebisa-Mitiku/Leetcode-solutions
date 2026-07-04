class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        time=sorted(processorTime,reverse=True)
        task=sorted(tasks)
        n=len(time)
    
        i=0
        start=0
        ans=0

        while i<n:
            
            for j in range(start,start+4):
                ans=max(ans,time[i]+task[j])

            i+=1 
            start+=4  
        return ans 
                
                
