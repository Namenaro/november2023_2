from utils import HtmlLogger
from main_constructions import Program, ProgramRealisation, AutomaticRealisation

from pandas import DataFrame
from copy import deepcopy
from statistics import mean, variance

class RFormula:
    def __init__(self, program, realisation, auto_realisation, signal):
        self.program = program
        self.realisation = realisation
        self.auto_realisation = auto_realisation
        self.signal = signal

        self.data={} # название переменной : значение     надо для лога значений переменных, входящих в формулу r

    def calc(self):
        signal_area = sum(self.signal)

        E_abs = self.auto_realisation.get_E()
        Us, Vs = self.auto_realisation.get_UV()
        N_segments = self.auto_realisation.get_num_segments()


        e_abs = self.realisation.get_e()
        us, vs = self.realisation.get_uv_dynamic() #TODO еще статический метод есть
        n_segments = self.program.get_num_segments()

        #расчет
        r = self.r_variant(signal_area=signal_area, E_abs=E_abs, Us=Us, Vs=Vs, N_segments=N_segments, e_abs=e_abs, us=us, vs=vs, n_segments=n_segments)

        #логирование


        self.data['U'] = sum(Us)
        self.data['u'] = sum(us)
        self.data['V'] = sum(Vs)
        self.data['v'] = sum(vs)
        #self.data['E_abs'] = E_abs
        #self.data['e_abs'] = e_abs
        #self.data['signal_area'] = signal_area
        self.data['N_segments'] = N_segments
        self.data['n_segments'] = n_segments

        return r

    def calc_and_log(self, log):
        self.calc()

        temp = {}
        for name, val in self.data.items():
            temp[name] = [val]

        data_frame = DataFrame.from_dict(temp)
        log.add_dataframe(data_frame)




    def r_variant2(self, signal_area, E_abs, Us, Vs, N_segments, e_abs, us, vs, n_segments):
        us_f = Us + us

        vs_f = Vs + vs

        normed_us = [ (u - min(us_f))/max(us_f) for u in us]
        normed_Us = [(u - min(us_f))/max(us_f) for u in Us]

        normed_vs = [(v - min(vs_f))/max(vs_f) for v in vs]
        normed_Vs = [(v - min(vs_f))/max(vs_f) for v in Vs]

        Effort = N_segments + sum(normed_Us) + sum(normed_Vs)
        effort = n_segments + sum(normed_us) + sum(normed_vs)


        sigma_profit = (E_abs - e_abs) / E_abs
        sigma_effort  = (Effort - effort)/Effort

        r = sigma_profit + sigma_effort

        # логирование
        self.data['r'] = r
        self.data['sigma_profit'] = sigma_profit
        self.data['sigma_effort'] = sigma_effort


        return r

    def r_variant(self, signal_area, E_abs, Us, Vs, N_segments, e_abs, us, vs, n_segments):
        us_f = Us + us

        vs_f = Vs + vs

        normed_us = [(u - min(us_f)) / max(us_f) for u in us]
        normed_Us = [(u - min(us_f)) / max(us_f) for u in Us]

        normed_vs = [(v - min(vs_f)) / max(vs_f) for v in vs]
        normed_Vs = [(v - min(vs_f)) / max(vs_f) for v in Vs]

        U = N_segments + sum(normed_Us)
        V = N_segments + sum(normed_Vs)
        u = n_segments + sum(normed_us)
        v = n_segments + sum(normed_vs)


        sigma_profit = (E_abs - e_abs) / E_abs
        sigma_u = (U-u)/U
        sigma_v = (V-v)/V

        r = sigma_profit + sigma_u + sigma_v

        # логирование
        self.data['r'] = r
        self.data['sigma_profit'] = sigma_profit
        self.data['sigma_u'] = sigma_u
        self.data['sigma_v'] = sigma_v

        return r


