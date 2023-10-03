class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        # Loop through the array
        # Check if val at array i equals to x
        # Add the index and array in hashmap
        # Check if val at array i equals to y:
        # Add the index and val to hashmap
        
        hashmap = {}
        min_val = float('inf')
        an = -1
        for i, n in enumerate(points):
            if n[0] == x or n[1] == y:
                hashmap[i] = n
        for i in sorted(hashmap):
            x2 = hashmap[i][0]
            y2 = hashmap[i][1]
            manhat = abs(x - x2) + abs(y - y2)
            
            if manhat < min_val:
                an = i
                min_val = manhat
        return an


                
