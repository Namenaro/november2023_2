from draw_case_to_pic import draw_case_to_pic
from utils import HtmlLogger, get_signal_snippet, draw_ECG
from main_constructions import Program, AutomaticRealisation, ProgramRealisation

import matplotlib.pyplot as plt


def good_case(log):
    log.add_text("хорошая программа и хороший десктриптор")
    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    # СОСТАВЛЯЕМ ПРОГРАММУ:
    program = Program()
    u1 = 80
    v1 = 210

    u2 = u1+40
    v2 = 0
    program.add_segment(name1='1', name2='2', parent_name_for1=None, abs_coord1=u1, abs_coord2=u2, v1=v1, v2=v2,
                        du_from_parent=None)

    u3 = u1 - 50
    v3 = 0
    program.add_segment(name1='1', name2='3', parent_name_for1=None, abs_coord1=u1, abs_coord2=u3, v1=v1, v2=v3,
                        du_from_parent=None)

    # ЗАПОЛНЯЕМ РЕАЛИЗАЦИЮ ЭТОЙ ПРОГРАММЫ:



    #fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    #log.add_fig(fig)


if __name__ == '__main__':
    log = HtmlLogger("TEST_T")


    good_case(log)
