from .segment_info import SegmentInfo
from utils import IdGenedator
from interpolation1d import Interpolator, InderpolationInfo
from .program import Program


class AutomaticRealisation:
    def __init__(self, signal):
        self.signal = signal
        self.segments = []  # [ [abs_coord1, abs_coord2], [abs_coord1, abs_coord2], ....]

    def _to_interpolation_info(self):
        ii = InderpolationInfo()
        for i in range(len(self.segments)):
            segment = self.segments[i]
            abs_coord1 = segment[0]
            v1 = self.signal[abs_coord1]
            name1 = str(i) + "_1"
            ii.add(u=abs_coord1, v=v1, name=name1, parent_name=None, is_linked=False)

            abs_coord2 = segment[1]
            v2 = self.signal[abs_coord2]
            name2 = str(i) + "_2"
            ii.add(u=abs_coord2, v=v2, name=name2, parent_name=name1, is_linked=True)

        return ii

    def add_segment(self, abs_coord1, abs_coord2):
        self.segments.append([abs_coord1, abs_coord2])

    def draw(self, ax):
        ii = self._to_interpolation_info()
        interpolator = Interpolator(inderpolation_info=ii, signal_len=len(self.signal))
        interpolator.draw(ax, color='red', label="лучшая")

    def get_E(self):
        ii = self._to_interpolation_info()
        interpolator = Interpolator(inderpolation_info=ii, signal_len=len(self.signal))
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
        U = sum(us)
        V = sum(vs)
        return U, V
