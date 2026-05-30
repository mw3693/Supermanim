import pytest
from manim import *

def test_remove_mobjects():
    scene = Scene()

    circle = Circle()
    square = Square()

    scene.add(circle, square)

    assert circle in scene.mobjects
    assert square in scene.mobjects

    scene.remove(circle)

    assert circle not in scene.mobjects
    assert square in scene.mobjects
