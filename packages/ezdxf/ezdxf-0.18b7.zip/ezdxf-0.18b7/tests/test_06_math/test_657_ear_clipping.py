# Copyright (c) 2021, Manfred Moitzi
# License: MIT License
import pytest
import math
from ezdxf.math import triangulation, Vec3, Vec2
from ezdxf.render import forms


def calculate_total_area(triangles):
    result = []
    for triangle in triangles:
        sides = []
        for i in range(3):
            next_index = (i + 1) % 3
            pt = triangle[i]
            pt2 = triangle[next_index]
            # Distance between two points
            side = math.sqrt(
                math.pow(pt2[0] - pt[0], 2) + math.pow(pt2[1] - pt[1], 2)
            )
            sides.append(side)
        c, b, a = sorted(sides)
        area = 0.25 * math.sqrt(
            abs((a + (b + c)) * (c - (a - b)) * (c + (a - b)) * (a + (b - c)))
        )
        result.append((area, a, b, c))
    triangle_area = sum(tri[0] for tri in result)
    return triangle_area


class PolyData:
    def __init__(self, name, vertices, triangles, total_area):
        self.name = name
        self.vertices = vertices
        self.triangles = triangles
        self.total_area = total_area


TEST_DATA = [
    PolyData(
        name="Star",
        vertices=[
            (350, 75),
            (379, 161),
            (469, 161),
            (397, 215),
            (423, 301),
            (350, 250),
            (277, 301),
            (303, 215),
            (231, 161),
            (321, 161),
        ],
        triangles=[
            ((321, 161), (350, 75), (379, 161)),
            ((379, 161), (469, 161), (397, 215)),
            ((397, 215), (423, 301), (350, 250)),
            ((350, 250), (277, 301), (303, 215)),
            ((303, 215), (231, 161), (321, 161)),
            ((321, 161), (379, 161), (397, 215)),
            ((321, 161), (397, 215), (350, 250)),
            ((321, 161), (350, 250), (303, 215)),
        ],
        total_area=18055.0,
    ),
    PolyData(
        name="Simple Diamond",
        vertices=[
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, 0),
        ],
        triangles=[((0, 1), (-1, 0), (0, -1)), ((0, 1), (0, -1), (1, 0))],
        total_area=2.0,
    ),
    PolyData(
        name="No Concave Vertex",
        vertices=[
            (-2.0, -17.0),
            (-2.0, -8.0),
            (-8.0, -2.0),
            (-17.0, -2.0),
            (-20.0, -8.0),
            (-18.0, -17.0),
            (-12.0, -24.0),
            (-7.0, -22.0),
        ],
        triangles=[
            ((-7.0, -22.0), (-2.0, -17.0), (-2.0, -8.0)),
            ((-7.0, -22.0), (-2.0, -8.0), (-8.0, -2.0)),
            ((-7.0, -22.0), (-8.0, -2.0), (-17.0, -2.0)),
            ((-7.0, -22.0), (-17.0, -2.0), (-20.0, -8.0)),
            ((-7.0, -22.0), (-20.0, -8.0), (-18.0, -17.0)),
            ((-7.0, -22.0), (-18.0, -17.0), (-12.0, -24.0)),
        ],
        total_area=297.5,
    ),
    PolyData(
        name="Slanted Side",
        vertices=[
            (-10.0, -20.0),
            (-10.0, -30.0),
            (0.0, -20.0),
            (0.0, -10.0),
            (-20.0, -10.0),
            (-20.0, -20.0),
        ],
        triangles=[
            ((-10.0, -20.0), (-10.0, -30.0), (0.0, -20.0)),
            ((-10.0, -20.0), (0.0, -20.0), (0.0, -10.0)),
            ((-10.0, -20.0), (0.0, -10.0), (-20.0, -10.0)),
            ((-10.0, -20.0), (-20.0, -10.0), (-20.0, -20.0)),
        ],
        total_area=250.0,
    ),
    PolyData(
        name="New Thing",
        vertices=[
            (-20.0, -20.0),
            (-10.0, -20.0),
            (-10.0, -30.0),
            (0.0, -20.0),
            (10.0, -20.0),
            (0.0, -10.0),
            (10.0, 0.0),
            (0.0, 0.0),
            (-10.0, -10.0),
            (-10.0, 0.0),
            (-20.0, -10.0),
            (-30.0, -10.0),
        ],
        triangles=[
            ((-30.0, -10.0), (-20.0, -20.0), (-10.0, -20.0)),
            ((-10.0, -20.0), (-10.0, -30.0), (0.0, -20.0)),
            ((0.0, -20.0), (10.0, -20.0), (0.0, -10.0)),
            ((0.0, -10.0), (10.0, 0.0), (0.0, 0.0)),
            ((0.0, -10.0), (0.0, 0.0), (-10.0, -10.0)),
            ((-10.0, -10.0), (-10.0, 0.0), (-20.0, -10.0)),
            ((-20.0, -10.0), (-30.0, -10.0), (-10.0, -20.0)),
            ((-20.0, -10.0), (-10.0, -20.0), (0.0, -20.0)),
            ((0.0, -20.0), (0.0, -10.0), (-10.0, -10.0)),
            ((-10.0, -10.0), (-20.0, -10.0), (0.0, -20.0)),
        ],
        total_area=500.0,
    ),
    PolyData(
        name="Edge Case 1",
        vertices=[
            (40.04332790675601, -30.70794551983977),
            (54.13, -30.70794551983977),
            (54.13, -28.03),
            (69.13, -28.03),
            (69.11, -52.53),
            (40.04332790675601, -52.53),
        ],
        triangles=[
            (
                (40.04332790675601, -30.70794551983977),
                (40.04332790675601, -52.53),
                (69.11, -52.53),
            ),
            ((69.11, -52.53), (69.13, -28.03), (54.13, -28.03)),
            ((69.11, -52.53), (54.13, -28.03), (54.13, -30.70794551983977)),
            (
                (54.13, -30.70794551983977),
                (40.04332790675601, -30.70794551983977),
                (69.11, -52.53),
            ),
        ],
        total_area=674.6551258629229,
    ),
    PolyData(  # 6
        name="Edge Case 2",
        vertices=[
            (229.28340553, 78.91250014),
            (258.42948809, 17.98278109),
            (132.01956999, -22.96900817),
            (107.97774096, 23.39276058),
            (65.85573925, 28.63846858),
            (41.66373597, -92.78859248),
            (-5.59948763, -54.18987786),
            (-44.61508682, -69.7461117),
            (-28.41208894, -106.93810071),
            (-71.11899145, -125.56044277),
            (-100.84787818, -88.51853387),
            (-211.53564549, -160.76853269),
            (-244.22754588, -147.51172179),
            (-226.83717643, -42.0984372),
            (-230.65279618, -10.5455196),
            (-240.50239817, 70.87826746),
            (-12.48219264, 137.70176109),
            (4.65848369, 204.21077075),
            (176.5243417, 193.73497584),
            (171.13537712, 87.27009315),
            (229.28340553, 78.91250014),
        ],
        triangles=[],
        total_area=95980.58295872653,
    ),
    PolyData(  # 7
        name="Edge Case 3-A",
        vertices=[
            (229, 78),
            (66, 28.7),
            (-244.2, -147.5),
            (-226, -42),
            (229, 78),
        ],
        triangles=[
            ((-226.0, -42.0), (-244.2, -147.5), (66.0, 28.7)),
            ((-226.0, -42.0), (66.0, 28.7), (229.0, 78.0)),
        ],
        total_area=16195.379999999925,
    ),
    PolyData(  # 8
        name="Edge Case 3-B",
        vertices=[
            (229000, 78000),
            (66000, 28700),
            (-244200, -147500),
            (-226000, -42000),
            (229000, 78000),
        ],
        triangles=[
            ((-226000, -42000), (-244200, -147500), (66000, 28700)),
            ((-226000, -42000), (66000, 28700), (229000, 78000)),
        ],
        total_area=16195379999.999996,
    ),
    PolyData(  # 9
        name="Edge Case 4",
        vertices=[
            (-1179, -842),
            (-489, -1049),
            (101, -1226),
            (520, -558),
            (779, -175),
            (856, 257),
            (544, 806),
            (-72, 713),
            (-1004, 945),
            (-988, 62),
            (-1179, -842),
        ],
        triangles=[],
        total_area=3112796.5,  # barycenter method gives 3112796.505805846
    ),
]


