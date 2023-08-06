"""
Why only static method?

Why global state?

"""
from typing import List

df_chart_config = []

"""
Reset should be called primarily in the context of unittest to avoid race condition
 as chart_config is a global variable for this class.
"""


def reset():
    global df_chart_config
    df_chart_config = []


def bar_chart(name, x, y, data, expose_data=False):
    df_chart_config.append({
        'expose_data': expose_data,
        'kind': 'bar',
        'name': name,
        'options': {
            'x': x,
            'y': y,
            'data': data
        }
    })


def scatter_chart(name, x, y, data, expose_data=False):
    df_chart_config.append({
        'expose_data': expose_data,
        'kind': 'scatter',
        'name': name,
        'options': {
            'x': x,
            'y': y,
            'data': data
        }
    })


def pie_chart(name, legends, y, data):
    df_chart_config.append({
        'kind': 'pie',
        'name': name,
        'options': {
            'y': y,
            'legends': legends,
            'data': data
        }
    })


def line_chart(name, x, y, data, expose_data=False):
    df_chart_config.append({
        'expose_data': expose_data,
        'kind': 'line',
        'name': name,
        'options': {
            'x': x,
            'y': y,
            'data': data
        }
    })


def single_value(name, value, variation=None):
    df_chart_config.append({
        'kind': 'single_value',
        'name': name,
        'options': {
            'value': value,
            'variation': variation
        }
    })


def segment_line_chart(name, x, y, segment_column, data):
    df_chart_config.append({
        'kind': 'segment',
        'name': name,
        'options': {
            'x': x,
            'y': y,
            'segments': segment_column,
            'data': data
        }
    })


def time_series_forecast(name, forecasted_rows, data):
    df_chart_config.append({
        'kind': 'time_series',
        'name': name,
        'options': {
            'forecasted_rows': forecasted_rows,
            'data': data
        }
    })


def gauge_single_value(name, value, minimum, maximum, threshold_1=None, threshold_2=None):
    df_chart_config.append({
        'kind': 'single_value_gauge',
        'name': name,
        'options': {
            'value': value,
            'minimum': minimum,
            'maximum': maximum,
            'threshold_1': threshold_1,
            'threshold_2': threshold_2
        }
    })


def radial_polar_chart(name, x, y, segment_column, data):
    df_chart_config.append({
        'kind': 'radial_polar_chart',
        'name': name,
        'options': {
            'x': x,
            'y': y,
            'segments': segment_column,
            'data': data
        }
    })


def stacked_histogram(name, x, y_columns: List[str], data):
    df_chart_config.append({
        'kind': 'stacked_histogram',
        'name': name,
        'options': {
            'x': x,
            'y_columns': y_columns,
            'data': data
        }
    })


def clubbed_histogram(name, x, y_columns: List[str], data):
    df_chart_config.append({
        'kind': 'clubbed_histogram',
        'name': name,
        'options': {
            'x': x,
            'y_columns': y_columns,
            'data': data
        }
    })


def heat_map_dataframe(name, y, x_columns: List[str], data):
    df_chart_config.append({
        'kind': 'heat_map_dataframe',
        'name': name,
        'options': {
            'y': y,
            'x_columns': x_columns,
            'data': data
        }
    })
