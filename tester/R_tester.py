from draw_case_to_pic import draw_case_to_pic
from utils import HtmlLogger, get_signal_snippet, draw_ECG
from main_constructions import Program, AutomaticRealisation, ProgramRealisation
from formulas import RFormula

import matplotlib.pyplot as plt

def ideal_case(log):
    log.add_text("лучшая и наша совпали")
    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48

    v1 = signal[u1]
    v2 = signal[u2]
    v3 = signal[u3]

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2,
                        v1=v1, v2=v2,
                        du_from_parent=None)

    program.add_segment(name1=point_name1, name2=point_name3, parent_name_for1=None, abs_coord1=u1, abs_coord2=u3,
                        v1=v1, v2=v3,
                        du_from_parent=None)

    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)
    program_realisation.add(point_name=point_name1, point_coord_real=u1)
    program_realisation.add(point_name=point_name2, point_coord_real=u2)
    program_realisation.add(point_name=point_name3, point_coord_real=u3)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    plt.show()
    log.add_fig(fig)




def good_case(log):
    log.add_text("хорошая программа и хороший десктриптор")

    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    u1 = 80
    v1 = 210

    u2 = u1+40
    v2 = 0
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = u1 - 50
    v3 = 0
    program.add_segment(name1=point_name1, name2=point_name3, parent_name_for1=None, abs_coord1=u1, abs_coord2=u3, v1=v1, v2=v3,
                        du_from_parent=None)



    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)
    u1_real = 106
    u2_real = u1_real + 35
    u3_real = u1_real - 55
    program_realisation.add(point_name=point_name1, point_coord_real=u1_real)
    program_realisation.add(point_name=point_name2, point_coord_real=u2_real)
    program_realisation.add(point_name=point_name3, point_coord_real=u3_real)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    #plt.show()
    log.add_fig(fig)

def good_case2(log):
    log.add_text("хорошая программа и хороший десктриптор")

    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    u1 = 80
    v1 = 170

    u2 = u1+40
    v2 = 0
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = u1 - 50
    v3 = 0
    program.add_segment(name1=point_name1, name2=point_name3, parent_name_for1=None, abs_coord1=u1, abs_coord2=u3, v1=v1, v2=v3,
                        du_from_parent=None)



    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)
    u1_real = 106
    u2_real = u1_real + 35
    u3_real = u1_real - 55
    program_realisation.add(point_name=point_name1, point_coord_real=u1_real)
    program_realisation.add(point_name=point_name2, point_coord_real=u2_real)
    program_realisation.add(point_name=point_name3, point_coord_real=u3_real)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    log.add_fig(fig)

def bad_case1(log):
    log.add_text("плохая программа, хороший дескриптор }")

    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    u1 = 80
    v1 = -5

    u2 = u1+40
    v2 = 0
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = u1 - 50
    v3 = 0
    program.add_segment(name1=point_name1, name2=point_name3, parent_name_for1=None, abs_coord1=u1, abs_coord2=u3, v1=v1, v2=v3,
                        du_from_parent=None)



    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)
    u1_real = 106
    u2_real = u1_real + 35
    u3_real = u1_real - 55
    program_realisation.add(point_name=point_name1, point_coord_real=u1_real)
    program_realisation.add(point_name=point_name2, point_coord_real=u2_real)
    program_realisation.add(point_name=point_name3, point_coord_real=u3_real)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    log.add_fig(fig)


def bad_case2(log):
    log.add_text("плохая программа, непохожий десктриптор средней эффективности")

    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    u1 = 80
    v1 = -5

    u2 = u1+40
    v2 = 0
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = u1 - 50
    v3 = 0
    program.add_segment(name1=point_name1, name2=point_name3, parent_name_for1=None, abs_coord1=u1, abs_coord2=u3, v1=v1, v2=v3,
                        du_from_parent=None)



    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)
    u1_real = 80
    u2_real = u1_real + 35
    u3_real = u1_real - 55
    program_realisation.add(point_name=point_name1, point_coord_real=u1_real)
    program_realisation.add(point_name=point_name2, point_coord_real=u2_real)
    program_realisation.add(point_name=point_name3, point_coord_real=u3_real)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    log.add_fig(fig)


def bad_case3(log):
    log.add_text("плохая программа, похожий десктриптор плохой эффективности")

    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    u1 = 80
    v1 = -5

    u2 = u1+75
    v2 = 0
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = u1 - 50
    v3 = 0
    program.add_segment(name1=point_name1, name2=point_name3, parent_name_for1=None, abs_coord1=u1, abs_coord2=u3, v1=v1, v2=v3,
                        du_from_parent=None)



    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)
    u1_real = 80
    u2_real = u1_real + 80
    u3_real = u1_real - 55
    program_realisation.add(point_name=point_name1, point_coord_real=u1_real)
    program_realisation.add(point_name=point_name2, point_coord_real=u2_real)
    program_realisation.add(point_name=point_name3, point_coord_real=u3_real)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    log.add_fig(fig)

