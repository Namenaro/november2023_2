from .segment_info import SegmentInfo
from utils import IdGenedator
from interpolation1d import Interpolator
from .program import Program


class AutomaticRealisation:
    def __init__(self, signal):
        self.signal = signal
        self.segments = []  # [ [abs_coord1, abs_coord2], [abs_coord1, abs_coord2], ....]



    def _to_interpolator(self):
        interp = Interpolator(signal_len=len(self.signal))
        for i in range(len(self.segments)):
            segment = self.segments[i]
            abs_coord1 = segment[0]
            v1 = self.signal[abs_coord1]
            name1 = str(i) + "_1"


            abs_coord2 = segment[1]
            v2 = self.signal[abs_coord2]
            name2 = str(i) + "_2"

            interp.add_new_segment(index1=abs_coord1, v1=v1, index2=abs_coord2, v2=v2, name1=name1, name2=name2)


        return interp

    def add_segment(self, abs_coord1, abs_coord2):
        self.segments.append([abs_coord1, abs_coord2])

    def draw(self, ax):

        interpolator = self._to_interpolator()
        interpolator.draw(ax, color='red', label="лучшая")

    def get_E(self):
        interpolator = self._to_interpolator()

        prediction = interpolator.get_interpolation()
        es = list([abs(self.signal[i] - prediction[i]) for i in range(len(prediction))])
        E = sum(es)
        return E

    def get_UV(self):
        us = []
        vs = []

        auto_u = len(self.signal) / 2
        auto_v = 0

        for segment in self.segments:
            u1 = segment[0]
            u2 = segment[1]
            v1 = self.signal[u1]
            v2 = self.signal[u2]

            err_u1 = abs(auto_u - u1)
            err_u2 = abs(auto_u - u2)

            err_v1 = abs(v1 - auto_v)
            err_v2 = abs(v2 - auto_v)

            us.append(err_u1 + err_u2)
            vs.append(err_v1 + err_v2)

        return us, vs

    def get_num_segments(self):
        return len(self.segments)



