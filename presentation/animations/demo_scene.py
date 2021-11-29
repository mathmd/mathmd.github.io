from manim import *
from manim_revealjs import PresentationScene, COMPLETE_LOOP


config.video_dir= "./videos"

toc=Group(
    Tex("1.~Decoding Pauli noise"),
    Tex("2.~Tensor network decoding"),
    Tex("3.~Contracting 2D tensor networks"),
    Tex("4.~","Sweepline"," Contraction"),
    Tex("5.~Numerics"),
    Tex("6.~Results"),
    Tex("7.~Conclusion"),
).arrange(DOWN,aligned_edge=LEFT,buff=0.5).move_to(ORIGIN)

class DemoScene(PresentationScene):
    def construct(self):
        # TODO find out why end_fragment has the t parameter
        rect = Rectangle(fill_color=BLUE, fill_opacity=1)
        self.play(Create(rect))
        self.end_fragment()

        self.play(rect.animate.shift(UP).rotate(PI / 3))
        self.end_fragment()

        self.play(rect.animate.shift(3*LEFT))
        self.end_fragment()

class Title(PresentationScene):
    def construct(self):
        title = Tex(r"\bfseries\textsc{Roles of Computational Study \\in Brugada Syndrome}").scale(1.25).shift(2.4*UP)
        # arxiv = Tex(r"\bfseries\texttt{arXiv:2101.04125}").scale(.75).shift(1.5*UP)
        name = Tex(r"\text{Chanoknun Sintavanuruk}").shift(0.5*DOWN)
        affiliation = Tex(r"\text{Department of Physiology}").scale(0.8).shift(1.5*DOWN)
        # ethz=SVGMobject("ethz_logo_white.svg").scale(1/3).next_to(1.5*DOWN,LEFT,buff=2.5)
        # udes=SVGMobject("Université_de_Sherbrooke_(logo).svg").scale(1/3).next_to(1.5*DOWN,RIGHT,buff=2.5)

        self.play(Write(name,run_time=0.8))
        self.play(Write(affiliation,run_time=0.8))
        self.end_fragment()

        self.play(Write(title))
        self.end_fragment()

        self.play(FadeOut(title,name,affiliation))
        self.end_fragment()

        self.play(FadeIn(toc))
        self.end_fragment()

        self.play(toc[0].animate.scale(1.2).set_color(YELLOW))
        self.end_fragment()

        for i in range(1,7):
            self.play(toc[i].animate.scale(1.2).set_color(YELLOW),toc[i-1].animate.scale(1/1.2).set_color(WHITE))
            self.end_fragment()

        self.play(toc[-1].animate.scale(1/1.2).set_color(WHITE))
        self.end_fragment()
