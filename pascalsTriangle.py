class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        
        pascal = [[1]]
        prev = []
        for i in range (numRows - 1):
            innerTri = []
            innerTri.append(1)
            count = 0

            for i2 in range (i):
                if prev != [] and prev != [1]:
                    innerTri.append(prev[count]+prev[count+1])
                    count += 1

            innerTri.append(1)
            pascal.append(innerTri)
            prev = innerTri
            
        return(pascal)
        
