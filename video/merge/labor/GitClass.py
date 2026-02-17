from manim import *


class Commit(VGroup):
    def __init__(self, label="", **kwargs):
        super().__init__(**kwargs)
        circle = Circle(radius=0.2, color=BLUE, fill_opacity=1)
        text = Text(label, font_size=24).next_to(circle, DOWN)
        self.add(circle, text)

class Branch(VGroup):
    def __init__(self, name="main", commits=None, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.commits = commits or []
        self.line = Line(LEFT, 2*RIGHT, color=WHITE)
        self.add(self.line)
        self._arrange_commits()

    def _arrange_commits(self):
        for i, commit in enumerate(self.commits):
            commit.move_to(self.line.get_start() + np.array([0, -0.25, 0]) + RIGHT*i*1.5)
            self.add(commit)

class Pointer(VGroup):
    def __init__(self, branch, commit_index=-1, **kwargs):
        super().__init__(**kwargs)
        self.branch = branch
        self.commit_index = commit_index
        arrow = Arrow(start=UP, end=DOWN, color=YELLOW)
        self.add(arrow)
        self.update_position()

    def update_position(self):
        target_commit = self.branch.commits[self.commit_index]
        self.move_to(target_commit.get_top() + UP*0.3)

class GitTimeline(VGroup):
    def __init__(self, branches=None, **kwargs):
        super().__init__(**kwargs)
        self.branches = branches or []
        self._arrange_branches()

    def _arrange_branches(self):
        for i, branch in enumerate(self.branches):
            branch.shift(DOWN * i * 1.5)
            self.add(branch)
