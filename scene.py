from manim import *
import math


class SceneZero(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        cone = Cone(base_radius=r, height=h, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0).move_to((0,0,0))
        prompt = Tex(r"$<$").set_opacity(0)
        self.add_fixed_in_frame_mobjects(prompt)

        equal = Tex(r"$=$")

        self.wait(1)
        self.play(Write(cone), run_time=2)
        self.wait(2)

        #self.play(cone.animate.rotate(angle=15*DEGREES,axis=[1.,0.,0.],about_point=[0,0,0]),run_time=0.1)

        self.play(cone.animate.shift(RIGHT*4)) # right and left are inverted

        self.play(prompt.animate.set_opacity(1),run_time=2)

        def approxer(approxe,n):
            for y in range(n):
                cyl = Cylinder(radius=r*(1-(y/n)), height=h/n, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((0,0,(h/n)*y-(h/2 - (0.5)*(h/n))))
                approxe.add(cyl)
            return

        approx1 = Group()
        approxer(approx1,1)
        approx1.shift(LEFT*4)

        approx2 = Group()
        approxer(approx2,2)
        approx2.shift(LEFT*4)

        approx3 = Group()
        approxer(approx3,4)
        approx3.shift(LEFT*4)

        approx4 = Group()
        approxer(approx4,8)
        approx4.shift(LEFT*4)

        self.play(FadeIn(approx1),run_time=0.5)
        self.wait(1)
        self.play(Transform(approx1,approx2),run_time=0.5)
        self.wait(1)
        self.play(Transform(approx1,approx3),run_time=0.5)
        self.wait(1)
        self.play(Transform(approx1,approx4),run_time=0.5)
        self.wait(0.5)

class SceneZeroPartOne(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        cone = Cone(base_radius=r, height=h, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0).move_to((0,0,0))
        cone.shift(RIGHT*4)

        prompt = Tex(r"$<$")
        equal = Tex(r"$=$")

        def approxer(approxe,n):
            for y in range(n):
                cyl = Cylinder(radius=r*(1-(y/n)), height=h/n, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((0,0,(h/n)*y-(h/2 - (0.5)*(h/n))))
                approxe.add(cyl)
            return

        approx4 = Group()
        approxer(approx4,8)
        approx4.shift(LEFT*4)

        self.add(approx4,cone)
        self.add_fixed_in_frame_mobjects(prompt)
        self.wait(0.5)

        approx5 = Group()
        approxer(approx5,14)
        approx5.shift(LEFT*4)

        approx6 = Group()
        approxer(approx6,20)
        approx6.shift(LEFT*4)

        
        self.play(Transform(approx4,approx5),run_time=0.5)
        self.wait(1)
        self.play(Transform(approx4,approx6),run_time=0.5)
        self.wait(0.5)

class SceneZeroPartTwo(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        cone = Cone(base_radius=r, height=h, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0).move_to((0,0,0))
        cone.shift(RIGHT*4)

        prompt = Tex(r"$<$")
        equal = Tex(r"$=$")

        def approxer(approxe,n):
            for y in range(n):
                cyl = Cylinder(radius=r*(1-(y/n)), height=h/n, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((0,0,(h/n)*y-(h/2 - (0.5)*(h/n))))
                approxe.add(cyl)
            return

        approx6 = Group()
        approxer(approx6,20)
        approx6.shift(LEFT*4)

        self.add(approx6,cone)
        self.add_fixed_in_frame_mobjects(prompt)
        self.wait(0.5)

        cone2 = cone.copy()
        cone2.shift(LEFT*8)

        self.play(FadeOut(approx6),FadeIn(cone2),Transform(prompt,equal),run_time=0.5)
        self.wait(1)
        self.play(FadeOut(cone2),FadeOut(equal),FadeOut(cone))
        self.wait(1)

class SceneOne(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        cone = Cone(base_radius=r, height=h, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0).move_to((0,0,0))

        self.wait(1)
        self.play(Write(cone), run_time=2)
        self.wait(2)

        #self.play(cone.animate.rotate(angle=15*DEGREES,axis=[1.,0.,0.],about_point=[0,0,0]),run_time=0.1)


        equal = Tex(r"$=$   ?").set_opacity(0)
        self.add_fixed_in_frame_mobjects(equal)

        self.play(cone.animate.shift(RIGHT*4),equal.animate.set_opacity(1)) # right and left are inverted

        self.wait(2)

        self.play(cone.animate.shift(IN*20),equal.animate.shift(DOWN*20)) # right and left are inverted

class SceneCone(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)
        r=3
        h=7.5
        initia=0.0001
        cylinder1 = Cylinder(radius=r,height=initia,fill_color=GREEN,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((0,0,0))
        cylinder2 = Cylinder(radius=r,height=h,fill_color=GREEN,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((0,0,0))
        br = BraceBetweenPoints((r,0,0),(r,initia/2,0)).move_to((r-1,0,0))
        br2 = BraceBetweenPoints((r,0,0),(r,h/2,0)).move_to((r-1,0,0))
        batxt = Tex(r"h").next_to(br2)
        batxt.set_opacity(0)
        self.add_fixed_in_frame_mobjects(br,batxt)

        brb = BraceBetweenPoints((0,0,0),(0,0,0)).move_to((0,0,0))
        brb2 = BraceBetweenPoints((0,-h/2,0),(r,-h/2,0)).move_to((0,(-h/2)+1,0))
        bbtxt = Tex(r"$\pi r^2$").next_to(brb2,direction=DOWN)
        bbtxt.set_opacity(0)
        self.add_fixed_in_frame_mobjects(brb,bbtxt)

        final = Tex(r"$V(\text{cylinder}) = h \pi r^2$").shift(UP*3.6)
        final.set_opacity(0)
        self.add_fixed_in_frame_mobjects(final)

        self.wait(1)
        self.play(Transform(cylinder1,cylinder2),Transform(br,br2),batxt.animate.set_opacity(1),Transform(brb,brb2),bbtxt.animate.set_opacity(1))
        self.wait(1)
        self.play(final.animate.set_opacity(1))
        self.wait(1)

        self.play(cylinder1.animate.shift(IN*20),br.animate.shift(DOWN*20),batxt.animate.shift(DOWN*20),bbtxt.animate.shift(DOWN*20),brb.animate.shift(DOWN*20),final.animate.shift(DOWN*20))



class SceneTwo(Scene):
    def construct(self):
        # circle area proof
        r=2

        def approxer1(n,gr1,gr2):
            colour = TEAL_D
            for x in range(n):
                if x > ((n/2)-1):
                    colour=WHITE
                sector = AnnularSector(angle=r*PI/n,inner_radius=0,outer_radius=2,start_angle=2*x*PI/n,color=colour,stroke_width=5).shift(UP*1.9)
                sector.set_opacity(0.7)
                if x > ((n/2)-1):
                    gr2.add(sector)
                else:
                    gr1.add(sector)

        def approxer2(n,gr1,gr2):
            span = 2*PI/n
            colour = TEAL_D
            d=math.sqrt(2*r*r -2*r*r*math.cos(span))
            rlht= math.sqrt(r*r-d*d/4)
            for x in range(n):
                strtangle = (PI-span)/2
                a=x*d
                b=0
                if x > ((n/2)-1):
                    colour=WHITE
                    a = (x-n/2)*d
                    strtangle = (PI-span)/2 + PI
                    b=1
                sector = AnnularSector(angle=span,inner_radius=0,outer_radius=2,start_angle=strtangle,color=colour,stroke_width=5)
                sector.set_opacity(0.7)
                sector.shift(DOWN*(sector.height/2 + (5.9-sector.height)/2) + RIGHT*((d/4)*(n-1)) + LEFT*a + UP*b*rlht + LEFT*b*d/2)
                if x > ((n/2)-1):
                    gr2.add(sector)
                else:
                    gr1.add(sector)

        
        groups = []
        for x in range(6):
            a=2**(x+1)
            phase11 = Group()
            phase12 = Group()
            phase21 = Group()
            phase22 = Group()
            approxer1(a,phase11,phase12)
            approxer2(a,phase21,phase22)
            groups.append(phase11)
            groups.append(phase12)
            groups.append(phase21)
            groups.append(phase22)

        groups[2].shift(UP*0.899)
        groups[2].scale(0.9)
        groups[2].shift(DOWN*0.1*groups[2].height)
        groups[3].shift(UP*0.899)
        groups[3].scale(0.9)

        phase0 = Circle(radius=r,color=WHITE).shift(UP*1.9)
        

        self.wait(1)
        self.play(Create(phase0))
        self.wait(1)
        for x in range(6):
            if ((4*x)-1) >= 0:
                self.play(FadeIn(Group(groups[4*x]),groups[4*x +1]),FadeOut(Group(groups[(4*x)-1],groups[(4*x)-2])))
            else:
                self.play(FadeIn(Group(groups[4*x]),groups[4*x +1]))
            if (4*x+4)<=len(groups):
                self.play(ReplacementTransform(groups[4*x],groups[4*x+2]),ReplacementTransform(groups[4*x+1],groups[4*x+3]))
            self.wait(0.5)
            # self.play(ReplacementTransform(phase2,phase22))
            # self.wait(0.5)
            # self.play(FadeOut(phase22),FadeIn(phase3))


        final = Polygon([-PI*r/2,0,0],[PI*r/2,0,0],[PI*r/2,-(5.9-r)/2,0],[-PI*r/2,-(5.9-r)/2,0],color=TEAL_D,stroke_width=5).set_opacity(0.7)
        final.shift(DOWN*r/2)

        self.play(FadeOut(Group(groups[23],groups[22])),FadeIn(final))
        self.wait(1)

        circ2 =  Circle(radius=r,color=TEAL_D,stroke_width=5).shift(LEFT*3.6)
        circ2.set_opacity(0.7)

        self.play(phase0.animate.shift(DOWN*1.9 + LEFT*3.6),final.animate.shift(UP*(r/2+(5.9-r)/4) + RIGHT*3.1))
        self.play(FadeIn(circ2))
        self.wait(1)
        br1 = Brace(final,direction=UP)
        br2 = Brace(final,direction=LEFT)

        br1t = Tex(r"$\pi r$").next_to(br1, UP)
        br2t = Tex(r"$r$").next_to(br2, LEFT)

        text = Tex(r"$A(\text{circle})=\pi r \cdot r$",font_size=45).shift(DOWN*3)
        text2 = Tex(r"$A(\text{circle})=\pi r^2$",font_size=45).shift(DOWN*3)
        self.play(GrowFromCenter(br1),GrowFromCenter(br2),Write(br1t),Write(br2t))
        self.wait(1)
        self.play(Write(text))
        self.wait(0.5)
        self.play(Transform(text,text2))
        self.wait(1)
        self.play(final.animate.shift(DOWN*20),br1.animate.shift(DOWN*20),br2.animate.shift(DOWN*20),br1t.animate.shift(DOWN*20),br2t.animate.shift(DOWN*20),text.animate.shift(DOWN*20),circ2.animate.shift(DOWN*20),phase0.animate.shift(DOWN*20))



class SceneThree(Scene):
    def construct(self):
        h=7
        r=3
        triangle = Polygon([-r,0,0],[r,0,0],[0,h,0],color=WHITE)
        triangle.shift(DOWN*h/2)
        def approxer(n):
            group = Group()
            for x in range(n):
                cyl = Polygon([-r+(x*r/n),x*h/n,0],[-r+(x*r/n),(x+1)*h/n,0],[r-(x*r/n),(x+1)*h/n,0],[r-(x*r/n),x*h/n,0],color=TEAL_A).set_opacity(0.5)
                cyl.shift(DOWN*h/2)
                group.add(cyl)
            return group

        self.wait(1)

        self.play(Create(triangle))
        self.wait(1)

        phase1 =  approxer(1)
        prompt1 = Tex("Divisions = $1$").shift(UP*3 + LEFT*4.7+LEFT*6)
        phase2 =  approxer(2)
        prompt2= Tex("Divisions = $2$").shift(UP*3 + LEFT*4.7)
        phase3 =  approxer(4)
        prompt3 = Tex("Divisions = $4$").shift(UP*3 + LEFT*4.7)
        phase4 =  approxer(8)
        prompt4 = Tex("Divisions = $8$").shift(UP*3 + LEFT*4.7)
        phase5 =  approxer(16)
        prompt5 = Tex("Divisions = $16$").shift(UP*3 + LEFT*4.7)
        phase6 =  approxer(32)
        prompt6 = Tex("Divisions = $32$").shift(UP*3 + LEFT*4.7)
        phase7 =  approxer(64)
        prompt7 = Tex("Divisions = $64$").shift(UP*3 + LEFT*4.7)
        phase8 = Polygon([-r,0,0],[r,0,0],[0,h,0],color=TEAL_A).set_opacity(0.5)
        phase8.shift(DOWN*h/2)
        prompt8 = Tex(r"Divisions = $\lim_{x\to\infty} x$").shift(UP*3 + LEFT*4)

        self.play(FadeIn(phase1),prompt1.animate.shift(RIGHT*6))
        self.wait(1)

        self.play(Transform(phase1,phase2),Transform(prompt1,prompt2))
        self.wait(0.7)
        self.play(Transform(phase1,phase3),Transform(prompt1,prompt3))
        self.wait(0.7)
        self.play(Transform(phase1,phase4),Transform(prompt1,prompt4))
        self.wait(0.7)
        self.play(Transform(phase1,phase5),Transform(prompt1,prompt5))
        self.wait(0.7)
        self.play(Transform(phase1,phase6),Transform(prompt1,prompt6))
        self.wait(0.7)
        self.play(Transform(phase1,phase7),Transform(prompt1,prompt7))
        self.wait(0.7)
        self.play(Transform(phase1,phase8),Transform(prompt1,prompt8))
        self.wait(2)

        self.play(Unwrite(prompt1),FadeOut(phase1,triangle))
        self.wait(1)

        

class SceneFour(ThreeDScene):
    def construct(self):

        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        cone = Cone(base_radius=r, height=h, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0).move_to((0,0,0))

        self.play(Write(cone))

        position_list = [
            [0, h/2, 0],  # top
            [-r/2, 0, 0],  # bottom right
            [r/2, 0, 0],  # bottom left
        ]
        triangle = Polygon(*position_list, color=TEAL_E)
        triangle.move_to([0,0,0])
        triangle.set_opacity(0)

        self.add_fixed_in_frame_mobjects(triangle)

        self.play(triangle.animate.set_opacity(0.6),run_time=2)

        self.wait(1)

        self.play(FadeOut(cone),triangle.animate.scale(2))

        self.wait(1)

        

class SceneFive(Scene):
    def construct(self):
        h=7.5
        r=3

        position_list = [
            [0, h, 0],  # top
            [-r, 0, 0],  # bottom right
            [r, 0, 0],  # bottom left
        ]
        triangle = Polygon(*position_list, color=TEAL_E)
        triangle.set_opacity(0.6)
        triangle.move_to([0,0,0])

        self.add(triangle)

        self.wait(1)

        c1_1 = [
            [-r, 0, 0],  # c1dl
            [-r, h/3, 0], # c1ul
            [-r+r/3, h/3, 0] # c1rl
        ]
        c1_2 = [
            [r, 0, 0],  # c1dl
            [r, h/3, 0], # c1ul
            [r-r/3, h/3, 0] # c1rl
        ]

        c2_1 = [
            [-r+r/3, h/3, 0],  # c2dl
            [-r+r/3, 2*h/3, 0], # c2ul
            [-r+(2*r)/3, 2*h/3, 0] # c2rl
        ]
        c2_2 = [
            [r-r/3, h/3, 0],  # c2rl
            [r-r/3, 2*h/3, 0], # c2ul
            [r-(2*r)/3, 2*h/3, 0] # c2ll
        ]

        c3_1 = [
            [-r+(2*r)/3, 2*h/3, 0],  # c1dl
            [-r+(2*r)/3, h, 0], # c1ul
            [0, h, 0] # c1rl
        ]
        c3_2 = [
            [r-(2*r)/3, 2*h/3, 0],  # c1dl
            [r-(2*r)/3, h, 0], # c1ul
            [0, h, 0] # c1rl
        ]
        
        cyl1 = Union(Polygon(*c1_1, color=TEAL_A),Polygon(*c1_2, color=TEAL_A))
        cyl2 = Union(Polygon(*c2_1, color=TEAL_A),Polygon(*c2_2, color=TEAL_A))
        cyl3 = Union(Polygon(*c3_1, color=TEAL_A),Polygon(*c3_2, color=TEAL_A))

        cyl1.set_opacity(0.5)
        cyl2.set_opacity(0.5)
        cyl3.set_opacity(0.5)

        cyl1.shift(DOWN*h/2)
        cyl2.shift(DOWN*h/2)
        cyl3.shift(DOWN*h/2)

        self.play(FadeIn(cyl1),FadeIn(cyl2),FadeIn(cyl3),run_time=2)

        self.wait(1)
        term1 = Text("h = cone's height",font_size=30).shift(RIGHT*4.5)
        hel1 = Line((0,0,0),(0,h,0),color=WHITE,stroke_width=10).shift(DOWN*h/2)
        term2 = Text("r = cone's base radius",font_size=30).shift(RIGHT*4.5)
        brad = Line((0,0,0),(r,0,0),color=WHITE,stroke_width=10).shift(DOWN*h/2)
        term3 = Text("n = number of cylinders",font_size=30).shift(RIGHT*4.5 + DOWN)

        self.play(Write(term1),Write(hel1))
        self.play(Unwrite(hel1))

        self.wait(0.7)

        self.play(Write(term2),Write(brad),term1.animate.shift(UP))
        self.play(Unwrite(brad))

        self.wait(0.7)

        self.play(Write(term3))
        self.wait(1)

        self.play(Unwrite(term1),Unwrite(term2),Unwrite(term3))

        self.wait(1)

        brhc1 = BraceBetweenPoints([r, 0, 0],[r, h/3, 0],direction=RIGHT)
        brhc2 = BraceBetweenPoints([r-r/3, h/3, 0],[r-r/3, 2*h/3, 0],direction=RIGHT)
        brhc3 = BraceBetweenPoints([r-(2*r)/3, 2*h/3, 0],[r-(2*r)/3, h, 0],direction=RIGHT)

        brhc1.shift(DOWN*h/2)
        brhc2.shift(DOWN*h/2)
        brhc3.shift(DOWN*h/2)

        brhc1t = Tex(r"$\frac{h}{n}$").next_to(brhc1, RIGHT)
        brhc2t = Tex(r"$\frac{h}{n}$").next_to(brhc2, RIGHT)
        brhc3t = Tex(r"$\frac{h}{n}$").next_to(brhc3, RIGHT)

        self.play(GrowFromCenter(brhc1),GrowFromCenter(brhc2),GrowFromCenter(brhc3),Write(brhc1t),Write(brhc2t),Write(brhc3t))
        self.wait(1)
        self.play(FadeOut(brhc1),FadeOut(brhc2),FadeOut(brhc3),FadeOut(brhc1t),FadeOut(brhc2t),FadeOut(brhc3t))
        self.wait(1)

        d2 = DashedLine((-r+r/3, h/3, 0),(r-r/3, h/3, 0))
        d3 = DashedLine((-r+(2*r)/3, 2*h/3, 0),(r-(2*r)/3, 2*h/3, 0))
        d1 = DashedLine((-r,0,0),(r,0,0))

        d1.shift(DOWN*h/2)
        d2.shift(DOWN*h/2)
        d3.shift(DOWN*h/2)

        h1 = DashedLine((-r+r/3, h/3, 0),(-r+r/3,0,0))
        h2 = DashedLine((-r+(2*r)/3, 2*h/3, 0),(-r+(2*r)/3, h/3, 0))

        h1.shift(DOWN*h/2)
        h2.shift(DOWN*h/2)

        h4 = DashedLine((r-r/3, h/3, 0),(r-r/3,0,0))
        h5 = DashedLine((r-(2*r)/3, 2*h/3, 0),(r-(2*r)/3, h/3, 0))

        h4.shift(DOWN*h/2)
        h5.shift(DOWN*h/2)

        self.play(Create(d1),Create(d2),Create(d3),run_time=2)
        self.wait(1)

        self.play(Create(h1),Create(h2),Create(h4),Create(h5),run_time=2)
        self.wait(1)

        b1 = BraceBetweenPoints([-r,0,0],[-r+r/3,0,0],direction=UP)
        b2 = BraceBetweenPoints([r,0,0],[r-r/3,0,0],direction=UP)
        b3 = BraceBetweenPoints([-2*r/3,h/3,0],[-2*r/3+r/3,h/3,0],direction=UP)
        b4 = BraceBetweenPoints([2*r/3,h/3,0],[2*r/3 - r/3,h/3,0],direction=UP)
        b5 = BraceBetweenPoints([-r/3,2*h/3,0],[0,2*h/3,0],direction=UP)
        b6 = BraceBetweenPoints([r/3,2*h/3,0],[0,2*h/3,0],direction=UP)

        b1.shift(DOWN*h/2)
        b2.shift(DOWN*h/2)
        b3.shift(DOWN*h/2)
        b4.shift(DOWN*h/2)
        b5.shift(DOWN*h/2)
        b6.shift(DOWN*h/2)

        b1t = b1.get_text("a")
        b2t = b2.get_text("a")
        b3t = b3.get_text("a")
        b4t = b4.get_text("a")
        b5t = b5.get_text("a")
        b6t = b6.get_text("a")

        self.play(GrowFromCenter(b1),GrowFromCenter(b2),GrowFromCenter(b3),GrowFromCenter(b4),GrowFromCenter(b5),GrowFromCenter(b6))
        self.wait(1)

        self.play(Write(b1t),Write(b2t),Write(b3t),Write(b4t),Write(b5t),Write(b6t))
        self.wait(1)

        redl = Line((0,0,0),(r,0,0),color=RED,stroke_width=8)
        redl2 = Line((0, h/3, 0),(r-r/3, h/3, 0),color=RED,stroke_width=8)
        redl3 = Line((0, 2*h/3, 0),(r-(2*r)/3, 2*h/3, 0),color=RED,stroke_width=8)

        redl.shift(DOWN*h/2)
        redl2.shift(DOWN*h/2)
        redl3.shift(DOWN*h/2)

        text1 = Tex(r"$L(\text{red line}) = r$",font_size=40).shift(RIGHT*4.5)
        text2 = Tex(r"$L(\text{red line}) = r-a$",font_size=40).shift(RIGHT*4.5)
        text3 = Tex(r"$L(\text{red line}) = r-2a$",font_size=40).shift(RIGHT*4.5)

        self.play(Create(redl),Write(text1))
        self.wait(1)
        self.play(Transform(redl,redl2),Transform(text1,text2))
        self.wait(1)
        self.play(Transform(redl,redl3),Transform(text1,text3))
        self.wait(1)
        self.play(FadeOut(redl),FadeOut(text1))
        self.wait(1)

        text1 = Tex(r"$L(\text{red line}) = r$",font_size=40).shift(RIGHT*4.5)

        text1.shift(UP)
        text3.shift(DOWN)
        self.play(FadeIn(text1),FadeIn(text2),FadeIn(text3))
        self.wait(1)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text3))
        self.wait(1)



        height = DashedLine((0,h,0),(0, 0, 0))
        br = BraceBetweenPoints([-r,h/7,0],[0,h/7,0],direction=UP)

        height.shift(DOWN*h/2)
        br.shift(DOWN*h/2)

        brt = br.get_text("r")

        self.play(Create(height),GrowFromCenter(br),Write(brt))
        self.wait(1)

        

        purpl1 = Line([-r,0,0],[-r+r/3,0,0],color=PURPLE_C,stroke_width=8)
        purpl2 = Line([-2*r/3,h/3,0],[-2*r/3+r/3,h/3,0],color=PURPLE_C,stroke_width=8)
        purpl3 = Line([-r/3,2*h/3,0],[0,2*h/3,0],color=PURPLE_C,stroke_width=8)

        purpl1.shift(DOWN*h/2)
        purpl2.shift(DOWN*h/2)
        purpl3.shift(DOWN*h/2)

        self.play(Create(purpl1),Create(purpl2),Create(purpl3))
        self.wait(0.7)
        self.play(purpl2.animate.shift(DOWN*h/3),purpl3.animate.shift(DOWN*2*h/3))
        self.wait(0.7)

        sumeq = Tex(r"$\overbrace{a + a + a + ...}^\text{n terms} = r$",font_size=40).shift(RIGHT*4.5)
        self.play(Write(sumeq))
        self.wait(1)
        sumeq2 = Tex(r"$\implies na = r$",font_size=40).shift(RIGHT*4.5 + DOWN)
        self.play(Write(sumeq2))
        self.wait(1)
        self.play(FadeOut(purpl1),FadeOut(purpl2),FadeOut(purpl3),FadeOut(sumeq),FadeOut(sumeq2))
        self.wait(1)
        final = Tex(r"$\implies a = \frac{r}{n}$",font_size=40).shift(RIGHT*4.5)
        highlightf = BackgroundRectangle(final, color=RED, fill_opacity=0.17)
        self.play(FadeIn(final),FadeIn(highlightf))
        self.wait(1)
        self.play(FadeOut(final),FadeOut(highlightf),FadeOut(d1),FadeOut(d2),FadeOut(d3),FadeOut(h1),FadeOut(h2),FadeOut(h4),FadeOut(h5),FadeOut(b1),FadeOut(b1t),FadeOut(b2),FadeOut(b2t),FadeOut(b3),FadeOut(b3t),FadeOut(b4),FadeOut(b4t),FadeOut(b5),FadeOut(b5t),FadeOut(b6),FadeOut(b6t),FadeOut(height),FadeOut(br),FadeOut(brt))
        self.wait(1)



class SceneSix(Scene):
    def construct(self):
        h=7.5
        r=3

        position_list = [
            [0, h, 0],  # top
            [-r, 0, 0],  # bottom right
            [r, 0, 0],  # bottom left
        ]
        triangle = Polygon(*position_list, color=TEAL_E)
        triangle.set_opacity(0.6)
        triangle.move_to([0,0,0])

        self.add(triangle)

        c1_1 = [
            [-r, 0, 0],  # c1dl
            [-r, h/3, 0], # c1ul
            [-r+r/3, h/3, 0] # c1rl
        ]
        c1_2 = [
            [r, 0, 0],  # c1dl
            [r, h/3, 0], # c1ul
            [r-r/3, h/3, 0] # c1rl
        ]

        c2_1 = [
            [-r+r/3, h/3, 0],  # c2dl
            [-r+r/3, 2*h/3, 0], # c2ul
            [-r+(2*r)/3, 2*h/3, 0] # c2rl
        ]
        c2_2 = [
            [r-r/3, h/3, 0],  # c2rl
            [r-r/3, 2*h/3, 0], # c2ul
            [r-(2*r)/3, 2*h/3, 0] # c2ll
        ]

        c3_1 = [
            [-r+(2*r)/3, 2*h/3, 0],  # c1dl
            [-r+(2*r)/3, h, 0], # c1ul
            [0, h, 0] # c1rl
        ]
        c3_2 = [
            [r-(2*r)/3, 2*h/3, 0],  # c1dl
            [r-(2*r)/3, h, 0], # c1ul
            [0, h, 0] # c1rl
        ]
        
        cyl1 = Union(Polygon(*c1_1, color=TEAL_A),Polygon(*c1_2, color=TEAL_A))
        cyl2 = Union(Polygon(*c2_1, color=TEAL_A),Polygon(*c2_2, color=TEAL_A))
        cyl3 = Union(Polygon(*c3_1, color=TEAL_A),Polygon(*c3_2, color=TEAL_A))

        cyl1.set_opacity(0.5)
        cyl2.set_opacity(0.5)
        cyl3.set_opacity(0.5)

        cyl1.shift(DOWN*h/2)
        cyl2.shift(DOWN*h/2)
        cyl3.shift(DOWN*h/2)

        self.add(cyl1,cyl2,cyl3)

        

        self.wait(1)
        diag = Group(triangle,cyl1,cyl2,cyl3)
        self.play(diag.animate.shift(LEFT*3.7))
        self.wait(1)

        place11 = Tex(r"$V(1^{\text{st}} cylinder) = h_1 \pi r^2$").shift(RIGHT*3 + UP*3/2)
        place21 = Tex(r"$V(2^{\text{nd}} cylinder) = h_2 \pi (r-a)^2$").shift(RIGHT*3 + UP*1/2)
        place31 = Tex(r"$V(3^{\text{rd}} cylinder) = h_3 \pi (r-2a)^2$").shift(RIGHT*3 + DOWN*1/2)
        dotdotdot = Tex(r"...").shift(RIGHT*3 + DOWN*3/2)

        C1 = Polygon([-r, 0 ,0], [r, 0, 0],[r,h/3,0],[-r,h/3,0],color=WHITE,stroke_width=7)
        C2 = Polygon([-r+r/3,h/3,0],[r-r/3,h/3,0],[r-r/3,2*h/3,0],[-r+r/3,2*h/3,0],color=WHITE,stroke_width=7)
        C3 = Polygon([-r+2*r/3,2*h/3,0],[r-2*r/3,2*h/3,0],[r-2*r/3,h,0],[-r+2*r/3,h,0],color=WHITE,stroke_width=7)
        C1.shift(DOWN*h/2 + LEFT*3.7)
        C2.shift(DOWN*h/2 + LEFT*3.7)
        C3.shift(DOWN*h/2 + LEFT*3.7)

        self.play(Create(C1),Write(place11))
        self.play(Uncreate(C1))

        self.wait(1)

        self.play(Create(C2),Write(place21))
        self.play(Uncreate(C2))

        self.wait(1)

        self.play(Create(C3),Write(place31))
        self.play(Uncreate(C3))

        self.wait(1)

        def approxer(n,group1,group2):
            for x in range(n):
                t1 = Polygon([-r+(x*r/n),x*h/n,0],[-r+(x*r/n),(x+1)*h/n,0],[-r+(x+1)*r/n,(x+1)*h/n,0],color=TEAL_A).set_opacity(0.5)
                t2 = Polygon([r-(x*r/n),x*h/n,0],[r-(x*r/n),(x+1)*h/n,0],[r-(x+1)*r/n,(x+1)*h/n,0],color=TEAL_A).set_opacity(0.5)
                t1.shift(DOWN*h/2 + LEFT*3.7)
                t2.shift(DOWN*h/2 + LEFT*3.7)
                group1.add(t1)
                group2.add(t2)

        origl = Group(Polygon(*c1_1, color=TEAL_A),Polygon(*c2_1, color=TEAL_A),Polygon(*c3_1, color=TEAL_A))
        origr = Group(Polygon(*c1_2, color=TEAL_A),Polygon(*c2_2, color=TEAL_A),Polygon(*c3_2, color=TEAL_A))
        origl.shift(DOWN*h/2 + LEFT*3.7)
        origr.shift(DOWN*h/2 + LEFT*3.7)
        self.add(origl)
        self.add(origr)
        self.remove(cyl1,cyl2,cyl3)

        phase2l = Group()
        phase2r = Group()
        approxer(6,phase2l,phase2r)

        phase3l = Group()
        phase3r = Group()
        approxer(12,phase3l,phase3r)

        phase4l = Group()
        phase4r = Group()
        approxer(24,phase4l,phase4r)

        phase5l = Group()
        phase5r = Group()
        approxer(48,phase5l,phase5r)

        phase6l = Group()
        phase6r = Group()
        approxer(96,phase6l,phase6r)

        self.play(Transform(origl,phase2l),Transform(origr,phase2r))
        self.wait(0.7)
        self.play(Transform(origl,phase3l),Transform(origr,phase3r))
        self.wait(0.7)
        self.play(Transform(origl,phase4l),Transform(origr,phase4r))
        self.wait(0.7)
        self.play(Transform(origl,phase5l),Transform(origr,phase5r))
        self.wait(0.7)
        self.play(Transform(origl,phase6l),Transform(origr,phase6r))
        self.wait(0.7)
        self.play(FadeIn(dotdotdot))
        self.wait(1)
        self.play(FadeOut(origl),FadeOut(origr),run_time=0.6)
        self.play(triangle.animate.shift(LEFT*10),place11.animate.shift(LEFT*3),place21.animate.shift(LEFT*3),place31.animate.shift(LEFT*3),dotdotdot.animate.shift(LEFT*3))

        place12 =Tex(r"$V(1^{\text{st}} cylinder) = \frac{h}{n} \pi r^2$").shift(UP*3/2)
        place22 =Tex(r"$V(2^{\text{nd}} cylinder) = \frac{h}{n} \pi \left(r-\frac{r}{n}\right)^2$").shift(UP*1/2)
        place32 =Tex(r"$V(3^{\text{rd}} cylinder) = \frac{h}{n} \pi \left(r-2\frac{r}{n}\right)^2$").shift(DOWN*1/2)

        self.play(Transform(place11,place12),Transform(place21,place22),Transform(place31,place32))

        self.wait(1)

class SceneSeven(Scene):
    def construct(self):

        place12 =Tex(r"$V(1^{\text{st}} cylinder) = \frac{h}{n} \pi r^2$").shift(UP*3/2)
        place22 =Tex(r"$V(2^{\text{nd}} cylinder) = \frac{h}{n} \pi \left(r-\frac{r}{n}\right)^2$").shift(UP*1/2)
        place32 =Tex(r"$V(3^{\text{rd}} cylinder) = \frac{h}{n} \pi \left(r-2\frac{r}{n}\right)^2$").shift(DOWN*1/2)
        dotdot = Tex(r"...").shift(DOWN*3/2)

        self.add(place12,place22,place32,dotdot)

        place13 =Tex(r"$V(1^{\text{st}} cylinder) = \frac{h}{n} \pi r^2$").shift(UP*3/2)
        place23 =Tex(r"$V(2^{\text{nd}} cylinder) = \frac{h}{n} \pi \left(r\left(1-\frac{1}{n}\right)\right)^2$").shift(UP*1/2)
        place33 =Tex(r"$V(3^{\text{rd}} cylinder) = \frac{h}{n} \pi \left(r\left(1-\frac{2}{n}\right)\right)^2$").shift(DOWN*1/2)

        self.wait(1)

        self.play(Transform(place12,place13),Transform(place22,place23),Transform(place32,place33))

        self.wait(1)

        place14 =Tex(r"$V(1^{\text{st}} cylinder) = \frac{h}{n} \pi r^2$").shift(UP*3/2)
        place24 =Tex(r"$V(2^{\text{nd}} cylinder) = \frac{h}{n} \pi r^2\left(1-\frac{1}{n}\right)^2$").shift(UP*1/2)
        place34 =Tex(r"$V(3^{\text{rd}} cylinder) = \frac{h}{n} \pi r^2\left(1-\frac{2}{n}\right)^2$").shift(DOWN*1/2)

        self.wait(1)
        self.play(Transform(place12,place14),Transform(place22,place24),Transform(place32,place34))
        self.wait(1)
        self.play(place12.animate.shift(LEFT*20),place22.animate.shift(LEFT*20),place32.animate.shift(LEFT*20),dotdot.animate.shift(LEFT*20))

        next =Tex(r"$V(total) = \overbrace{\left(\frac{h}{n} \pi r^2) + \left(\frac{h}{n} \pi r^2\left(1-\frac{1}{n})^2\right) + \left(\frac{h}{n} \pi r^2(1-\frac{2}{n}\right)^2\right) + ...}^\text{n terms}$").shift(UP*3)

        self.play(Write(next))

        self.wait(1)

        next2 = Tex(r"$V(total) = \frac{h}{n} \pi r^2 \overbrace{\left(1 + \left(1-\frac{1}{n}\right)^2 + \left(1-\frac{2}{n}\right)^2 + ...\right)}^\text{n terms}$")

        self.play(Write(next2))
        self.wait(1)

        next3 = Tex(r"$V(total) = h \pi r^2 \overbrace{\left(\frac{1 + \left(1-\frac{1}{n}\right)^2 + \left(1-\frac{2}{n}\right)^2 + ...}{n}\right)}^\text{n terms}$").shift(DOWN*3)

        self.play(Write(next3))
        self.wait(1)

        self.play(next.animate.shift(DOWN*20),next2.animate.shift(DOWN*20),next3.animate.shift(DOWN*20))
        self.wait(1)

class SceneEight(Scene):
    def construct(self):
        series1 = Tex(r"$\left(\frac{1 + \left(1-\frac{1}{n}\right)^2 + \left(1-\frac{2}{n}\right)^2 + \left(1-\frac{3}{n}\right)^2 + ...}{n}\right)$").shift(UP*3)
        series2 = Tex(r"$\left(1 + \left(1-\frac{1}{n}\right)^2 + \left(1-\frac{2}{n}\right)^2 + \left(1-\frac{3}{n}\right)^2 + ...\right)$")
        series3 = Tex(r"$=\left(1 + \left(1-\frac{1}{n}\right)^2 + \left(1-\frac{2}{n}\right)^2 + \left(1-\frac{3}{n}\right)^2 + ...\right)$").shift(DOWN*3)
        self.play(Write(series1))
        self.wait(0.7)
        self.play(Write(series2))
        self.wait(0.7)
        self.play(Write(series3))
        self.wait(1)
        # shift above text to left
        self.play(Group(series1,series2,series3).animate.shift(LEFT*20))
        self.wait(1)
        #bring below text from down
        series4 = Tex(r"$\left(1-\frac{x}{n}\right)^2$").shift(UP*21)
        series5 = Tex(r"$=1 -2\frac{x}{n} + \frac{x^2}{n^2}$").shift(UP*19)
        self.play(series4.animate.shift(DOWN*20))
        self.wait(0.7)
        self.play(series5.animate.shift(DOWN*20))
        self.wait(1)
        #move above text up
        self.play(Group(series4,series5).animate.shift(UP*20))
        self.wait(1)
        #bring below text from left
        series6 = Tex(r"$\overbrace{1+1+1+...}^\text{n terms} + \overbrace{-2\frac{1}{n} + -2\frac{2}{n} + ...}^\text{n-1 terms} + \overbrace{\frac{1^2}{n} + \frac{2^2}{n} + ...}^\text{n-1 terms}$",font_size=30).shift(LEFT*20 + UP*3.2)
        series7 = Tex(r"$=(n) + [-\frac{2}{n}\overbrace{(1+2+3+...)}^\text{n-1 terms}] + [\frac{1}{n^2}\overbrace{(1^2+2^2+3^2+...)}^\text{n-1 terms}]$",font_size=30).shift(LEFT*20 + UP*0.8)
        naturalsum = Tex(r"$\overbrace{1 + 2 + 3 + ...}^\text{x terms} = \frac{x(x+1)}{2}$",font_size=25).shift(UP*3.6 + LEFT* 5)
        series8 = Tex(r"$=(n) + -\frac{2}{n}\frac{(n-1)(n)}{2} + [\frac{1}{n^2}\overbrace{(1^2+2^2+3^2+...)}^\text{n-1 terms}]$",font_size=30).shift(LEFT*20+DOWN*0.8)
        squaresum = Tex(r"$\overbrace{1^2 + 2^2 + 3^2 + ...}^\text{x terms} = \frac{x(x+1)(2x+1)}{6}$",font_size=25).shift(UP*3.6 + LEFT* 5)
        series9 = Tex(r"$=(n) + -\frac{2}{n}\frac{(n-1)(n)}{2} + \frac{1}{n^2}\frac{(n-1)(n)(2n-1)}{6}$",font_size=30).shift(LEFT*20+ DOWN*3.2)
        series10 = Tex(r"$=(n) + -(n-1) + \frac{n}{3} + \frac{1}{6n} - \frac{1}{2}$",font_size=30).shift(LEFT*20+ UP*3.2)
        series11 = Tex(r"$=1 + \frac{n}{3} + \frac{1}{6n} - \frac{1}{2}$",font_size=30).shift(LEFT*20+ UP*0.8)
        series12 = Tex(r"$=\frac{1 + \frac{n}{3} + \frac{1}{6n} - \frac{1}{2}}{n}$",font_size=30).shift(LEFT*20+ DOWN*0.8)
        series13 = Tex(r"$=\frac{1}{3} + \frac{1}{2n} + \frac{1}{6n^2}$",font_size=30).shift(LEFT*20+ DOWN*3.2)
        self.play(series6.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(series7.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(Write(naturalsum))
        self.wait(0.7)
        self.play(series8.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(Unwrite(naturalsum))
        self.wait(0.7)
        self.play(Write(squaresum))
        self.wait(0.7)
        self.play(series9.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(Unwrite(squaresum))
        self.wait(0.7)
        self.play(Group(series6,series7,series8,series9,squaresum).animate.shift(UP*20))
        self.wait(1)
        self.play(series10.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(series11.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(series12.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(series13.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(Group(series10,series11,series12,series13).animate.shift(UP*20))
        self.wait(1)
        #move text up
        #VIDEO EDITING BRING CYLINDER LIMITING VIDEO BACK
        #MOVE IT BACK DOWN

##############################################################################
class SceneNine(ThreeDScene):
    def construct(self):
        
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        prompt1 = Tex(r"$n=1$").shift(DOWN*30+UP*3+LEFT*3)
        prompt2 = Tex(r"$n=2$").shift(UP*3+LEFT*3)
        prompt3 = Tex(r"$n=4$").shift(UP*3+LEFT*3)
        prompt4 = Tex(r"$n=8$").shift(UP*3+LEFT*3)
        self.add_fixed_in_frame_mobjects(prompt1)

        def approxer(approxe,n):
            for y in range(n):
                cyl = Cylinder(radius=r*(1-(y/n)), height=h/n, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((0,0,(h/n)*y-(h/2 - (0.5)*(h/n))))
                approxe.add(cyl)
            return

        approx1 = VGroup()
        approxer(approx1,1)

        approx2 = VGroup()
        approxer(approx2,2)

        approx3 = VGroup()
        approxer(approx3,4)

        approx4 = VGroup()
        approxer(approx4,8)

        self.play(prompt1.animate.shift(UP*30))

        self.play(Write(approx1),run_time=0.5)
        self.wait(1)
        self.play(Transform(approx1,approx2),Transform(prompt1,prompt2),run_time=0.5)
        self.wait(1)
        self.play(Transform(approx1,approx3),Transform(prompt1,prompt3),run_time=0.5)
        self.wait(1)
        self.play(Transform(approx1,approx4),Transform(prompt1,prompt4),run_time=0.5)
        self.wait(0.5)

class SceneNinePartOne(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        prompt1 = Tex(r"$n=8$").shift(UP*3+LEFT*3)
        prompt2 = Tex(r"$n=14$").shift(UP*3+LEFT*3)
        prompt3 = Tex(r"$n=20$").shift(UP*3+LEFT*3)
        self.add_fixed_in_frame_mobjects(prompt1)

        def approxer(approxe,n):
            for y in range(n):
                cyl = Cylinder(radius=r*(1-(y/n)), height=h/n, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((0,0,(h/n)*y-(h/2 - (0.5)*(h/n))))
                approxe.add(cyl)
            return

        approx4 = VGroup()
        approxer(approx4,8)
        self.add(approx4)

        approx5 = VGroup()
        approxer(approx5,14)

        approx6 = VGroup()
        approxer(approx6,20)

        self.wait(0.5)

        self.add(approx4)
        self.wait(1)
        self.play(Transform(approx4,approx5),Transform(prompt1,prompt2),run_time=0.5)
        self.wait(1)
        self.play(Transform(approx4,approx6),Transform(prompt1,prompt3),run_time=0.5)
        self.wait(0.5)

class SceneNinePartTwo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        prompt1 = Tex(r"$n=20$").shift(UP*3+LEFT*3)
        prompt2 = Tex(r"$\lim_{n\to\infty} n$").shift(UP*3+LEFT*3)
        prompt2.set_opacity(0)
        self.add_fixed_in_frame_mobjects(prompt1)
        self.add_fixed_in_frame_mobjects(prompt2)

        def approxer(approxe,n):
            for y in range(n):
                cyl = Cylinder(radius=r*(1-(y/n)), height=h/n, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((0,0,(h/n)*y-(h/2 - (0.5)*(h/n))))
                approxe.add(cyl)
            return

        approx6 = VGroup()
        approxer(approx6,20)
        self.add(approx6)

        cone = Cone(base_radius=r, height=h, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0).move_to((0,0,0))

        self.wait(0.5)

        self.wait(1)
        self.play(FadeOut(approx6),FadeIn(cone),prompt1.animate.set_opacity(0),prompt2.animate.set_opacity(1),run_time=1)
        self.wait(1)
        self.play(FadeOut(cone),FadeOut(prompt2))
        self.wait(1)
################################################################################################################

class SceneTen(Scene):
    def construct(self):
        #bring text from up
        series14 = Tex(r"$\lim_{n\to\infty} \frac{1}{3} + \frac{1}{2n} + \frac{1}{6n^2}$").shift(UP*20 + UP*2)
        series15 = Tex(r"$= \frac{1}{3} + 0 + 0$").shift(UP*20)
        series16 = Tex(r"$= \frac{1}{3}$").shift(UP*20+ DOWN*2)

        self.play(series14.animate.shift(DOWN*20))
        self.wait(0.7)
        self.play(series15.animate.shift(DOWN*20))
        self.wait(0.7)
        self.play(series16.animate.shift(DOWN*20))
        self.wait(1)
        self.play(Group(series14,series15,series16).animate.shift(DOWN*20))
        self.wait(1)
        # move above text down
        series17 = Tex(r"$V(total) = h \pi r^2 \left(\frac{1 + \left(1-\frac{1}{n}\right)^2 + \left(1-\frac{2}{n}\right)^2 + ...}{n}\right)$").shift(LEFT*20 + UP*3.2)
        series18 = Tex(r"$\lim_{n\to\infty} V(total) = \lim_{n\to\infty} h \pi r^2 \left(\frac{1 + \left(1-\frac{1}{n}\right)^2 + \left(1-\frac{2}{n}\right)^2 + ...}{n}\right)$").shift(LEFT*20 + UP*0.8)
        series19 = Tex(r"$\lim_{n\to\infty} V(total) = h \pi r^2 \frac{1}{3}$").shift(LEFT*20 + DOWN*0.8)
        series20 = Tex(r"$V(cone) = \frac{1}{3} h \pi r^2$").shift(LEFT*20 + DOWN*3.2)

        self.play(series17.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(series18.animate.shift(RIGHT*20))
        self.wait(0.7)
        self.play(series19.animate.shift(RIGHT*20))
        self.wait(1)
        self.play(series20.animate.shift(RIGHT*20))
        self.wait(1)
        self.play(Group(series17,series18,series19,series20).animate.shift(RIGHT*20))
        self.wait(1)


class SceneEnd(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.5)

        h=7.5
        r=3

        cone = Cone(base_radius=r, height=h, fill_opacity=1, fill_color=GREEN,resolution=(15, 15), stroke_opacity=0).move_to((0,0,0))

        self.wait(1)
        self.play(Write(cone), run_time=2)
        def rotatec(obj,dt):
            obj.rotate(10*dt*DEGREES,about_point=obj.get_center())
        cone.add_updater(rotatec)
        self.wait(1)

        #self.play(cone.animate.rotate(angle=15*DEGREES,axis=[1.,0.,0.],about_point=[0,0,0]),run_time=0.1)


        equal = Tex(r"$= \frac{1}{3}h\pi r^2$   ").set_opacity(0)
        self.add_fixed_in_frame_mobjects(equal)

        self.play(cone.animate.shift(RIGHT*4),equal.animate.set_opacity(1)) # right and left are inverted

        self.wait(8)

        self.play(cone.animate.shift(IN*20),equal.animate.set_opacity(0))

        self.wait(1)

        sphere = Sphere(radius=r, fill_opacity=1,resolution=(15, 15), stroke_opacity=0).shift(OUT*20)
        sphere.set_color(GREEN)

        self.play(sphere.animate.move_to([0,0,0]))
        sphere.add_updater(rotatec)

        self.wait(1)

        equal2 = Tex(r"\hspace{50 pt}$= $ ?").set_opacity(0)
        self.add_fixed_in_frame_mobjects(equal2)

        self.play(sphere.animate.shift(RIGHT*4),equal2.animate.set_opacity(1))

        self.wait(8)

class SceneQues(Scene):
    def construct(self):
        self.wait(1)
        text = Tex("?",font_size=180)
        self.play(Write(text))
        self.wait(1)
        self.play(Unwrite(text))
        self.wait(1)

class Thumbnail(ThreeDScene):
    def construct(self):
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        self.set_camera_orientation(phi=PI/2, theta=PI/2,zoom=0.4)

        h=7.5
        r=3

        cone1 = Cone(base_radius=r, height=h, fill_opacity=0.5, fill_color=RED,resolution=(15, 15), stroke_opacity=0).move_to((-r-1/2,0,0))
        cone2 = cone1.copy().move_to((1/2+r,0,0))
        cone2.set_color(GREEN)
        cone3 = cone1.copy().move_to((3*r+3/2,0,0))
        cone3.set_color(BLUE)

        cyl = Cylinder(radius=r, height=h, fill_opacity=0.5, fill_color=WHITE,resolution=(15, 15), stroke_opacity=0,checkerboard_colors=False).move_to((-3*r-3/2,0,0))

        self.add(cone1,cone2,cone3,cyl)

        equal1 = Tex(r"$+$ ").move_to((0,0,0))
        equal2 = Tex(r"$+$").move_to((-r+1/5,0,0))
        equal3 = Tex(r"$=$").move_to((r-1/2,0,0))

        self.add_fixed_in_frame_mobjects(equal1,equal2,equal3)

        