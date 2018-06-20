import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('al.csv')
df.reset_index()
df['text']=df['Country']+' '+df['Product']
app.layout = html.Div([
    dcc.Graph(
        id='1995 Feb',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['Country'] == i]['2018 Feb'],
                    y=df[df['Country'] == i]['text'],
                    text=df[df['Country'] == i]['text'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.Country.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'WBMS Production by Country in 2018 Feb'},
                yaxis={'title': 'Production'},
                margin={'l': 100, 'b': 40, 't':50, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    
    app.run_server()