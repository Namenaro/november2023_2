from draw_case_to_pic import draw_case_to_pic
from utils import HtmlLogger, get_signal_snippet, draw_ECG
from main_constructions import Program, AutomaticRealisation, ProgramRealisation

import matplotlib.pyplot as plt


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
    fig = draw_case_to_pic(signal, program, program_realisation, auto_realisation)
    log.add_fig(fig)


if __name__ == '__main__':
    log = HtmlLogger("TEST_T")
    good_case(log)
