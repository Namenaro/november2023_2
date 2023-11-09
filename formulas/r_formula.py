from utils import HtmlLogger
from main_constructions import Program, ProgramRealisation, AutomaticRealisation

from pandas import DataFrame
from copy import deepcopy

class RFormula:
    def __init__(self, program, realisation, auto_realisation):
        self.program = program
        self.realisation = realisation
        self.auto_realisation = auto_realisation

        self.data={} # название переменной : значение     надо для лога значений переменных, входящих в формулу r

    def calc(self):
        E = self.auto_realisation.get_E()
        U, V = self.auto_realisation.get_UV()

        e = self.realisation.get_e()
        u, v = self.realisation.get_uv_dynamic() #TODO еще статический метод есть

        #расчет
        sigma_e = (E - e) / E
        sigma_u = (U-u)/U
        sigma_v = (V-v) / V

        r = sigma_v + sigma_u + sigma_e


        #логирование
        self.data['r'] = r
        self.data['sigma_u'] = sigma_u
        self.data['sigma_v'] = sigma_v
        self.data['sigma_e'] = sigma_e
        return r

    def calc_and_log(self, log):
        self.calc()

        temp = {}
        for name, val in self.data.items():
            temp[name] = [val]

        data_frame = DataFrame.from_dict(temp)
        log.add_dataframe(data_frame)

