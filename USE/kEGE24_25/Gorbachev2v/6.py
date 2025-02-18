from shapely.geometry import Polygon
from shapely.ops import unary_union

# R1: вершины (0,0), (0,121), (99,121), (99,0)
R1 = Polygon([(0, 0), (0, 121), (99, 121), (99, 0)])
# R2: вершины (-38,-53), (-38,37), (52,37), (52,-53)
R2 = Polygon([(-38, -53), (-38, 37), (52, 37), (52, -53)])

union_poly = unary_union([R1, R2])

perimeter = union_poly.length

print("Периметр объединения:", perimeter)
