import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import psutil
import time

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='live-update-graph'),
    dcc.Interval(id='interval-component', interval=1*1000, n_intervals=0)
])

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    cpu_usage = psutil.cpu_percent(interval=1)

    return {
        'data': [go.Scatter(x=[time.time()], y=[cpu_usage], mode='lines+markers')],
        'layout': go.Layout(title='Live CPU Usage')
    }

if __name__ == '__main__':
    app.run_server(debug=True)