class TestPolygons:
    @pytest.mark.parametrize("poly_data", TEST_DATA)
    def test_polygon(self, poly_data):
        triangles = list(
            triangulation.ear_clipping_2d(poly_data.vertices, fast=True)
        )
        total_area = calculate_total_area(triangles)
        absolute_error = abs(poly_data.total_area - total_area)
        assert (
            absolute_error < triangulation.EPSILON
        ), "{}: area absolute error ({} - {} = {}) >= epsilon ({})".format(
            poly_data.name,
            poly_data.total_area,
            total_area,
            absolute_error,
            triangulation.EPSILON,
        )
        if len(poly_data.triangles) > 0:
            assert triangles == poly_data.triangles


def test_open_polygons_are_the_regular_case():
    result = list(
        triangulation.ear_clipping_2d(
            [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1)]
        )
    )
    assert len(result) == 4


def test_closed_polygons_work_also_as_expected():
    result = list(
        triangulation.ear_clipping_2d(
            [(0, 0), (1, 0), (1, 1), (1, 2), (0, 2), (0, 1), (0, 0)]
        )
    )
    assert len(result) == 4


def test_empty_input_returns_empty_result():
    result = list(triangulation.ear_clipping_2d([]))
    assert len(result) == 0


def test_single_vertex_returns_empty_result():
    result = list(triangulation.ear_clipping_2d([(0, 0)]))
    assert len(result) == 0


