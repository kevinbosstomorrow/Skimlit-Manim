'''  
reference: https://github.com/Ackeraa/snake/blob/main/movie/main.py
manim -pqh manim4.py Main
'''

import itertools as it

from manim import *
import random





colors = ['#80ff9e', '#f0ff80', '#f0ff80', '#9eff80', '#80ffe3', '#97ff80', '#80f2ff', '#aa80ff', '#e680ff', '#ff80c8']


# get neural network |  color = np.random.choice(colors)
def get_nn(struct, circle_size, stroke_size, col):
    nn = VGroup()
    nn_edges = VGroup()
    for i in range(len(struct)):
        nn.add(VGroup(*[Circle(circle_size, color=col, stroke_width=stroke_size) for _ in range(struct[i])]).arrange(DOWN, buff=0.1)).arrange(RIGHT, 1)
    
    for l1, l2 in zip(nn[:-1], nn[1:]):
        for n1, n2 in it.product(l1, l2):
            edge = Line(n1.get_right(),n2.get_left(),stroke_width = 0.3, color = np.random.choice(colors)) 
            nn_edges.add(edge)
    nn.add(nn_edges)
    
    return nn


# the size of one single matrix, the number of vector matrix, the number of matrix (一个单独的方块， 一排， n个一排)
def get_matrix(scalar_size, vector_size, matrix_size, stroke_size, col):
    scaler = VGroup(*[Square(scalar_size, stroke_width=stroke_size).set_color(col) for _ in range(vector_size)]).arrange(RIGHT, buff=0)
    matrix = VGroup(*[scaler.copy() for _ in range(matrix_size)]).arrange(DOWN, buff=0)
    return matrix


def get_rectangle(scalar_height, scalar_width, vector_size, matrix_size, stroke_size, col):
    scaler = VGroup(*[Rectangle(height = scalar_height, width = scalar_width, stroke_width = stroke_size).set_color(col) for _ in range(vector_size)]).arrange(RIGHT, buff=0)
    matrix = VGroup(*[scaler.copy() for _ in range(matrix_size)]).arrange(DOWN, buff=0)

    for n in range(len(matrix)):
        if n % 2 == 0:
            matrix[n].set_fill(GREY_A , opacity=1)
        else:
            matrix[n].set_fill(WHITE, opacity=1)
    return matrix

def get_rectangle_nocolor(scalar_height, scalar_width, vector_size, matrix_size, col):
    scaler = VGroup(*[Rectangle(height = scalar_height, width = scalar_width).set_color(col) for _ in range(vector_size)]).arrange(RIGHT, buff=0)
    matrix = VGroup(*[scaler.copy() for _ in range(matrix_size)]).arrange(DOWN, buff=0)
    return matrix


def get_ai(number, ai_per_row):
    population = VGroup()
    for i in range(number):
        #population.add(Individual(happy=random.random()>0.5).scale(0.2))  
        headcolor = random.choice(colors)
        head = Circle(stroke_width=2).set_color(headcolor).scale(0.7).set_fill(headcolor, opacity=0.5)
        
        # 两个圆眼睛
        eyecolor = random.choice(colors)
        eyes = VGroup(Circle(stroke_width=1, color = eyecolor),
                        Circle(stroke_width=1, color = eyecolor)).arrange(RIGHT, buff=0.6).set_fill(random.choice(colors), opacity=0.5).scale(0.2).shift(UP*0.2)

        # A I in the eye
        txt =  VGroup(Text('A'), Text('I')).arrange(RIGHT, buff=0.60).set_fill(random.choice(colors), opacity=1).scale(0.6).shift(UP*0.2)
        
        # 嘴， 半圆， 分开心和不开心 angle=PI 是不开心
        happy_face = Arc(stroke_width=1, angle=PI).scale(0.2).shift(DOWN*0.8).set_color(eyecolor).rotate(angle = 3.15)
        sad_face = Arc(stroke_width=1, angle=PI).scale(0.2).shift(DOWN*0.7).set_color(eyecolor)

        # VGroup的作用就是把所有的 parts 装到一起
        AI = VGroup(head, eyes, txt, happy_face).scale(0.6)
        
        population.add(AI)

    population.arrange_in_grid(rows=ai_per_row).shift(UP*0.5)
    return population


def display_code(code):
    return Code(code,
                font_size=12,
                tab_width=4,
                background="rectangle",
                insert_line_no=False,
                style=Code.styles_list[14],
                font="Monospace",
                background_stroke_color=BLUE_A,
                language="Python",
                line_spacing=0.5,
                margin=0.2)



def decomposition_one_hundred(n, total):
    """ n split & input number """

    dividers = sorted(random.sample(range(1, total), n - 1))
    return [(a - b)/100 for a, b in zip(dividers + [total], [0] + dividers)]



