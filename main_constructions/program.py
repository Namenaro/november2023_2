from segment_info import SegmentInfo
from utils import IdGenedator
from interpolation1d import Interpolator, InderpolationInfo


class Program:
    def __init__(self):
        self.seg_names_generator = IdGenedator(prefix="seg_")

        self.segments_order = []  # [segment_name1, segment_name2,...]
        self.names_to_segments_ifo = {}  # segment_name: SegmentInfo

    def add_segment(self, name1, name2, parent_name_for1, abs_coord1, abs_coord2, v1, v2, du_from_parent):
        seg_name = self.seg_names_generator.get_id()
        segment_ifo = SegmentInfo(name1, name2, parent_name_for1, abs_coord1, abs_coord2, v1, v2, du_from_parent)
        self.names_to_segments_ifo[seg_name] = segment_ifo

    def draw(self, signal_len, ax):
        ii = InderpolationInfo()

        for segment_name in self.segments_order:
            seg_info = self.names_to_segments_ifo[segment_name]
            ii.add(u=seg_info.abs_coord1, v=seg_info.v1, name=seg_info.name1, parent_name=seg_info.parent_name_for1, is_linked=False)
            ii.add(u=seg_info.abs_coord2, v=seg_info.v2, name=seg_info.name2, parent_name=seg_info.name1, is_linked=True)

        interpolator = Interpolator(inderpolation_info=ii, signal_len=signal_len)
        interpolator.draw(ax, color='blue', label="программа")
