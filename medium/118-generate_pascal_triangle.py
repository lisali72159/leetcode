# Generate Pascal's triangle given n number of rows.

# Input: 5
# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
 
 def generate(self, numRows):
        if numRows == 0: return []
        if numRows == 1: return [[1]]
        # if numRows == 2: return [[1], [1,1]]
        
        prevTriangle = self.generate(numRows - 1)
        lastRow = prevTriangle[-1]
        newRow = [1]
        
        for i in range(len(lastRow) - 1):
            newRow.append(lastRow[i] + lastRow[i + 1])
        newRow.append(1)
        prevTriangle.append(newRow)
        return prevTriangle
            