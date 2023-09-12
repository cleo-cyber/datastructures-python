class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        

        if matrix[0][0]==target:
            return True
        
        for m in range(len(matrix)):
          if matrix[m][0]<=target and matrix[m][-1]>=target:
             for n in range(len(matrix[m])):
               if matrix[m][n]==target:
                   return True
        return False
    
    