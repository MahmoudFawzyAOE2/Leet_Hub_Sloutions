class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        records = []
        for i in range(len(ops)):
            if ops[i] =='+' :
                records.append(records[-1]+records[-2]) 
            elif ops[i] =='C' :
                records.pop()   
            elif ops[i] =='D' :
                records.append(2*records[-1])
            else :
                records.append(int(ops[i]))
        
        return sum(records)