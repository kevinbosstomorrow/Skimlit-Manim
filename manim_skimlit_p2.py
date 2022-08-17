
# manim -pqh manim_skimlit_p2.py Main
import itertools as it
from manim_helper import  get_matrix, get_rectangle
from manim import *
colors = ['#80ff9e', '#f0ff80', '#f0ff80', '#9eff80', '#80ffe3', '#97ff80', '#80f2ff', '#aa80ff', '#e680ff', '#ff80c8']
def get_nn(struct, circle_size, stroke_size):
    nn = VGroup()
    for i in range(len(struct)):
        nn.add(VGroup(*[Circle(circle_size, color= WHITE, stroke_width=stroke_size) for _ in range(struct[i])]).arrange(DOWN, buff=0.1)).arrange(RIGHT, 1)
    
    for l1, l2 in zip(nn[:-1], nn[1:]):
        for n1, n2 in it.product(l1, l2):
            edge = Line(n1.get_right(),n2.get_left(),stroke_width = 0.3, color = WHITE) 
            nn.add(edge)

    return nn


class Main(Scene):
    def construct(self):
        self.camera.background_color = GREY_E

        '''PART 1 - PRE-PROCESSING'''
        color = WHITE
        everything = VGroup()

        top1 = VGroup()
        top1_research_number = Text("###24854809", color = color)
        top1_research = Text('''OBJECTIVE	To investigate the efficacy of @ weeks of daily low-dose oral prednisolone in improving pain , mobility ,
METHODS	A total of @ patients with primary knee OA were randomized @:@ ; @ received @ mg/day of prednisolone and @ received placebo for @ weeks .
METHODS	Outcome measures included pain reduction and improvement in function scores and systemic inflammation markers .
METHODS	Pain was assessed using the visual analog pain scale ( @-@ mm ) .
METHODS	Secondary outcome measures included the Western Ontario and McMaster Universities Osteoarthritis Index scores , patient global assessment ( PGA )
METHODS	Serum levels of interleukin @ ( IL-@ ) , IL-@ , tumor necrosis factor ( TNF ) - , and high-sensitivity C-reactive protein ( hsCRP ) were measured .
RESULTS	There was a clinically relevant reduction in the intervention group compared to the placebo group for knee pain , physical function , PGA , and @MWD at @ weeks .
RESULTS	The mean difference between treatment arms ( @ % CI ) was @ ( @-@ @ ) , p < @ ; @ ( @-@ @ ) , p < @ ; @ ( @-@ @ ) , p < @ ;
RESULTS	Further , there was a clinically relevant reduction in the serum levels of IL-@ , IL-@ , TNF - , and hsCRP at @ weeks in the intervention group.
RESULTS	These differences remained significant at @ weeks .
RESULTS	The Outcome Measures in Rheumatology Clinical Trials-Osteoarthritis Research Society International responder rate was @ % in the intervention group and @ % in the placebo group ( p < @ ) .
CONCLUSIONS	Low-dose oral prednisolone had both a short-term and a longer sustained effect resulting in less knee pain.''', color = color).next_to(top1_research_number, DOWN).align_to(top1_research_number, LEFT)

        top1.add(top1_research_number, top1_research).scale(0.18).center().shift(UP*2.8)






        sample_research = VGroup()
        
        num = Text("###24854809", color = color)
    
        t1background = Text("BACKGROUND", color = color).next_to(num, DOWN).align_to(num, LEFT)
        t1text = Text("Emotional eating is associated with overeating and the development of obesity .", color = color).next_to(t1background, RIGHT)

        t2background = Text("BACKGROUND", color = color).next_to(t1background, DOWN).align_to(t1background, LEFT)
        t2text = Text("Yet , empirical evidence for individual ( trait ) differences in emotional eating and cognitive mechanisms that contribute to eating during sad mood remain equivocal.", color = color).next_to(t2background, RIGHT)

        t1object = Text("OBJECTIVE", color = color).next_to(t2background, DOWN).align_to(t2background, LEFT)
        t1objecttext = Text("The aim of this study was to test if attention bias for food moderates the effect of self-reported emotional eating during sad mood ( vs neutral mood ) on actual food intake.", color = color).next_to(t1object, RIGHT)

        t2object = Text("OBJECTIVE", color = color).next_to(t1object, DOWN).align_to(t1object, LEFT)
        t2objecttext = Text("It was expected that emotional eating is predictive of elevated attention for food and higher food intake after an experimentally induced sad mood.", color = color).next_to(t2object, RIGHT)

        t1method = Text("METHODS", color = color).next_to(t2object, DOWN).align_to(t2object, LEFT)
        t1methodtext = Text("Participants ( N = @ ) were randomly assigned to one of the two experimental mood induction conditions ( sad/neutral ) .", color = color).next_to(t1method, RIGHT)
        t2method = Text("METHODS", color = color).next_to(t1method, DOWN).align_to(t1method, LEFT)
        t2methodtext = Text("Attentional biases for high caloric foods were measured by eye tracking during a visual probe task with pictorial food and neutral stimuli .", color = color).next_to(t2method, RIGHT)
        t3method = Text("METHODS", color = color).next_to(t2method, DOWN).align_to(t2method, LEFT)
        t3methodtext = Text("Self-reported emotional eating was assessed with the Dutch Eating Behavior Questionnaire ( DEBQ ) and ad libitum food intake was tested by a disguised food offer .", color = color).next_to(t3method, RIGHT)

        t1result = Text("RESULTS", color = color).next_to(t3method, DOWN).align_to(t3method, LEFT)
        t1resulttext = Text("Hierarchical multivariate regression modeling showed that self-reported emotional eating did not account for changes in attention allocation for food or food intake in either condition .", color = color).next_to(t1result, RIGHT)
        t2result = Text("RESULTS", color = color).next_to(t1result, DOWN).align_to(t1result, LEFT)
        t2resulttext = Text("Yet , attention maintenance on food cues was significantly related to increased intake specifically in the neutral condition , but not in the sad mood condition .", color = color).next_to(t2result, RIGHT)

        t1conclusions = Text("CONCLUSIONS", color = color).next_to(t2result, DOWN).align_to(t2result, LEFT)
        t1conclusionstext = Text("The current findings show that self-reported emotional eating ( based on the DEBQ ) might not validly predict who overeats when sad , at least not in a laboratory setting with healthy women .", color = color).next_to(t1conclusions, RIGHT)
        t2conclusions = Text("CONCLUSIONS", color = color).next_to(t1conclusions, DOWN).align_to(t1conclusions, LEFT)
        t2conclusionstext = Text("Results further suggest that attention maintenance on food relates to eating motivation when in a neutral affective state , and might therefore be a cognitive mechanism .", color = color).next_to(t2conclusions, RIGHT)



        # vgroup 里面给个 position .center() 意思就是放到画面中间
        sample_research.add(num, t1background, t1text, t2background, t2text, t1object, t1objecttext, t2object, t2objecttext,
                            t1method,t1methodtext,t2method,t2methodtext,t3method,t3methodtext,t1result, t1resulttext, t2result, t2resulttext,
                           t1conclusions, t1conclusionstext, t2conclusions, t2conclusionstext).scale(0.18).center().shift(UP*0.8).align_to(top1_research_number, LEFT)
 



        Ellipsis1 = Text("。", color = color).center().scale(0.5).shift(DOWN*0.4)
        Ellipsis2 = Text("。", color = color).center().scale(0.5).shift(DOWN*0.7)
        Ellipsis3 = Text("。", color = color).center().scale(0.5).shift(DOWN*1)






        bottom1 = VGroup()
        bottom1_research_number = Text("###25165090", color = color).align_to(top1_research_number, LEFT)
        bottom1_research = Text('''BACKGROUND	Although working smoke alarms halve deaths in residential fires , many households do not keep alarms operational .
BACKGROUND	We tested whether theory-based education increases alarm operability .
METHODS	Randomised multiarm trial , with a single arm randomly selected for use each day , in low-income neighbourhoods in Maryland , USA .
METHODS	Intervention arms : ( @ ) Full Education combining a health belief module with a social-cognitive theory module...
METHODS	Four hundred and thirty-six homes recruited through churches or by knocking on doors in @-@...
METHODS	Follow-up visits checked alarm operability in @ homes ( @ % ) @-@ @ years after installation .
METHODS	number of homes with working alarms defined as alarms with working batteries or hard-wired and number of working alarms per home .
METHODS	Regressions controlled for alarm status preintervention ; demographics and beliefs about fire risks and alarm effectiveness .
RESULTS	Homes in the Full Education and Practice arms were more likely to have a functioning smoke alarm at follow-up
RESULTS	Working alarms per home rose @ % .
RESULTS	Full Education and Practice had similar effectiveness ( p = @ on both outcome measures ) .
CONCLUSIONS	Without exceeding typical fire department installation time , installers can achieve greater smoke alarm operability
CONCLUSIONS Hands-on practice is key .
CONCLUSIONS Two years after installation , for every three homes that received hands-on practice , one had an additional working alarm .
BACKGROUND http://www.clinicaltrials.gov number NCT@ .''', color = color).next_to(bottom1_research_number, DOWN).align_to(top1_research_number, LEFT)

        bottom1.add(bottom1_research_number, bottom1_research).scale(0.18).center().shift(DOWN*2.3).align_to(top1_research_number, LEFT)
        
        everything.add(top1, sample_research, Ellipsis1, Ellipsis2, Ellipsis3, bottom1)

        #white_background = Square().set_fill(WHITE, opacity=1).surround(everything)

        #everything2 = VGroup()
        #everything2.add(white_background, everything)

        self.play(FadeIn(everything))
        self.wait(3)

        # hightlight the research number 
        #self.play(Indicate(everything2[1][0][0], everything2[1][1][0], everything2[1][5][0], color= PURE_GREEN), run_time = 2)
        '''
        htrn1 = Rectangle(height= 0.5,width = 7, color = MAROON).scale(0.25).set_opacity(0.2).shift(everything[0][0].get_center())
        htrn2 = Rectangle(height= 0.5,width = 7, color = MAROON).scale(0.25).set_opacity(0.2).shift(everything[1][0].get_center())        
        htrn3 = Rectangle(height= 0.5,width = 7, color = MAROON).scale(0.25).set_opacity(0.2).shift(everything[5][0].get_center())
        self.play(FadeIn(htrn1), FadeIn(htrn2), FadeIn(htrn3), run_time = 3)
        self.wait(1)
        '''
        self.play(Indicate(everything[0][0], color= MAROON, run_time = 3, scale_factor =1),
                  Indicate(everything[1][0], color= MAROON, run_time = 3, scale_factor =1),
                  Indicate(everything[5][0], color= MAROON, run_time = 3, scale_factor =1))
        self.wait(2)
        

        # hightlight each chunck 
        '''
        #self.play(Circumscribe(everything2[1][0], everything2[1][1], everything2[1][5]), run_time = 2)
        self.play(Circumscribe(everything2[1][0],  run_time = 2),
                  Circumscribe(everything2[1][1],  run_time = 2),
                  Circumscribe(everything2[1][5],  run_time = 2))
        

        background1 = Rectangle(stroke_color = YELLOW).surround(everything2[1][0])
        background2 = Rectangle(stroke_color = YELLOW).surround(everything2[1][1])
        background3 = Rectangle(stroke_color = YELLOW).surround(everything2[1][5])
        self.play(FadeIn(background1, background2, background3 ))

        self.play(ShowPassingFlash(background1.copy().set_color(BLUE),run_time=2, time_width= 1),
                  ShowPassingFlash(background2.copy().set_color(BLUE),run_time=2, time_width= 1),
                  ShowPassingFlash(background3.copy().set_color(BLUE),run_time=2, time_width= 1))

        self.wait(2)
        '''
        # 只保留第2部分 
        self.play(FadeOut(everything[0], everything[2],everything[3],everything[4],everything[5]))

        # 分成2部分一部分是标记好的有了 label， 一部分是内容 text
        self.play(Indicate(everything[1][1], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][3], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][5], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][7], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][9], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][11], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][13], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][15], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][17], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][19], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][21], color= MAROON, run_time = 2, scale_factor =1))      

        self.play(Indicate(everything[1][2], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][4], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][6], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][8], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][10], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][12], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][14], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][16], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][18], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][20], color= MAROON, run_time = 2, scale_factor =1),
                  Indicate(everything[1][22], color= MAROON, run_time = 2, scale_factor =1))      




        #self.play(everything[1].animate.scale(0.9))
        self.play(everything[1].animate.shift(UP*1.9))


        # Show dataframe scalar_height, scalar_width, vector_size, matrix_size, stroke_size, col
        rt = get_rectangle(1, 7, 7, 20, 0.5, WHITE).center().shift(DOWN*0.8)

        title = ['Research num(论文编号)', 'Subject(主题)', 'Text(句子)', 'Line_number(句子行号)', 'Total_lines(论文总体行数)', 'Sentence_length(每句的单词数量)']
        for i,t in enumerate(title):
            rt.add(Text(t, color= BLACK).scale(0.7).move_to(rt[0][i+1].get_center()))
        
        rt.scale(0.25)
        # 播放表格
        self.play(FadeIn(rt))


        # 开始填表格 dataframe

        # 填 fill in index #
        index1 = Text("0").set_color(BLACK).scale(0.20).shift(rt[1][0].get_center())
        index2 = Text("1").set_color(BLACK).scale(0.20).shift(rt[2][0].get_center())
        index3 = Text("2").set_color(BLACK).scale(0.20).shift(rt[3][0].get_center())
        index4 = Text("3").set_color(BLACK).scale(0.20).shift(rt[4][0].get_center())
        index5 = Text("4").set_color(BLACK).scale(0.20).shift(rt[5][0].get_center())
        index6 = Text("5").set_color(BLACK).scale(0.20).shift(rt[6][0].get_center())
        index7 = Text("6").set_color(BLACK).scale(0.20).shift(rt[7][0].get_center())
        index8 = Text("7").set_color(BLACK).scale(0.20).shift(rt[8][0].get_center())
        index9 = Text("8").set_color(BLACK).scale(0.20).shift(rt[9][0].get_center())
        index10 = Text("9").set_color(BLACK).scale(0.20).shift(rt[10][0].get_center())
        index11 = Text("10").set_color(BLACK).scale(0.20).shift(rt[11][0].get_center())

        # 填research number fill research number
        rn1 = everything[1][0][3:].copy().set_color(BLACK)
        rn2 = everything[1][0][3:].copy().set_color(BLACK)
        rn3 = everything[1][0][3:].copy().set_color(BLACK)
        rn4 = everything[1][0][3:].copy().set_color(BLACK)
        rn5 = everything[1][0][3:].copy().set_color(BLACK)
        rn6 = everything[1][0][3:].copy().set_color(BLACK)
        rn7 = everything[1][0][3:].copy().set_color(BLACK)
        rn8 = everything[1][0][3:].copy().set_color(BLACK)
        rn9 = everything[1][0][3:].copy().set_color(BLACK)
        rn10 = everything[1][0][3:].copy().set_color(BLACK)
        rn11 = everything[1][0][3:].copy().set_color(BLACK)
        # add 要放到play 前面要不然背景会有数字
        rt.add(rn1,rn2,rn3,rn4,rn5,rn6,rn7,rn8,rn9,rn10,rn11,index1,index2,index3,index4,index5,index6,index7,index8,index9,index10,index11)
        self.play(rn1.animate.move_to(rt[1][1].get_center()),
            rn2.animate.move_to(rt[2][1].get_center()),
            rn3.animate.move_to(rt[3][1].get_center()),
            rn4.animate.move_to(rt[4][1].get_center()),
            rn5.animate.move_to(rt[5][1].get_center()),
            rn6.animate.move_to(rt[6][1].get_center()),
            rn7.animate.move_to(rt[7][1].get_center()),
            rn8.animate.move_to(rt[8][1].get_center()),
            rn9.animate.move_to(rt[9][1].get_center()),
            rn10.animate.move_to(rt[10][1].get_center()),
            rn11.animate.move_to(rt[11][1].get_center()), 
            FadeIn(index1),FadeIn(index2),FadeIn(index3),FadeIn(index4),FadeIn(index5),FadeIn(index6),FadeIn(index7),FadeIn(index8),FadeIn(index9),FadeIn(index10),FadeIn(index11),
            run_time = 2)


        
        # 填主题 fill the subject
        subject1 = everything[1][1].copy().set_color(BLACK)
        subject2 = everything[1][3].copy().set_color(BLACK)
        subject3 = everything[1][5].copy().set_color(BLACK)
        subject4 = everything[1][7].copy().set_color(BLACK)
        subject5 = everything[1][9].copy().set_color(BLACK)
        subject6 = everything[1][11].copy().set_color(BLACK)
        subject7 = everything[1][13].copy().set_color(BLACK)
        subject8 = everything[1][15].copy().set_color(BLACK)
        subject9 = everything[1][17].copy().set_color(BLACK)
        subject10 = everything[1][19].copy().set_color(BLACK)
        subject11 = everything[1][21].copy().set_color(BLACK)
        rt.add(subject1,subject2,subject3,subject4,subject5,subject6,subject7,subject8,subject9,subject10,subject11)
        self.play(subject1.animate.move_to(rt[1][2].get_center()),
            subject2.animate.move_to(rt[2][2].get_center()),
            subject3.animate.move_to(rt[3][2].get_center()),
            subject4.animate.move_to(rt[4][2].get_center()),
            subject5.animate.move_to(rt[5][2].get_center()),
            subject6.animate.move_to(rt[6][2].get_center()),
            subject7.animate.move_to(rt[7][2].get_center()),
            subject8.animate.move_to(rt[8][2].get_center()),
            subject9.animate.move_to(rt[9][2].get_center()),
            subject10.animate.move_to(rt[10][2].get_center()),
            subject11.animate.move_to(rt[11][2].get_center()), run_time = 2)


        # 填 fill the text 
        txt1 = everything[1][2][:30].copy().set_color(BLACK)
        txt2 = everything[1][4][:30].copy().set_color(BLACK)
        txt3 = everything[1][6][:30].copy().set_color(BLACK)
        txt4 = everything[1][8][:30].copy().set_color(BLACK)
        txt5 = everything[1][10][:30].copy().set_color(BLACK)
        txt6 = everything[1][12][:30].copy().set_color(BLACK)
        txt7 = everything[1][14][:30].copy().set_color(BLACK)
        txt8 = everything[1][16][:30].copy().set_color(BLACK)
        txt9 = everything[1][18][:30].copy().set_color(BLACK)
        txt10 = everything[1][20][:30].copy().set_color(BLACK)
        txt11 = everything[1][22][:30].copy().set_color(BLACK)
        rt.add(txt1,txt2,txt3,txt4,txt5,txt6,txt7,txt8,txt9,txt10,txt11)
        self.play(txt1.animate.move_to(rt[1][3].get_center()),
            txt2.animate.move_to(rt[2][3].get_center()),
            txt3.animate.move_to(rt[3][3].get_center()),
            txt4.animate.move_to(rt[4][3].get_center()),
            txt5.animate.move_to(rt[5][3].get_center()),
            txt6.animate.move_to(rt[6][3].get_center()),
            txt7.animate.move_to(rt[7][3].get_center()),
            txt8.animate.move_to(rt[8][3].get_center()),
            txt9.animate.move_to(rt[9][3].get_center()),
            txt10.animate.move_to(rt[10][3].get_center()),
            txt11.animate.move_to(rt[11][3].get_center()), run_time = 2)


        # 填 fill the line number
        line1 = Text("1").set_color(BLACK).scale(0.2).shift(rt[1][4].get_center())
        line2 = Text("2").set_color(BLACK).scale(0.2).shift(rt[2][4].get_center())
        line3 = Text("3").set_color(BLACK).scale(0.2).shift(rt[3][4].get_center())
        line4 = Text("4").set_color(BLACK).scale(0.2).shift(rt[4][4].get_center())
        line5 = Text("5").set_color(BLACK).scale(0.2).shift(rt[5][4].get_center())
        line6 = Text("6").set_color(BLACK).scale(0.2).shift(rt[6][4].get_center())
        line7 = Text("7").set_color(BLACK).scale(0.2).shift(rt[7][4].get_center())
        line8 = Text("8").set_color(BLACK).scale(0.2).shift(rt[8][4].get_center())
        line9 = Text("9").set_color(BLACK).scale(0.2).shift(rt[9][4].get_center())
        line10 =Text("10").set_color(BLACK).scale(0.2).shift(rt[10][4].get_center())
        line11 =Text("11").set_color(BLACK).scale(0.2).shift(rt[11][4].get_center())
        rt.add(line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11)
        self.play(FadeIn(line1),FadeIn(line2),FadeIn(line3),FadeIn(line4),FadeIn(line5),FadeIn(line6),FadeIn(line7),FadeIn(line8),FadeIn(line9),FadeIn(line10),FadeIn(line11),run_time = 2)



        # 填 fill the total line number
        tline1 = Text("11").set_color(BLACK).scale(0.2).shift(rt[1][5].get_center())
        tline2 = Text("11").set_color(BLACK).scale(0.2).shift(rt[2][5].get_center())
        tline3 = Text("11").set_color(BLACK).scale(0.2).shift(rt[3][5].get_center())
        tline4 = Text("11").set_color(BLACK).scale(0.2).shift(rt[4][5].get_center())
        tline5 = Text("11").set_color(BLACK).scale(0.2).shift(rt[5][5].get_center())
        tline6 = Text("11").set_color(BLACK).scale(0.2).shift(rt[6][5].get_center())
        tline7 = Text("11").set_color(BLACK).scale(0.2).shift(rt[7][5].get_center())
        tline8 = Text("11").set_color(BLACK).scale(0.2).shift(rt[8][5].get_center())
        tline9 = Text("11").set_color(BLACK).scale(0.2).shift(rt[9][5].get_center())
        tline10 =Text("11").set_color(BLACK).scale(0.2).shift(rt[10][5].get_center())
        tline11 =Text("11").set_color(BLACK).scale(0.2).shift(rt[11][5].get_center())
        rt.add(tline1,tline2,tline3,tline4,tline5,tline6,tline7,tline8,tline9,tline10,tline11)
        self.play(FadeIn(tline1),FadeIn(tline2),FadeIn(tline3),FadeIn(tline4),FadeIn(tline5),FadeIn(tline6),FadeIn(tline7),FadeIn(tline8),FadeIn(tline9),FadeIn(tline10),FadeIn(tline11),run_time = 2)

        


        # 填 fill the sentense lengths 12,25,32,23, 22, 23,27,26,27,34, 27
        len1 = Text("12").set_color(BLACK).scale(0.2).shift(rt[1][6].get_center())
        len2 = Text("25").set_color(BLACK).scale(0.2).shift(rt[2][6].get_center())
        len3 = Text("32").set_color(BLACK).scale(0.2).shift(rt[3][6].get_center())
        len4 = Text("23").set_color(BLACK).scale(0.2).shift(rt[4][6].get_center())
        len5 = Text("22").set_color(BLACK).scale(0.2).shift(rt[5][6].get_center())
        len6 = Text("23").set_color(BLACK).scale(0.2).shift(rt[6][6].get_center())
        len7 = Text("27").set_color(BLACK).scale(0.2).shift(rt[7][6].get_center())
        len8 = Text("26").set_color(BLACK).scale(0.2).shift(rt[8][6].get_center())
        len9 = Text("27").set_color(BLACK).scale(0.2).shift(rt[9][6].get_center())
        len10 =Text("34").set_color(BLACK).scale(0.2).shift(rt[10][6].get_center())
        len11 =Text("27").set_color(BLACK).scale(0.2).shift(rt[11][6].get_center())
        rt.add(len1,len2,len3,len4,len5,len6,len7,len8,len9,len10,len11)
        self.play(FadeIn(len1),FadeIn(len2),FadeIn(len3),FadeIn(len4),FadeIn(len5),FadeIn(len6),FadeIn(len7),FadeIn(len8),FadeIn(len9),FadeIn(len10),FadeIn(len11),run_time = 2)
        self.wait(2)


        # fill the Ellipsis row 
        erow1 = Text("...").set_color(BLACK).scale(0.2).shift(rt[12][0].get_center())
        erow2 = Text("...").set_color(BLACK).scale(0.2).shift(rt[12][1].get_center())
        erow3 = Text("...").set_color(BLACK).scale(0.2).shift(rt[12][2].get_center())
        erow4 = Text("...").set_color(BLACK).scale(0.2).shift(rt[12][3].get_center())
        erow5 = Text("...").set_color(BLACK).scale(0.2).shift(rt[12][4].get_center())
        erow6 = Text("...").set_color(BLACK).scale(0.2).shift(rt[12][5].get_center())
        erow7 = Text("...").set_color(BLACK).scale(0.2).shift(rt[12][6].get_center())
        rt.add(erow1,erow2,erow3,erow4,erow5,erow6,erow7)
        self.play(FadeIn(erow1),FadeIn(erow2),FadeIn(erow3),FadeIn(erow4),FadeIn(erow5),FadeIn(erow6),FadeIn(erow7),run_time = 2)


        # fill the rest row 13 - 18
        '''
        r2 = ['25165090', 'RESULTS', 'Working alarms per home rose', '10','15','17']
        r3 = ['25165090', 'RESULTS', 'Full Education and Practice', '11','15','22']
        r4 = ['25165090', 'CONCLUSIONS', 'Without exceeding typical fire', '12','15','27']
        r5 = ['25165090', 'CONCLUSIONS', 'Hands-on practice is key .', '13','15','4']
        r6 = ['25165090', 'CONCLUSIONS', 'Two years after installation', '14','15','24']
        r7 = ['25165090', 'BACKGROUND', 'www.clinicaltrials.gov number', '15','15','3']
        '''
        r20 = Text('180034').set_color(BLACK).scale(0.2).shift(rt[13][0].get_center())
        r21 = Text('25165090').set_color(BLACK).scale(0.19).shift(rt[13][1].get_center())
        r22 = Text('RESULTS').set_color(BLACK).scale(0.19).shift(rt[13][2].get_center())
        r23 = Text('Working alarms per home rose').set_color(BLACK).scale(0.19).shift(rt[13][3].get_center())
        r24 = Text('10').set_color(BLACK).scale(0.2).shift(rt[13][4].get_center())
        r25 = Text('15').set_color(BLACK).scale(0.2).shift(rt[13][5].get_center())
        r26 = Text('17').set_color(BLACK).scale(0.2).shift(rt[13][6].get_center())
       
        r30 = Text('180035').set_color(BLACK).scale(0.2).shift(rt[14][0].get_center())
        r31 = Text('25165090').set_color(BLACK).scale(0.19).shift(rt[14][1].get_center())
        r32 = Text('RESULTS').set_color(BLACK).scale(0.19).shift(rt[14][2].get_center())
        r33 = Text('Full Education and Practice').set_color(BLACK).scale(0.19).shift(rt[14][3].get_center())
        r34 = Text('11').set_color(BLACK).scale(0.2).shift(rt[14][4].get_center())
        r35 = Text('15').set_color(BLACK).scale(0.2).shift(rt[14][5].get_center())
        r36 = Text('22').set_color(BLACK).scale(0.2).shift(rt[14][6].get_center())

        r40 = Text('180036').set_color(BLACK).scale(0.2).shift(rt[15][0].get_center())       
        r41 = Text('25165090').set_color(BLACK).scale(0.19).shift(rt[15][1].get_center())
        r42 = Text('CONCLUSIONS').set_color(BLACK).scale(0.19).shift(rt[15][2].get_center())
        r43 = Text('Without exceeding typical fire').set_color(BLACK).scale(0.19).shift(rt[15][3].get_center())
        r44 = Text('12').set_color(BLACK).scale(0.2).shift(rt[15][4].get_center())
        r45 = Text('15').set_color(BLACK).scale(0.2).shift(rt[15][5].get_center())
        r46 = Text('27').set_color(BLACK).scale(0.2).shift(rt[15][6].get_center())
        
        r50 = Text('180037').set_color(BLACK).scale(0.2).shift(rt[16][0].get_center())
        r51 = Text('25165090').set_color(BLACK).scale(0.19).shift(rt[16][1].get_center())
        r52 = Text('CONCLUSIONS').set_color(BLACK).scale(0.19).shift(rt[16][2].get_center())
        r53 = Text('Hands-on practice is key .').set_color(BLACK).scale(0.19).shift(rt[16][3].get_center())
        r54 = Text('13').set_color(BLACK).scale(0.2).shift(rt[16][4].get_center())
        r55 = Text('15').set_color(BLACK).scale(0.2).shift(rt[16][5].get_center())
        r56 = Text('5').set_color(BLACK).scale(0.2).shift(rt[16][6].get_center())
        
        r60 = Text('180038').set_color(BLACK).scale(0.2).shift(rt[17][0].get_center())        
        r61 = Text('25165090').set_color(BLACK).scale(0.19).shift(rt[17][1].get_center())
        r62 = Text('CONCLUSIONS').set_color(BLACK).scale(0.19).shift(rt[17][2].get_center())
        r63 = Text('Two years after installation').set_color(BLACK).scale(0.19).shift(rt[17][3].get_center())
        r64 = Text('14').set_color(BLACK).scale(0.2).shift(rt[17][4].get_center())
        r65 = Text('15').set_color(BLACK).scale(0.2).shift(rt[17][5].get_center())
        r66 = Text('24').set_color(BLACK).scale(0.2).shift(rt[17][6].get_center())
        
        r70 = Text('180039').set_color(BLACK).scale(0.2).shift(rt[18][0].get_center())  
        r71 = Text('25165090').set_color(BLACK).scale(0.19).shift(rt[18][1].get_center())
        r72 = Text('BACKGROUND').set_color(BLACK).scale(0.19).shift(rt[18][2].get_center())
        r73 = Text('www.clinicaltrials.gov number').set_color(BLACK).scale(0.19).shift(rt[18][3].get_center())
        r74 = Text('15').set_color(BLACK).scale(0.2).shift(rt[18][4].get_center())
        r75 = Text('15').set_color(BLACK).scale(0.2).shift(rt[18][5].get_center())
        r76 = Text('4').set_color(BLACK).scale(0.2).shift(rt[18][6].get_center())         
        
        # fill in last row 
        lr = Text('180040 rows x 6 columns').set_color(BLACK).scale(0.2).shift(rt[19][0].get_center())

        rt.add(r20,r21,r22,r23,r24,r25,r26,r30,r31,r32,r33,r34,r35,r36,r40,r41,r42,r43,r44,r45,r46,r50,r51,r52,r53,r54,r55,r56,r60,r61,r62,r63,r64,r65,r66,r70,r71,r72,r73,r74,r75,r76, lr)
        self.play(FadeIn(r20),FadeIn(r21),FadeIn(r22),FadeIn(r23),FadeIn(r24),FadeIn(r25),FadeIn(r26),
                FadeIn(r30),FadeIn(r31),FadeIn(r32),FadeIn(r33),FadeIn(r34),FadeIn(r35),FadeIn(r36),
                FadeIn(r40),FadeIn(r41),FadeIn(r42),FadeIn(r43),FadeIn(r44),FadeIn(r45),FadeIn(r46),
                FadeIn(r50),FadeIn(r51),FadeIn(r52),FadeIn(r53),FadeIn(r54),FadeIn(r55),FadeIn(r56),
                FadeIn(r60),FadeIn(r61),FadeIn(r62),FadeIn(r63),FadeIn(r64),FadeIn(r65),FadeIn(r66),
                FadeIn(r70),FadeIn(r71),FadeIn(r72),FadeIn(r73),FadeIn(r74),FadeIn(r75),FadeIn(r76),
                FadeIn(lr), run_time = 2)

        # Intro 介绍python index 从0开始
        box = VGroup(SurroundingRectangle(rt[1][0], color=MAROON  , buff= 0 ).set_stroke(width=2))
        self.play(FadeIn(box), run_time = 2)

        # Intro total rows. 让神经网络尽可能的学习
        self.play(box.animate.move_to(rt[19][0].get_center()), run_time = 3)

        # Intro research number , 只是区分文章的不代入模型
        self.play(box.animate.move_to(rt[0][1].get_center()), run_time = 2)

        # Intro subject , 模型output用的 Y 
        self.play(box.animate.move_to(rt[0][2].get_center()), run_time = 2)

        # Intro TEXT , 模型input 用的， 代入神经网络 
        self.play(box.animate.move_to(rt[0][3].get_center()), run_time = 2)

        # Intro line number , 模型input 用的， 顺序不能变 因为。。 
        self.play(box.animate.move_to(rt[0][4].get_center()), run_time = 2)

        # total lines, ....
        self.play(box.animate.move_to(rt[0][5].get_center()), run_time = 2)

        # sentence in order to get 95 percentile is 55
        self.play(box.animate.move_to(rt[0][6].get_center()), run_time = 2)
        self.wait(4)
        


        '''PART 3 - INPUT& OUPUT & MODEL'''

        # Fade out the text 
        self.play(FadeOut(everything[1]),FadeOut(box))
        #self.play(rt.animate.shift(UP*0.8))

        # Model output ont-hot encoing subject
        subjects = VGroup()
        subjects.add(rt[0][2].copy(), rt[1][2].copy(),rt[2][2].copy(),rt[3][2].copy(),rt[4][2].copy(),rt[5][2].copy(),rt[6][2].copy(),
        rt[7][2].copy(),rt[8][2].copy(),rt[9][2].copy(),rt[10][2].copy(),rt[11][2].copy(),rt[12][2].copy(),rt[13][2].copy(),rt[14][2].copy(),
        rt[15][2].copy(),rt[16][2].copy(),rt[17][2].copy(),rt[18][2].copy(),rt[19][2].copy(),rt[21].copy(), rt[48].copy(),rt[49].copy(),
        rt[50].copy(),rt[51].copy(),rt[52].copy(),rt[53].copy(),rt[54].copy(),rt[55].copy(),rt[56].copy(),rt[57].copy(),rt[58].copy(),
        rt[105].copy(),rt[112].copy(),rt[119].copy(),rt[126].copy(),rt[133].copy(),rt[140].copy(),rt[147].copy())
        self.play(FadeIn(subjects), FadeOut(rt), run_time = 2)
        self.play(subjects.animate.shift(LEFT*2.5))
        self.wait(2)


        # one hot encoding part
        # Show dataframe scalar_height, scalar_width, vector_size, matrix_size, stroke_size, col
        rt2 = get_rectangle(1, 5, 6, 20, 0.5, WHITE).center().shift(RIGHT*1).shift(DOWN*0.8)

        # 填 index
        indexlist = ['0','1','2','3','4','5','6','7','8','9','10','...',"180034","180035","180036","180037","180038","180039","180040 rows x 5 columns"]
        for i,t in enumerate(indexlist):
            
            if i == 18:
                rt2.add(Text(t).set_color(BLACK).scale(0.80).shift(rt2[i+1][0].get_center()).shift(RIGHT*0.52))
            else:
                rt2.add(Text(t).set_color(BLACK).scale(0.80).shift(rt2[i+1][0].get_center()))    

        # 填one-hot0 method
        oh0 = ['0','0','0','0','1','1','1','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh0):
            rt2.add(Text(t).set_color(BLACK).scale(0.80).shift(rt2[i+1][1].get_center()))
            
        # 填one-hot1 results
        oh1 = ['0','0','0','0','0','0','0','1','1','0','0','...','1','1','0','0','0','0',]
        for i,t in enumerate(oh1):
            rt2.add(Text(t).set_color(BLACK).scale(0.80).shift(rt2[i+1][2].get_center()))
        
        # 填one-hot2 conclusions
        oh2 = ['0','0','0','0','0','0','0','0','0','1','1','...','0','0','1','1','1','0',]
        for i,t in enumerate(oh2):
            rt2.add(Text(t).set_color(BLACK).scale(0.80).shift(rt2[i+1][3].get_center()))
        
        # 填one-hot3 background
        oh3 = ['1','1','0','0','0','0','0','0','0','0','0','...','0','0','0','0','0','1',]
        for i,t in enumerate(oh3):
            rt2.add(Text(t).set_color(BLACK).scale(0.80).shift(rt2[i+1][4].get_center()))

        # 填one-hot4 objective
        oh4 = ['0','0','1','1','0','0','0','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh4):
            rt2.add(Text(t).set_color(BLACK).scale(0.80).shift(rt2[i+1][5].get_center()))


        title2 = ['METHODS(方法)', 'RESULTS(结果)', 'CONCLUSIONS(总结)', 'BACKGROUND(背景)', 'OBJECTIVE(目标)']
        for i,t in enumerate(title2):
            rt2.add(Text(t, color= BLACK).scale(0.7).move_to(rt2[0][i+1].get_center()))

        rt2.scale(0.25)
        s2 = subjects.copy()
        self.play(Transform(s2, rt2), run_time = 3)


        # color indecate METHOD = RED  
        '''
        rsmall = Rectangle(height= 1,width = 7, color = RED).scale(0.25)
        Rectangle(height= 1,width = 7, color = RED).scale(0.25).shift(rt[0][4].get_center()).set_opacity(0.2)

        self.play(Transform(subjects[21], subjects[21].set_color(YELLOW).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[22], subjects[22].set_color(YELLOW).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[38], subjects[38].set_color(YELLOW).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[93], rt2[93].set_color(YELLOW).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[94], rt2[94].set_color(YELLOW).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[110], rt2[110].set_color(YELLOW).set_stroke(BLACK, width=0.1)),

                  Transform(subjects[23], subjects[23].set_color(GREEN).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[24], subjects[24].set_color(GREEN).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[113], rt2[113].set_color(GREEN).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[114], rt2[114].set_color(GREEN).set_stroke(BLACK, width=0.1)),
                  
                  Transform(subjects[25], subjects[25].set_color(RED).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[26], subjects[26].set_color(RED).set_stroke(BLACK, width=0.1)),                            
                  Transform(subjects[27], subjects[27].set_color(RED).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[43], rt2[43].set_color(RED).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[44], rt2[44].set_color(RED).set_stroke(BLACK, width=0.1)),                  
                  Transform(rt2[45], rt2[45].set_color(RED).set_stroke(BLACK, width=0.1)),
               
                  Transform(subjects[28], subjects[28].set_color(BLUE).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[29], subjects[29].set_color(BLUE).set_stroke(BLACK, width=0.1)),  
                  Transform(subjects[33], subjects[33].set_color(BLUE).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[34], subjects[34].set_color(BLUE).set_stroke(BLACK, width=0.1)),  
                  Transform(rt2[64], rt2[64].set_color(BLUE).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[65], rt2[65].set_color(BLUE).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[69], rt2[69].set_color(BLUE).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[70], rt2[70].set_color(BLUE).set_stroke(BLACK, width=0.1)),

                  Transform(subjects[30], subjects[30].set_color(PINK).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[31], subjects[31].set_color(PINK).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[35], subjects[35].set_color(PINK).set_stroke(BLACK, width=0.1)),
                  Transform(subjects[36], subjects[36].set_color(PINK).set_stroke(BLACK, width=0.1)),                                           
                  Transform(subjects[37], subjects[37].set_color(PINK).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[84], rt2[84].set_color(PINK).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[85], rt2[85].set_color(PINK).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[89], rt2[89].set_color(PINK).set_stroke(BLACK, width=0.1)),
                  Transform(rt2[90], rt2[90].set_color(PINK).set_stroke(BLACK, width=0.1)),                  
                  Transform(rt2[91], rt2[91].set_color(PINK).set_stroke(BLACK, width=0.1)), run_time = 3)           
        
        # example background
        self.play(Indicate(subjects[21], color= PURE_RED, run_time = 3, scale_factor =1),
                  Indicate(subjects[22], color= PURE_BLUE, run_time = 3, scale_factor =1),
                  Indicate(subjects[38], color= PURE_GREEN, run_time = 3, scale_factor =1),
                  Indicate(rt2[93], color= YELLOW, run_time = 3, scale_factor =1),
                  Indicate(rt2[94], color= PURE_GREEN, run_time = 3, scale_factor =1),
                  Indicate(rt2[110], color= PURE_GREEN, run_time = 3, scale_factor =1))
        '''
        rta1 = Rectangle(height= 1,width = 7, color = YELLOW).scale(0.25).set_opacity(0.2).shift(subjects[1].get_center())
        rta2 = Rectangle(height= 1,width = 7, color = YELLOW).scale(0.25).set_opacity(0.2).shift(subjects[2].get_center())
        rta3 = Rectangle(height= 1,width = 7, color = YELLOW).scale(0.25).set_opacity(0.2).shift(subjects[18].get_center())
        rta4 = Rectangle(height= 1,width = 5, color = YELLOW).scale(0.25).set_opacity(0.2).shift(rt2[1][4].get_center())
        rta5 = Rectangle(height= 1,width = 5, color = YELLOW).scale(0.25).set_opacity(0.2).shift(rt2[2][4].get_center())
        rta6 = Rectangle(height= 1,width = 5, color = YELLOW).scale(0.25).set_opacity(0.2).shift(rt2[18][4].get_center())
        
        self.play(FadeIn(rta1),
                  FadeIn(rta2),
                  FadeIn(rta3),
                  FadeIn(rta4),
                  FadeIn(rta5), 
                  FadeIn(rta6),run_time = 2)
        self.wait(2)
        self.play(FadeOut(rta1),
                  FadeOut(rta2),
                  FadeOut(rta3),
                  FadeOut(rta4),
                  FadeOut(rta5),
                  FadeOut(rta6), run_time = 2)




        # Bar chart
        bc = VGroup()
        re1 = Rectangle(height = 3, width = 0.5, stroke_width = 0.5, fill_color=RED, fill_opacity=1).shift(rt2[0][1].get_top()).shift(UP*1).set_stroke(color=BLACK, width=1).scale(0.5)     
        re2 = Rectangle(height = 2.7, width = 0.5, stroke_width = 0.5, fill_color=BLUE, fill_opacity=1).shift(rt2[0][2].get_top()).scale(0.5).align_to(re1, DOWN).set_stroke(color=BLACK, width=1)
        re3 = Rectangle(height = 1.4, width = 0.5, stroke_width = 0.5, fill_color=PINK, fill_opacity=1).shift(rt2[0][3].get_top()).scale(0.5).align_to(re1, DOWN).set_stroke(color=BLACK, width=1)
        re4 = Rectangle(height = 1.1, width = 0.5, stroke_width = 0.5, fill_color=YELLOW, fill_opacity=1).shift(rt2[0][4].get_top()).scale(0.5).align_to(re1, DOWN).set_stroke(color=BLACK, width=1)
        re5 = Rectangle(height = 0.5, width = 0.5, stroke_width = 0.5, fill_color=GREEN, fill_opacity=1).shift(rt2[0][5].get_top()).scale(0.5).align_to(re1, DOWN).set_stroke(color=BLACK, width=1)

        axes = VGroup()
        xaxis = Line(start= np.array([0, 0, 0]), end=np.array([5.8, 0, 0]),buff=0).set_color(WHITE)
        yaxis = Line(start= np.array([0, 0, 0.]), end=np.array([0, 1.7, 0.]),buff=0).set_color(WHITE)

        three_bar = Line(start= np.array([0, 0, 0]), end=np.array([0.1, 0, 0]),buff=0).shift(yaxis.get_center()).set_color(WHITE)
        six_bar = Line(start= np.array([0, 0, 0]), end=np.array([0.1, 0, 0]),buff=0).shift(yaxis.get_top()).shift(DOWN*0.1).set_color(WHITE)

        zero = Text('0').scale(0.3).set_color(WHITE).shift(xaxis.get_left()).shift(LEFT*0.4)
        three = Text('30000').scale(0.3).set_color(WHITE).shift(yaxis.get_left()).shift(LEFT*0.4)
        six = Text('60000').scale(0.3).set_color(WHITE).shift(yaxis.get_top()).shift(LEFT*0.4)
        axes.add(xaxis,yaxis,three_bar,six_bar,zero,three,six).shift(re1.get_bottom()).shift(LEFT*0.4)
          

        total_method =  Text('59353').scale(0.2).set_color(WHITE).shift(re1.get_top()).shift(UP*0.1)
        total_result =  Text('57953').scale(0.2).set_color(WHITE).shift(re2.get_top()).shift(UP*0.1)
        total_conclusions =  Text('27168').scale(0.2).set_color(WHITE).shift(re3.get_top()).shift(UP*0.1)
        total_background =  Text('21727').scale(0.2).set_color(WHITE).shift(re4.get_top()).shift(UP*0.1)
        total_objective =  Text('13839').scale(0.2).set_color(WHITE).shift(re5.get_top()).shift(UP*0.1)
                        


        bc.add(re1,re2,re3,re4,re5,axes,total_method,total_result,total_conclusions,total_background,total_objective).shift(DOWN*0.15)
        self.play(Create(bc), run_time = 3)
        self.wait(4)


    
        # 算出每一列的total for example emthod sums up to 59353
        rtf = Rectangle(height= 20,width = 5, color = RED).center().scale(0.25).shift(DOWN*0.8).shift(LEFT*0.9).set_opacity(0.3)
        self.play(FadeIn(rtf)) 
        self.wait(2)
        rtf4 = rtf.copy().set_color(GREEN).shift(RIGHT*5)
        self.play(Transform(rtf, rtf4), run_time = 2)
        self.wait(2)

        self.play(FadeOut(rt2,s2,bc,rtf,rtf4))
        self.play(subjects.animate.shift(RIGHT*2.5))
        self.play(FadeIn(rt))
        self.wait(2)
        self.play(FadeOut(subjects))





        # text input
        texts = VGroup()
        texts.add(rt[0][3].copy(), rt[1][3].copy(),rt[2][3].copy(),rt[3][3].copy(),rt[4][3].copy(),rt[5][3].copy(),rt[6][3].copy(),
        rt[7][3].copy(),rt[8][3].copy(),rt[9][3].copy(),rt[10][3].copy(),rt[11][3].copy(),rt[12][3].copy(),rt[13][3].copy(),rt[14][3].copy(),
        rt[15][3].copy(),rt[16][3].copy(),rt[17][3].copy(),rt[18][3].copy(),rt[19][3].copy(),rt[22].copy(), rt[59].copy(),rt[60].copy(),
        rt[61].copy(),rt[62].copy(),rt[63].copy(),rt[64].copy(),rt[65].copy(),rt[66].copy(),rt[67].copy(),rt[68].copy(),rt[69].copy(),
        rt[106].copy(),rt[113].copy(),rt[120].copy(),rt[127].copy(),rt[134].copy(),rt[141].copy(),rt[148].copy())
        self.play(FadeIn(texts), FadeOut(rt), run_time = 2)
        self.play(texts.animate.shift(LEFT*5))
        self.wait(2)



        # Preprocessing text Show dataframe scalar_height, scalar_width, vector_size, matrix_size, stroke_size, col
        texts_preprocess = get_rectangle(1, 7, 1, 20, 0.5, WHITE).center().shift(DOWN*0.8).shift(LEFT*2.5)

        textpre = ['Processed text(处理好的句子)',
            'emotional eating is associated with', 
                'yet empirical evidence for indivi', 
                'the aim of this study was to test if at', 
                'it was expected that emotional eati',
                'participants were randomly assigned',
                'attentional biases for high calori',
                'self reported emotional eating wa',
                'hierarchical multivariate regres',
                'yet attention maintenance on food',
                'the current findings show that self',
                'results further suggest that atten',
                '...',
                'working alarms per home rose',
                'full education and practice',
                'without exceeding typical fire',
                'hands on practive is key',
                'two years after installation',
                'www clinicaltrials gov number']

        for i,t in enumerate(textpre):
            texts_preprocess.add(Text(t, color= BLACK).scale(0.7).move_to(texts_preprocess[i][0].get_center()))        
        texts_preprocess.scale(0.25)

        texts_copy = texts.copy()

        self.play(Transform(texts_copy, texts_preprocess), run_time = 2)



        # text vectorization 
        tvdf = get_rectangle(1, 3, 2, 20, 0.5, WHITE).center().shift(DOWN*0.8)#.shift(RIGHT*1.5)
        onehotindex = ['0',	 '1',	 '2',	 '3',	 '4',	'5','6','7','8','9','10', '...','64833','64834',	'64835', '64836', '64837', '64838', '64839', '64840']
        onehotwords = ['the',  'and',  'of',  'in',  'to',  'with',  'a',  'were',  'was',  'for',  'patients',  '...',  'noted',  'associations',  'little',  'count',  'signs',  'met',  'toxicity',  'multivariate']
        for i,t in enumerate(onehotwords):
            tvdf.add(Text(t, color= BLACK).scale(0.7).move_to(tvdf[i][0].get_center()))
        for i,t in enumerate(onehotindex):
            tvdf.add(Text(t, color= BLACK).scale(0.7).move_to(tvdf[i][1].get_center()))

        texts_preprocess_copy = VGroup()
        texts_preprocess_copy.add(texts_preprocess[21].copy(),
                                texts_preprocess[22].copy(),
                                texts_preprocess[23].copy(),
                                texts_preprocess[24].copy(),
                                texts_preprocess[25].copy(),
                                texts_preprocess[26].copy(),
                                texts_preprocess[27].copy(),
                                texts_preprocess[28].copy(),
                                texts_preprocess[29].copy(),
                                texts_preprocess[30].copy(),
                                texts_preprocess[31].copy(),
                                texts_preprocess[32].copy(),
                                texts_preprocess[33].copy(),
                                texts_preprocess[34].copy(),
                                texts_preprocess[35].copy(),
                                texts_preprocess[36].copy(),
                                texts_preprocess[37].copy(),
                                texts_preprocess[38].copy())


        self.wait(2)
        self.play(Transform(texts_preprocess_copy, tvdf.scale(0.25)), run_time = 2)
        self.wait(2)
        tvdf_2 = tvdf.copy()


        # vectorized text
        text_vec_df = get_rectangle(1, 7, 1, 20, 0.5, WHITE).center().shift(DOWN*0.8).shift(RIGHT*2.5)
        textpre = ['Vectorized text (矢量化文本)', 
        '3432  123  65  4332  5  ...', 
        '877  653  37  9  97  ...', 
        '0  122  2  98  12234  8  4 30 54 78', 
        '13  8  143  222  3432  246  ...',
        '15431  7  23423  44321  ...',
        '55443  14448  9  2663  2345  ...',
        '421  886  3432  123  165  ...',
        '56678  64840  322  ...',
        '877  2352  1242  11  19  ...',
        '0  3221  45  53  1651  421  ...',
        '8665  5678  14242  1651  1412  ...',
        '...',
        '584  21421  242  4236  1231  ...',
        '2535  24321  1  4436  ...',
        '2344  24512  2414  42155  ...',
        '1229  11  4344  65  345  ...',
        '23523  2442  3636  3151  ...',
        '61544  4347  34634  5236  ...']

        for i,t in enumerate(textpre):
            text_vec_df.add(Text(t, color= BLACK).scale(0.7).move_to(text_vec_df[i].get_center()))

        text_vec_df.scale(0.25)

        self.play(Transform(tvdf_2, text_vec_df), run_time = 2)
        self.wait(2)






        # highlight - 通常pre- process 会去掉大小写， 去掉特殊字符，去掉数字，  去掉标调符号， 有些时候回去掉stopwords 和数字等等
        tprta1 = Rectangle(height= 0.5,width = 0.5, color = YELLOW,).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(texts_preprocess[2].get_left()).shift(RIGHT*0.07)
        tprta2 = Rectangle(height= 0.4,width = 1.5, color = YELLOW,).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(texts_preprocess[5].get_center()).shift(LEFT*0.1)
        tprta3 = Rectangle(height= 0.4,width = 0.3, color = YELLOW,).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(texts_preprocess[16].get_center()).shift(RIGHT*0.7)

        tprta1c = Rectangle(height= 0.5,width = 0.5, color = YELLOW,).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(texts[2].get_left()).shift(RIGHT*0.06)
        tprta2c = Rectangle(height= 0.7,width = 1.9, color = YELLOW,).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(texts[5].get_center()).shift(LEFT*0.1)
        tprta3c = Rectangle(height= 0.4,width = 0.3, color = YELLOW,).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(texts[16].get_center()).shift(RIGHT*0.7)
        
        self.play(FadeIn(tprta1),FadeIn(tprta1c))
        self.wait(2)
        self.play(Transform(tprta1, tprta2), Transform(tprta1c, tprta2c), run_time = 2)    
        self.wait(1)
        self.play(Transform(tprta1, tprta3), Transform(tprta1c, tprta3c), run_time = 2)     
        self.wait(2)







        # 介绍比如 for 转换成了9 
        hightlight_for_9 = Rectangle(height= 1,width = 6, color = YELLOW).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(tvdf[9].get_center())
        tprta4 = Rectangle(height= 0.6,width = 0.8, color = YELLOW,).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(texts_preprocess[2].get_center()).shift(RIGHT*0.42)
        tprta4c = Rectangle(height= 0.6,width = 0.6, color = YELLOW,).set_stroke(color=BLACK, width=1).scale(0.25).set_opacity(0.5).shift(text_vec_df[2].get_center()).shift(RIGHT*0.17)
        self.play(Transform(tprta1, tprta4), Transform(tprta1c, tprta4c), FadeIn(hightlight_for_9), run_time = 2)     
        self.wait(2)

        self.play(FadeOut(tprta1), FadeOut(tprta1c), FadeOut(hightlight_for_9))

        # embedded text
        embedded_df = get_rectangle(1, 7, 1, 20, 0.5, WHITE).center().shift(DOWN*0.8).shift(RIGHT*5)
        textpre2 = ['Embedded text (向量化文本)', 
        '-0.015  0.028  ...  -0.03  0.033', 
        '-0.037  0.012  ...  0.010  0.012', 
        '-0.034  0.005  ...  0.047  0.012', 
        '-0.031  0.001  ...  0.003  -0.06',
        '0.0312  0.001  ...  0.003  -0.00',
        '0.9822  -0.31  ...  0.244  0.098',
        '0.2121  -0.04  ...  0.123  0.165',
        '0.3325  -0.52  ...  -0.12  -0.521',
        '0.7545  -0.37  ...  0.976  0.753',
        '0.4363  -0.46  ...  0.548  0.546',
        '0.1232  -0.36  ...  0.236  0.548',
        '...',
        '0.8564  -0.45  ...  -0.23  0.214',
        '0.5334  -0.21  ...  0.867  0.325',
        '0.2133  0.042  ...  0.453  0.234',
        '0.1242  -0.12  ...  -0.23  0.573',
        '-0.123  0.422  ...  0.245  0.356',
        '0.124·  -0.12  ...  0.556  -0.214']

        for i,t in enumerate(textpre2):
            embedded_df.add(Text(t, color= BLACK).scale(0.7).move_to(embedded_df[i].get_center()))

        embedded_df.scale(0.25)
        text_vec_df_2 = text_vec_df.copy()
        self.play(Transform(text_vec_df_2, embedded_df), run_time = 2)
        self.wait(3)



        # 做好了text input，基本上成功一办了, 我们再来回顾一下
        self.play(FadeOut(texts_copy), FadeOut(texts_preprocess), FadeOut(texts_preprocess_copy), FadeOut(tvdf), FadeOut(tvdf),FadeOut(tvdf_2),FadeOut(text_vec_df),FadeOut(text_vec_df_2),FadeOut(embedded_df))
        self.play(texts.animate.shift(RIGHT*5))
        self.play(FadeIn(rt))
        self.wait(2)
        self.play(FadeOut(texts))



        ''' 拿出来所有的 subject, text, line number, total lines '''
        # subject
        rt2.scale(0.37).move_to(rt[0][2].get_center()).shift(UP*1.25).shift(LEFT*0.05)
        
        # Text -> scale 0.3
        embedded_df.scale(0.38).move_to(rt[0][3].get_center()).shift(UP*1.25)

        # Play text & subject together
        self.play(FadeIn(rt2), run_time = 1)
        self.play(FadeIn(embedded_df), run_time = 1)


        # line number one-hot
        lnoh = get_rectangle(1, 5, 6, 20, 0.5, WHITE).center().shift(RIGHT*1).shift(DOWN*0.8)
        indexlist = ['0','1','2','3','4','5','6','7','8','9','10','...',"180034","180035","180036","180037","180038","180039","180040 rows x 5 columns"]
        for i,t in enumerate(indexlist):
            
            if i == 18:
                lnoh.add(Text(t).set_color(BLACK).scale(0.80).shift(lnoh[i+1][0].get_center()).shift(RIGHT*0.52))
            else:
                lnoh.add(Text(t).set_color(BLACK).scale(0.80).shift(lnoh[i+1][0].get_center()))    

        oh0 = ['1','0','0','0','0','0','0','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh0):
            lnoh.add(Text(t).set_color(BLACK).scale(0.80).shift(lnoh[i+1][1].get_center()))
            
        oh1 = ['0','1','0','0','0','0','0','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh1):
            lnoh.add(Text(t).set_color(BLACK).scale(0.80).shift(lnoh[i+1][2].get_center()))

        oh2 = ['...','...','...','...','...','...','...','...','...','...','...','...','...','...','...','...','...','...']
        for i,t in enumerate(oh2):
            lnoh.add(Text(t).set_color(BLACK).scale(0.80).shift(lnoh[i+1][3].get_center()))

        oh3 = ['0','0','0','0','0','0','0','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh3):
            lnoh.add(Text(t).set_color(BLACK).scale(0.80).shift(lnoh[i+1][4].get_center()))

        oh4 = ['0','0','0','0','0','0','0','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh4):
            lnoh.add(Text(t).set_color(BLACK).scale(0.80).shift(lnoh[i+1][5].get_center()))

        title2 = ['1', '2', '...', '30', '31']
        for i,t in enumerate(title2):
            lnoh.add(Text(t, color= BLACK).scale(0.7).move_to(lnoh[0][i+1].get_center()))
        lnoh.scale(0.09).move_to(rt[0][4].get_center()).shift(UP*1.25)  
        self.play(FadeIn(lnoh), run_time = 2)



        # total lines one-hot
        tloh = get_rectangle(1, 5, 6, 20, 0.5, WHITE).center().shift(RIGHT*1).shift(DOWN*0.8)

        for i,t in enumerate(indexlist):
            
            if i == 18:
                tloh.add(Text(t).set_color(BLACK).scale(0.80).shift(tloh[i+1][0].get_center()).shift(RIGHT*0.52))
            else:
                tloh.add(Text(t).set_color(BLACK).scale(0.80).shift(tloh[i+1][0].get_center()))    

        oh0 = ['0','0','0','0','0','0','0','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh0):
            tloh.add(Text(t).set_color(BLACK).scale(0.80).shift(tloh[i+1][1].get_center()))
            
        oh1 = ['1','1','1','1','1','1','1','1','1','1','1','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh1):
            tloh.add(Text(t).set_color(BLACK).scale(0.80).shift(tloh[i+1][2].get_center()))

        oh2 = ['...','...','...','...','...','...','...','...','...','...','...','...','...','...','...','...','...','...']
        for i,t in enumerate(oh2):
            tloh.add(Text(t).set_color(BLACK).scale(0.80).shift(tloh[i+1][3].get_center()))

        oh3 = ['0','0','0','0','0','0','0','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh3):
            tloh.add(Text(t).set_color(BLACK).scale(0.80).shift(tloh[i+1][4].get_center()))

        oh4 = ['0','0','0','0','0','0','0','0','0','0','0','...','0','0','0','0','0','0',]
        for i,t in enumerate(oh4):
            tloh.add(Text(t).set_color(BLACK).scale(0.80).shift(tloh[i+1][5].get_center()))

        title2 = ['10', '11', '...', '30', '31']
        for i,t in enumerate(title2):
            tloh.add(Text(t, color= BLACK).scale(0.7).move_to(tloh[0][i+1].get_center()))

        tloh.scale(0.09).move_to(rt[0][5].get_center()).shift(UP*1.25).shift(RIGHT*1)  
        self.play(FadeIn(tloh), run_time = 2)
       
    
        '''model input 放到左边， output 右边， 中间出来 neural network'''
        self.play(FadeOut(rt))     
        self.play(embedded_df.animate.scale(1.3).to_edge().shift(DOWN*0.35),
                lnoh.animate.scale(1.3).to_edge().shift(DOWN*2.8),
                tloh.animate.scale(1.3).to_edge().shift(DOWN*5.2),
                rt2.animate.scale(1.5).center().shift(RIGHT*4), run_time = 4)
        self.wait(2)

        # NN 3 inputs 
        ddinputs = VGroup()
        dli1 = get_rectangle(1, 1, 1, 9, 0.5, GREEN).scale(0.2).set_color(GREEN).set_stroke(BLACK, width=0.5).move_to(embedded_df.get_right())
        dli2 = get_rectangle(1, 1, 1, 9, 0.5, YELLOW).scale(0.2).set_color(YELLOW).set_stroke(BLACK, width=0.5).move_to(lnoh.get_right())
        dli3 = get_rectangle(1, 1, 1, 9, 0.5, RED).scale(0.2).set_color(RED).set_stroke(BLACK, width=0.5).move_to(tloh.get_right())

        # nn output 
        dli4 = get_rectangle(1, 1, 1, 5, 0.5, GREEN).scale(0.2).set_color(PURPLE).set_stroke(BLACK, width=0.5).move_to(rt2.get_left()).shift(LEFT*0.2)

        self.play(Transform(embedded_df, dli1), Transform(lnoh, dli2), Transform(tloh, dli3), Transform(rt2, dli4), run_time = 2)
        self.play(embedded_df.animate.shift(DOWN*0.5).shift(RIGHT*3))
        self.play(lnoh.animate.move_to(embedded_df.get_bottom()).shift(DOWN*0.9))
        self.play(tloh.animate.move_to(lnoh.get_bottom()).shift(DOWN*0.9))
        ddinputs.add(embedded_df, lnoh, tloh)
        #self.play(ddinputs)

        # nn 
        nns = get_nn([5,8,8,5],0.2,0.5).center().scale(0.5).shift(LEFT*0.4)
        self.play(FadeIn(nns))

        self.play(Transform(ddinputs, nns[0]), Transform(rt2, nns[3]), run_time = 2)
        self.play(FadeOut(ddinputs), FadeOut(rt2))
        self.play(nns.animate.scale(1.5))
        for _ in range(5):
            m = np.random.randint(5,139, 1)[0]
            #self.play(ShowPassingFlash(nns[n:n+6].copy().set_color(PINK), ), ShowPassingFlash(nns[n-6:n].copy()), runtime = 2)
            #self.play(Indicate(nns[m:m+6].copy(), scale_factor = 0), Indicate(nns[m-6:m].copy(), scale_factor = 0), runtime = 2, reverse=True)
            x = nns[m:m+10]
            y = nns[m:m+10].copy().set_color(np.random.choice(colors))
            self.play(Transform(x, y))
            self.play(FadeOut(y))
        self.wait(5)