def bad_case4(log):
    log.add_text("избыточная программа - 3 сегмента")

    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    point_name4 = '4'
    u1 = 55
    v1 = 0

    u2 = 105
    v2 = 220
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = 125
    v3 = 100
    program.add_segment(name1=point_name2, name2=point_name3, parent_name_for1=None, abs_coord1=u2, abs_coord2=u3, v1=v2, v2=v3,
                        du_from_parent=None)

    u4 = 143
    v4 = 0
    program.add_segment(name1=point_name3, name2=point_name4, parent_name_for1=None, abs_coord1=u3, abs_coord2=u4,
                        v1=v3, v2=v4,
                        du_from_parent=None)

    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)
    u1_ = 56
    u2_ = 105
    u3_ = 125
    u4_ = 144
    program_realisation.add(point_name=point_name1, point_coord_real=u1_)
    program_realisation.add(point_name=point_name2, point_coord_real=u2_)
    program_realisation.add(point_name=point_name3, point_coord_real=u3_)
    program_realisation.add(point_name=point_name4, point_coord_real=u4_)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    #plt.show()
    log.add_fig(fig)

def bad_case5(log):
    log.add_text("избыточная программа - 4 сегмента")

    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    point_name4 = '4'
    point_name5 = '5'

    u1 = 55
    v1 = 0

    u2 = 105
    v2 = 220
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = 125
    v3 = 100
    program.add_segment(name1=point_name2, name2=point_name3, parent_name_for1=None, abs_coord1=u2, abs_coord2=u3, v1=v2, v2=v3,
                        du_from_parent=None)

    u4 = 143
    v4 = 0
    program.add_segment(name1=point_name3, name2=point_name4, parent_name_for1=None, abs_coord1=u3, abs_coord2=u4,
                        v1=v3, v2=v4,
                        du_from_parent=None)

    u5= 158
    v5=0

    program.add_segment(name1=point_name4, name2=point_name5, parent_name_for1=None, abs_coord1=u4, abs_coord2=u5,
                        v1=v4, v2=v5,
                        du_from_parent=None)

    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)

    program_realisation.add(point_name=point_name1, point_coord_real=u1)
    program_realisation.add(point_name=point_name2, point_coord_real=u2)
    program_realisation.add(point_name=point_name3, point_coord_real=u3)
    program_realisation.add(point_name=point_name4, point_coord_real=u4)
    program_realisation.add(point_name=point_name5, point_coord_real=u5)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    # plt.show()
    log.add_fig(fig)

def bad_case6(log):
    log.add_text("избыточная программа - 5 сегмента")

    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    point_name1 = '1'
    point_name2 = '2'
    point_name3 = '3'
    point_name4 = '4'
    point_name5 = '5'
    point_name6 = '6'

    u1 = 55
    v1 = 0

    u2 = 105
    v2 = 220
    program.add_segment(name1=point_name1, name2=point_name2, parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = 125
    v3 = 100
    program.add_segment(name1=point_name2, name2=point_name3, parent_name_for1=None, abs_coord1=u2, abs_coord2=u3, v1=v2, v2=v3,
                        du_from_parent=None)

    u4 = 143
    v4 = 0
    program.add_segment(name1=point_name3, name2=point_name4, parent_name_for1=None, abs_coord1=u3, abs_coord2=u4,
                        v1=v3, v2=v4,
                        du_from_parent=None)

    u5= 158
    v5=0

    program.add_segment(name1=point_name4, name2=point_name5, parent_name_for1=None, abs_coord1=u4, abs_coord2=u5,
                        v1=v4, v2=v5,
                        du_from_parent=None)

    u6 = 174
    v6= 0
    program.add_segment(name1=point_name5, name2=point_name6, parent_name_for1=None, abs_coord1=u5, abs_coord2=u6,
                        v1=v5, v2=v6,
                        du_from_parent=None)

    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:
    program_realisation = ProgramRealisation(program=program, signal=signal)

    program_realisation.add(point_name=point_name1, point_coord_real=u1)
    program_realisation.add(point_name=point_name2, point_coord_real=u2)
    program_realisation.add(point_name=point_name3, point_coord_real=u3)
    program_realisation.add(point_name=point_name4, point_coord_real=u4)
    program_realisation.add(point_name=point_name5, point_coord_real=u5)
    program_realisation.add(point_name=point_name6, point_coord_real=u6)

    # ЗАПОЛНЯЕМ АВТО-РЕАЛИЗИЮ:
    auto_realisation = AutomaticRealisation(signal=signal)
    u1 = 105
    u2 = u1 + 35
    u3 = u1 - 48
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u2)
    auto_realisation.add_segment(abs_coord1=u1, abs_coord2=u3)

    # логируем результат
    r_form = RFormula(program, realisation=program_realisation, auto_realisation=auto_realisation, signal=signal)
    r_form.calc_and_log(log)
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    # plt.show()
    log.add_fig(fig)

if __name__ == '__main__':
    log = HtmlLogger("TEST_T")
    ideal_case(log)
    good_case(log)
    good_case2(log)
    bad_case1(log)
    bad_case2(log)
    bad_case3(log)
    bad_case4(log)
    bad_case5(log)
    bad_case6(log)

