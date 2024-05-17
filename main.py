points = [(3, 6), (8, 2), (15, 11), (23, 1), (4, 5)]


def euclideanDistance(point1, point2):
    x_diff = point1[0] - point2[0]
    y_diff = point1[1] - point2[1]
    return ((x_diff ** 2) + (y_diff ** 2)) ** 0.5


distances = []

for i in range(len(points) - 1):
    for k in range(i + 1, len(points)):
        distances.append(euclideanDistance(points[i], points[k]))

print(len(points))
print(distances)
print(f"minimum distance is = {min(distances)}")
