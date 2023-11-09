import matplotlib.pyplot as plt

from .interpolation_info import InderpolationInfo
from .segment import InterpolationSegment


class Interpolator:
    def __init__(self, inderpolation_info, signal_len):
        self.signal_len = signal_len
        self.interpolation_info = inderpolation_info

        self.coords_to_predictions = {}  # над любой точкой сцены самое новое предсказание (хронологичски добавленное)

        for coord in range(signal_len):
            self.coords_to_predictions[coord] = 0

        self._fill_prediction()

    def get_interpolation(self):
        pointwise_prediction = []
        for coord in range(self.signal_len):
            pointwise_prediction.append(self.coords_to_predictions[coord])
        return pointwise_prediction

    def _register_new_segment(self, index1, v1, index2, v2):
        seg = InterpolationSegment(index1, v1, index2, v2)
        vals = seg.get_vals_from_left()
        indexes = seg.get_indexes_from_left()

        for i in range(len(vals)):
            coord = indexes[i]
            val = vals[i]

            self.coords_to_predictions[coord] = val

    def _fill_prediction(self):
        for name in self.interpolation_info.order:

            v = self.interpolation_info.names_to_points[name].v
            u = self.interpolation_info.names_to_points[name].u

            self.coords_to_predictions[u] = v


            parent_name = self.interpolation_info.names_to_parents_names[name]
            if parent_name is not None:
                if self.interpolation_info.names_to_parent_linking[name]:
                    parent_u = self.interpolation_info.names_to_points[parent_name].u
                    parent_v = self.interpolation_info.names_to_points[parent_name].v
                    self._register_new_segment(index1=u, v1=v, index2=parent_u, v2=parent_v)

    def draw(self, ax, color, label=None):
        pointwise_prediction = self.get_interpolation()

        ax.plot(pointwise_prediction, 'o-',  c=color, markersize=2, alpha=0.5, label=label)

        for name in self.interpolation_info.order:
            v = self.interpolation_info.names_to_points[name].v
            u = self.interpolation_info.names_to_points[name].u
            ax.scatter(u, v, c=color)
            ax.annotate(str(name), (u, v), xytext=(5, 2), c=color, textcoords='offset points',  weight='bold')
        plt.legend()

