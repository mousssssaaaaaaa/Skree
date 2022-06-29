from code.functions import distance as d

def distance_to_H(point, list_H):
    """Returns the smallest distance to an H aminocode"""
    dis = []
    for point_H in list_H:
        distance = d.distance(point_H, point)
        dis.append(distance)

    return min(dis)