class Main(Scene):
    def construct(self):
    
        #self.create_population()
        #self.create_Genes()
        #self.vanishing_population()
        self.code_display()
    
    def create_population(self):
        population = get_ai(25,5)

        # 可以同时把2个object 丢到一起play
        self.play(FadeIn(population))
      
        # animate 的作用就是和 applyMethod 一样的 体现了一个 做移动+缩小的动作 
        self.play(population.animate.shift(LEFT*5.5).scale(0.5))
    

        # 把object 从 population[i] 里面转到 individuals里面 直接用add就可以拿出来， 以后抽奖也可以用这种动画 
        '''
        individuals = VGroup()
        for i in range(m):
            if i == m // 2:
                individuals.add(Text('....').scale(1))
            else:
                individuals.add(population[i]).scale(1)
        individuals.arrange(DOWN, buff=0.1)
        self.play(Create(individuals, run_time = 2))
        
        
        for i in range(m):
            individual = VGroup()
            individual.add(population[i]).scale(2)
            self.play(Create(individual.shift([i+3,0,0]), run_time = 0.5))
        
        arr = VGroup()
        #dot = Dot().move_to(population[14])
        arr.add(Arrow(start=population[14], end=individual, stroke_width=1.5,max_tip_length_to_length_ratio=0.05, color=GRAY_B))
        self.play(FadeIn(arr), FadeIn(individual))
        '''

        
    def create_Genes(self):

        '''创建基因 也就是向下的格子'''
        # Genes.
        n = 5
        v = [round(random.random(),3) for _ in range(n)]
        v[n//2] = '...'
        size = 0.6
        
        #  直接生成5个向下排列的格子
        #p = VGroup(*[Square(size, stroke_width=3, color = WHITE) for _ in range(n)]).arrange(DOWN, buff=0)
        p = get_matrix(1, 1, 5, 1, WHITE)

        # 然后把每个格子里面都装上数字
        t= VGroup(*[Text(str(v[i])).scale(size/2).move_to(p[i].get_center())  for i in range(len(v))])  
        p.add(t)
        p.shift(RIGHT*4)
        self.play(Create(p))
        self.play(FadeOut(p))
    
        '''创建神经网络'''
        nns = get_nn([5, 6, 8, 4], 0.06, 1.5, WHITE)
        nns.shift(LEFT * 4)
        self.play(FadeIn(nns))
        #self.play(FadeOut(nns))
        #nna = nns.copy()
        #nna.shift(RIGHT * 4)
        #self.play(FadeIn(nna))
        #self.play(Transform(p, nns), run_time = 2)


        '''创建Game'''
        #matrix = get_matrix(10, 0.7, GRAY, stroke_width=1).scale(0.2)   
        mm = get_matrix(1, 10, 10, 1, WHITE).scale(0.2)
        mm[5][5].set_fill(WHITE, opacity=1)
        mm[5][6].set_fill(PURE_BLUE, opacity=1)
        mm[4][6].set_fill(PURE_BLUE, opacity=1)
        mm[2][2].set_fill(PURE_RED, opacity=1)
        mm.shift(RIGHT * 2)
        self.play(FadeIn(mm))



        '''在matrix和神经网络之间做 弧型箭头'''
        dot1 = Dot().move_to(nns).shift(RIGHT*0.5+DOWN*0.3)
        dot2 = Dot().move_to(mm).shift(LEFT*0.6+DOWN*0.3)
        ar = CurvedArrow(start_point=[dot1.get_x(), dot1.get_y(), 0],end_point=[dot2.get_x(), dot2.get_y(), 0],stroke_width=1.5, color=GRAY_B).scale(0.25)

 
        ar1 = CurvedArrow(start_point=[dot2.get_x(), dot2.get_y(), 0], end_point=[dot1.get_x(), dot1.get_y(), 0],stroke_width=1.5, color=GRAY_B).scale(0.25).shift(DOWN*0.5)
        arr2 = VGroup()
        arr2.add(ar, ar1)
        self.play(FadeIn(arr2))



        # Show passing flash.  copy() 加上之后 看起来就是只是传递光源但是 没有消失 和下面的对比就能发现不同
        run_time = 1
        for _ in range(2):
            self.play(ShowPassingFlash(arr2[1].copy().set_color(BLUE_E),run_time=run_time,time_width=run_time))
            self.play(ShowPassingFlash(arr2[0].set_color(RED_E),run_time=run_time,time_width=run_time))

            self.play(MathTex("f(score, steps)").scale(0.4).next_to(mm, RIGHT))

        

    def vanishing_population(self):

        # make AI population
        population2 = get_ai(30,6)
        population2.shift([2,0,0])
        self.play(FadeIn(population2))
        self.play(population2.animate.shift(LEFT*5).scale(0.5))


        # random disappear some of the AI  30个AI机器人里面选16个消失
        die_ai = random.sample(list(range(30)),16)
        run_time = 1

        # fadeout one by one
        '''
        for x in die_ai:
            self.play(FadeOut(population2[x]), run_time=run_time)
            run_time -= 0.05
        '''

        # 同时fadeout
        self.play(FadeOut(population2[0]),FadeOut(population2[1]),FadeOut(population2[12]), run_time=1)

        # 从不同的AI里面组合不同的部位
        self.play(population2[2][0].animate.shift([3,0,0]), 
                  population2[3][1].animate.shift([2,0,0]),
                  population2[-1][2].animate.shift([3,0,0]))


    def code_display(self):
        code1 = display_code("code1.py")
                  
        self.play(FadeIn(code1))

        
        self.play(Wiggle(code1[-1]))

        self.play(FadeOut(code1.code[8:], shift=DOWN))
        '''
        lines = [1,3,5,7,9]
        arr = CodeArr(code1, lines[0])
        self.play(FadeIn(arr))


        for i in range(len(lines)):
            self.play(arr.move(lines[i]))
            self.wait(1.5)


        '''
        lines = [8, 11, 14, 19, 22]
        #arr = CodeArr(code, lines[0])
        t = Triangle().set_fill(PINK, opacity=1).rotate(-90*DEGREES).scale(.03)

        #self.play(t.animate.next_to(code1).shift(DOWN*(code1)))
        #self.play(t.animate.next_to(code1[-1]))
 





















