class CountSquares:

    def __init__(self):
        self.points = {} # {point: point count} # This is to count the ways faster.

    def add(self, point: List[int]) -> None:
        t_point = tuple(point)
        if t_point in self.points:
            self.points[t_point] += 1
        else:
            self.points[t_point] = 1

    def count(self, point: List[int]) -> int:
        qx, qy = point
        total = 0
        for p, cnt in self.points.items():
            x, y = p

            if qy == y and qx != x:
                # Found a possible one horizontal line & d (length)
                d = abs(qx - x)
                
                # Find points that are away by d length from query point
                # horizontal line으로부터 위쪽 정사각형
                if ((qx, qy + d) in self.points and (x, y + d) in self.points):
                    total += (self.points[(qx, qy+d)] * self.points[(x, y+d)] * self.points[(x,y)])
                # horizontal line으로부터 아래쪽 정사각형
                if ((qx, qy - d) in self.points and (x, y - d) in self.points):
                    total += (self.points[(qx, qy-d)] * self.points[(x, y-d)] * self.points[(x,y)])
        return total


                

