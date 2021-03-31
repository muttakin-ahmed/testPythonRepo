import math

points = [(-2, -4), (0, -2), (-1, 0), (3, -5), (-2, -3), (3,2)]
distances = []
points_with_dis = []

class point_with_dis:
    center = 0
    distance = 0

def calculate_dist(x, y):
    return math.sqrt(x*x + y*y)

for i in range(len(points)):
    point = points[i]
    distance = calculate_dist(points[i][0], points[i][1])
    distances.append(distance)

    pwd = point_with_dis()
    pwd.center = point
    pwd.distance = distance
    points_with_dis.append(pwd)

max_heap = distances[:3]
for p in range(len(points_with_dis[4:])):
    if points_with_dis[p].distance < max(max_heap):
        #replace max_heap value with this distance
        max_heap.pop(max_heap.index(max(max_heap)))
        print(max_heap)
        max_heap.append(points_with_dis[p].distance)
        print(max_heap)
