import plotly.express as px
import plotly.graph_objects as go

from tsp import TSP


def simple_timeseries(t: TSP):

    chart = px.line(t.long,
               x = 'time',
               y = 'temperature_in_ground',
               line_group = 'depth')

    return chart
