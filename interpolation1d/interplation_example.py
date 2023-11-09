from interpolation1d import Interpolator, InderpolationInfo
from utils import HtmlLogger, get_signal_snippet, draw_ECG
import matplotlib.pyplot as plt

if __name__ == '__main__':
    signal = get_signal_snippet(lead_name='i', start_coord=243, end_coord=435)

    ii = InderpolationInfo()

    u1 = 80
    ii.add(u=u1, v=210, name='1')
    u12 = u1+40
    ii.add(u=u12, v=0, name='2', parent_name='1', is_linked=True)

    u13 = u1-50
    ii.add(u=u13, v=0, name='3', parent_name='1', is_linked=True)


    fig, ax = plt.subplots()
    draw_ECG(ax, signal)
    Interpolator(ii, signal_len=len(signal)).draw(ax, color='red')
    plt.show()

