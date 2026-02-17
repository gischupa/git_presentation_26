from GitClass import *

class GitExample(Scene):
    def construct(self):
        c1 = Commit("").move_to(np.array([0,0,0]))
        c2 = Commit("").move_to(np.array([0.3,0,0]))
        c3 = Commit("").move_to(np.array([0.6,0,0]))
        b1 = Commit("").move_to(np.array([0.9,0,0]))
        b2 = Commit("").move_to(np.array([1.2,0,0]))
        b3 = Commit("").move_to(np.array([1.5,0,0]))
        b4 = Commit("").move_to(np.array([1.8,0,0]))

        seq = [c1,c2,c3,b1,b2,b3,b4]

        #main_branch = Branch("main", [c1, c2, c3])
        #pointer = Pointer(main_branch, commit_index=1)
        
        #timeline = GitTimeline([main_branch])
        #self.add(timeline, pointer)

        #self.play(FadeIn(timeline), FadeIn(pointer))
        #self.add(main_branch)       
        for c in seq:
            self.add(c)
            self.wait(2)

        self.wait(2)
