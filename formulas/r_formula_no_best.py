from utils import HtmlLogger
from main_constructions import Program, ProgramRealisation, AutomaticRealisation

from pandas import DataFrame
from copy import deepcopy
from statistics import mean, variance

class RFormulaNoAuto:
    def __init__(self, program, realisation, signal):
        self.program = program
        self.realisation = realisation
        self.signal = signal

        self.val_sample = self.fill_val_sample()
        self.real_val = self.get_real_val()
        self.data = {} # название переменной : значение     надо для лога значений переменных, входящих в формулу r

    def get_random_chord(self):

        return u1, u2, v1, v2, error

    def norm_u(self, u):
        return u_normed

    def norm_v(self, v):
        return v_normed

    def norm_err(self, err):
        return err_normed

    def get_real_val(self):
        return real_val

    def get_normed_effort(self, u1, u2, v1, v2):
        return normed_effort

    def get_p_of_so_good(self):
        return p

    def fill_val_sample(self):
        N = 100

        for i in range(N):
            u1, u2, v1, v2, error = self.get_random_chord()
            normed_effort = self.get_normed_effort(u1, u2=u2, v1=v1, v2=v2)
            normed_err_profit = self.norm_err(error)
            val = normed_err_profit + normed_effort
            self.val_sample.append(val)

    def r_variant(self):
        r = self.get_p_of_so_good()
        return r

    def draw_distr(self, ax):
        # рисуем гистограмму
        pass