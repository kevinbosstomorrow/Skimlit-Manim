'''  
reference: https://github.com/Ackeraa/snake/blob/main/movie/main.py


manim -pqh manim_skimlit_p1.py Main
'''


from manim_helper import get_nn, get_matrix, get_rectangle
from manim import *






class Main(Scene):
    def construct(self):
        self.camera.background_color = GREY_E
        '''Chapter 1 - intro'''
        self.Intro()
        #self.Preprocessing()



    def Intro(self):



        '''INTRO ABSTRACT'''
        color = BLACK

        txt = '''
                    Despite the significant public health issue that it poses, only five medical treatments have been
                    approved for Alzheimer's disease (AD) and these act to control symptoms rather than alter the course 
                    of the disease. Studies of potential disease-modifying therapy have generally been undertaken in 
                    patients with clinically detectable disease, yet evidence suggests that the pathological changes 
                    associated with AD begin several years before this. It is possible that pharmacological therapy may 
                    be providing earlier diagnosis, such as cerebrospinal fluid biomarkers and amyloid positron emission 
                    tomography neuroimaging, are key to testing this theory in clinical trials. Recent results from  
                    trials of agents such as aducanumab are encouraging but must also be interpreted with caution. Such
                    medicines could potentially delay the onset of dementia and would therefore markedly reduce its
                    prevalence. However, we currently remain a good distance away from clinically available disease-
                    modifying therapy.
                    '''

        main = VGroup()
        title = Text("Drug treatments in Alzheimer's disease", color = color, slant=ITALIC).scale(0.6).shift(UP*4.2)


        authors = Text("Robert Briggs , Sean P Kennelly , Desmond O'Neill ", color= BLUE).scale(0.3).shift(UP*3.4).shift(LEFT*2.3)

        extra = Text('''
                    Affiliations + expand
                    PMID: 27251914 PMCID: PMC5922703 DOI: 10.7861/clinmedicine.16-3-247''',  color= color).scale(0.3).shift(UP*2.8).shift(LEFT*1.1)


        Abstract = Text(
                    '''Abstract''',  color= color).scale(0.5).shift(UP*2.3).shift(LEFT*3.85)
                    
        paragraph1 = Text(txt).shift(UP*1).scale(0.3).set_color(color)


        main.add(paragraph1, title, authors, extra, Abstract)
        
        white_square_background = Square().set_fill(WHITE, opacity=1).surround(main).shift(DOWN*1.1)

        txt_and_background = VGroup(white_square_background, main).scale(0.8).shift(DOWN*0.9)
        

        # show the whole paper, scale down and shift left
        self.play(FadeIn(txt_and_background))
        self.play(txt_and_background.animate.scale(0.7))
        self.play(txt_and_background.animate.shift(LEFT*3))

        white_backgroud2 = white_square_background.copy().shift(RIGHT*6)
        self.play(FadeIn(white_backgroud2))


        # paragraph1 
        cp = txt_and_background[1][0].copy()
        self.play(cp.animate.shift(RIGHT*6))
        self.wait(1)
        
        ''' SPLIT THE PARAGRAPH BY ITS SENTENCES'''
        splited_txt = VGroup()

        s1 = Text('''
                  Despite the significant public health issue that it poses, only five medical treatments have been
                  approved for Alzheimer's disease (AD) and these act to control symptoms rather than alter the 
                  course of the disease.''', color= color).scale(0.17).shift(RIGHT*3).shift(UP*2.3)

        s2 = Text('''
                  Studies of potential disease-modifying therapy have generally been undertaken in patients with 
                  clinically detectable disease, yet evidence suggests that the pathological changes associated 
                  with AD begin several years before this.''', color= color).scale(0.17).shift(UP*1.7).align_to(s1, LEFT)

        s3 = Text('''
                  It is possible that pharmacological therapy may be beneficial in this pre-clinical stage before 
                  the neurodegenerative process is established. ''', color= color).scale(0.17).align_to(s1, LEFT).shift(UP*1.1)

        s4 = Text('''
                  Techniques providing earlier diagnosis, such as cerebrospinal fluid biomarkers and amyloid 
                  positron emission tomography neuroimaging, are key to testing this theory in clinical trials. ''', color= color).scale(0.17).align_to(s1, LEFT).shift(UP*0.5)

        s5 = Text('''
                  Recent results from trials of agents such as aducanumab are encouraging but must also be 
                  interpreted with caution.''', color= color).scale(0.17).align_to(s1, LEFT).shift(DOWN*0.1)

        s6 = Text('''
                  Such medicines could potentially delay the onset of dementia and would therefore markedly 
                  reduce its prevalence.''', color= color).scale(0.17).align_to(s1, LEFT).shift(DOWN*0.7)

        s7 = Text('''
                  However, we currently remain a good distance away from clinically available disease-modifying 
                  therapy.''', color= color).scale(0.17).align_to(s1, LEFT).shift(DOWN*1.3)

        splited_txt.add(s1,s2,s3,s4,s5,s6,s7)
        #splited_txt.add(s1,s2)


        # transform from VGroup to VGroup. vgroup 转mobject不行
        self.play(Transform(cp, splited_txt), run_time = 3)
        self.play(FadeOut(txt_and_background))

        txt2_and_background = VGroup(white_backgroud2, cp)
        self.play(txt2_and_background.animate.shift(LEFT*6))


        '''FITTING IN THE DEEP NEURAL NETWORK'''

        # nn
        nns = get_nn([15, 12, 8, 5], 0.15, 1, WHITE).shift(RIGHT*3)

        #nns_label
        nnsl = ['Input layer(输入层)', 'Hidden layer(隐藏层)', 'Hidden layer(隐藏层)', 'Output layer(输出层)']
        nnslvg = VGroup()
        for n in range(4):
            nnslvg.add(Text(nnsl[n], color = WHITE).scale(0.2).move_to(nns[n].get_top()).shift(UP*0.3))

        # output label 
        ol = ['METHODS(方法)', 'RESULTS(结果)', 'CONCLUSIONS(总结)', 'BACKGROUND(背景)', 'OBJECTIVE(目标)']

        # label 放到output layer的右边
        ol_group = VGroup()
        for n in range(len(nns[-2])):
              ol_group.add(Text(ol[n]).move_to(nns[-2][n].get_right()).shift(RIGHT*0.8).scale(0.2))
        self.play(FadeIn(nns, ol_group, nnslvg),run_time = 2)