class TestEarClipping3D:
    def test_simple_case(self):
        cube = forms.cube()
        for face in list(cube.faces_as_vertices()):
            result = list(triangulation.ear_clipping_3d(face))
            assert len(result) == 2

    def test_polygon(self):
        polygon = Vec3.list(
            [
                (0, 0, 0),
                (1, 0, 0),
                (1, 0, 1),
                (2, 0, 1),
                (2, 0, 2),
                (0, 0, 2),
            ]
        )
        result = list(triangulation.ear_clipping_3d(polygon))
        assert len(result) == 4
        for triangle in result:
            assert all(abs(v.y) < 1e-9 for v in triangle)

    def test_input_type_is_Vec3(self):
        with pytest.raises(TypeError):
            list(triangulation.ear_clipping_3d([(0, 0, 0)]))  # type: ignore

    def test_empty_input_returns_empty_result(self):
        assert len(list(triangulation.ear_clipping_3d([]))) == 0

    def test_invalid_polygon_raise_zero_division_error(self):
        with pytest.raises(ZeroDivisionError):
            list(
                triangulation.ear_clipping_3d(
                    Vec3.list([(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
                )
            )


def test_simple_polygon_triangulation():
    open_square = forms.square()
    r = triangulation.simple_polygon_triangulation(open_square)
    assert len(r) == 4
    center = r[0][2]
    assert center == (0.5, 0.5, 0)

    closed_square = list(forms.circle(4, elevation=2, close=True))
    assert len(closed_square) == 5
    r = triangulation.simple_polygon_triangulation(closed_square)
    assert len(r) == 4
    center = r[0][2]
    assert center.isclose((0, 0, 2))

    # also subdivide triangles
    r = triangulation.simple_polygon_triangulation(
        Vec3.list([(0, 0), (1, 0), (1, 1)])
    )
    assert len(r) == 3


def test_fast_mode_is_not_reliable_for_concave_polygons():
    """The fast mode takes a shortcut for small faces (< 6 vertices) but this
    is not reliable for concave faces!
    """
    concave = Vec2.list([(0, 0), (1, 1), (2, 0), (1, 2)])
    area_correct = calculate_total_area(
        triangulation.ear_clipping_2d(concave, fast=False)
    )
    area_fast = calculate_total_area(
        triangulation.ear_clipping_2d(concave, fast=True)
    )
    assert abs(area_fast - area_correct) > 1e-6


if __name__ == "__main__":
    pytest.main([__file__])
