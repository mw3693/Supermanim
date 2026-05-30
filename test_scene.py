from manim import *

class TestRemove(Scene):
    def construct(self):
        circles = VGroup(*[
            Circle().shift(RIGHT * i)
            for i in range(50)
        ])

        self.add(circles)
        self.wait(1)

        # stress test remove
        self.remove(*circles[:25])
        self.wait(1)

        self.remove(*circles[25:])
        self.wait(1)
