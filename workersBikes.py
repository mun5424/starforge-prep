class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distances = [] 
        for i, worker in enumerate(workers): 
            for j, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                distances.append((distance, i, j) )
                
        distances.sort()
        #print(distances)
        
        result = [-1] * len(workers)
        bike_used = set() 
        for distance, i,j in distances:
            #print(distance, i, j)
            if result[i] == -1 and j not in bike_used:
                result[i] = j
                bike_used.add(j) 
        
        return result