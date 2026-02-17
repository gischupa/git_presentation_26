from manim import *

class Commit(VGroup):
    def __init__(self, label="", color=BLUE, **kwargs):
        super().__init__(**kwargs)
        circle = Circle(radius=0.2, color=color)
        text = Text(label, font_size=24).next_to(circle, DOWN)
        self.add(circle, text)

class Branch(VGroup):
    def __init__(self, name="main", commits=None, color=BLUE, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.color = color
        self.commits = commits or []
        self.line = Line(LEFT, RIGHT, color=color)
        self.add(self.line)
        self._arrange_commits()

    def _arrange_commits(self):
        for i, commit in enumerate(self.commits):
            commit.move_to(self.line.get_start() + RIGHT * i * 1.5)
            self.add(commit)

    def add_commit(self, commit):
        self.commits.append(commit)
        commit.move_to(self.line.get_start() + RIGHT * (len(self.commits)-1) * 1.5)
        self.add(commit)

class Pointer(VGroup):
    def __init__(self, branch, commit_index=-1, color=YELLOW, **kwargs):
        super().__init__(**kwargs)
        self.branch = branch
        self.commit_index = commit_index
        arrow = Arrow(start=UP, end=DOWN, color=color)
        self.add(arrow)
        self.update_position()

    def update_position(self, commit_index=None):
        if commit_index is not None:
            self.commit_index = commit_index
        target_commit = self.branch.commits[self.commit_index]
        self.move_to(target_commit.get_top() + UP*0.3)

class GitTimeline(VGroup):
    def __init__(self, branches=None, **kwargs):
        super().__init__(**kwargs)
        self.branches = branches or []
        self._arrange_branches()

    def _arrange_branches(self):
        for i, branch in enumerate(self.branches):
            branch.shift(DOWN * i * 2)
            self.add(branch)

class GitDemo(Scene):
    def construct(self):
        # Branch "main" mit zwei Commits
        cA = Commit("A")
        cB = Commit("B")
        main_branch = Branch("main", [cA, cB], color=BLUE)

        # Branch "feature" ab Commit B
        cC = Commit("C", color=GREEN)
        cD = Commit("D", color=GREEN)
        feature_branch = Branch("feature", [cC, cD], color=GREEN)
        feature_branch.shift(RIGHT*3)  # seitlich versetzt

        # Pointer auf main
        pointer_main = Pointer(main_branch, commit_index=1)

        # GitTimeline
        timeline = GitTimeline([main_branch, feature_branch])
        self.add(timeline, pointer_main)

        # Animation: Pointer über main
        self.play(FadeIn(timeline), FadeIn(pointer_main))
        self.wait(1)

        self.play(pointer_main.animate.update_position(commit_index=0))
        self.wait(0.5)
        self.play(pointer_main.animate.update_position(commit_index=1))
        self.wait(1)

        # Animation: Pointer zur feature branch
        pointer_feature = Pointer(feature_branch, commit_index=0, color=YELLOW)
        self.add(pointer_feature)
        self.play(pointer_feature.animate.update_position(commit_index=0))
        self.wait(0.5)
        self.play(pointer_feature.animate.update_position(commit_index=1))
        self.wait(1)

        # Merge: Feature zurück zu main (visualisiert mit Linie)
        merge_line = Line(start=feature_branch.commits[-1].get_bottom(),
                          end=main_branch.commits[-1].get_top(), color=PURPLE)
        self.play(Create(merge_line))
        self.wait(2)
