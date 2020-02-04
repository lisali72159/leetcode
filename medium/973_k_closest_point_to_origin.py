# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

# (Here, the distance between two points on a plane is the Euclidean distance.)

# You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].


def closestPoints(points, k):
    heap = []
    result = []

    for point in points:
        heapq.heapify(heap, point, (points[0] ** 2 + points[1] ** 2))
    
    while k > 0:
         temp = heapq.heappop(heap)
         result.append(temp[1])
         k -= 1
    
    return result