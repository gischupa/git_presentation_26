from manim import *

class GitFlow(Scene):
    
    
    
    def construct(self):
        # Styling
        # Commits
        commit_radius = 0.15
        line_y = -1
        # --- Pointer Settings (FIXED) ---
        font_size_main = 12
        font_size_head = 12
        arrow_length = 0.35  

    
        # Basislinie
        def draw_line():
            line = Line(LEFT * 3, LEFT * 3).set_stroke(width=4)
            line.shift(DOWN * 1)
            self.add(line)
            return line

        line = draw_line()
        
        commits = []
        positions = [LEFT * 3, LEFT * 1.5, RIGHT * 0.5, RIGHT * 1.5]

        self.add(NumberPlane())

        def make_arrow():
            return Arrow(UP * arrow_length, DOWN * arrow_length, buff=0)

        def boxed(text_obj):
            box = SurroundingRectangle(text_obj, buff=0.15)
            return VGroup(box, text_obj)
        
        def pointer_bauen():
            # Pointer initialisieren
            main_label = Text("main", font_size=font_size_main)
            head_label = Text("HEAD", font_size=font_size_head)

            main_box = boxed(main_label)
            head_box = boxed(head_label)

            arrow_main = make_arrow()
            arrow_head = make_arrow()

            main_group = VGroup(main_box, arrow_main)
            head_group = VGroup(head_box, arrow_head)
            
            return main_group, head_group

        main_group, head_group = pointer_bauen()
        
        for i, pos in enumerate(positions):
            # Commit erzeugen (erstmal blau)
            commit = Circle(radius=commit_radius, color=BLUE, fill_opacity=1)
            commit.move_to(pos + DOWN)
            commits.append(commit)

            # Linie verlängern
            new_line = Line(line.get_start(), pos + DOWN).set_stroke(width=4)
            self.play(
                Transform(line, new_line),
                FadeIn(commit, scale=0.5),
                run_time=0.8
            )

            # Pointer beim ersten Commit erzeugen
            if i == 0:
                main_group.arrow_main.next_to(commit, UP, buff=0.05)
                main_group.main_box.next_to(arrow_main, UP, buff=0.05)

                head_group.arrow_head.next_to(main_box, UP, buff=0.05)
                head_group.head_box.next_to(arrow_head, UP, buff=0.05)

                self.play(FadeIn(main_group), FadeIn(head_group))

                # Aktuellen Commit gelb färben
                self.play(commit.animate.set_fill(YELLOW), run_time=0.3)
            else:
                # Neue Pointer Positionen
                new_arrow_main = make_arrow()
                new_arrow_main.next_to(commit, UP, buff=0.05)

                new_main_box = boxed(Text("main", font_size=font_size_main))
                new_main_box.next_to(new_arrow_main, UP, buff=0.05)

                new_arrow_head = make_arrow()
                new_arrow_head.next_to(new_main_box, UP, buff=0.05)

                new_head_box = boxed(Text("HEAD", font_size=font_size_head))
                new_head_box.next_to(new_arrow_head, UP, buff=0.05)

                new_main_group = VGroup(new_main_box, new_arrow_main)
                new_head_group = VGroup(new_head_box, new_arrow_head)

                prev_commit = commits[i - 1]

                self.play(
                    Transform(main_group, new_main_group),
                    Transform(head_group, new_head_group),
                    # Farbwechsel: alter blau, aktueller gelb
                    prev_commit.animate.set_fill(BLUE),
                    commit.animate.set_fill(YELLOW),
                    run_time=0.6
                )

            self.wait(0.3)

        self.wait(1)
