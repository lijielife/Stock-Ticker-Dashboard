import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web
from datetime import datetime
# import pandas
import pandas as pd

app = dash.Dash()
# read a .csv file, make a dataframe, and build a list of Dropdown options
wbms = pd.read_csv('aa.csv', header=None)
wbms.set_index(0, inplace=True)
options = []
optionsdate = []
for country in wbms.index:
    options.append({'label':'{}'.format(country), 'value':country})
for date in wbms.iloc[0]:
    optionsdate.append({'label':'{}'.format(date), 'value': date})
app.layout = html.Div([
    html.H1('WBMS Dashboard'),
    html.Div([
        html.H3('Select WBMS country:', style={'paddingRight':'30px'}),
        # replace dcc.Input with dcc.Options, set options=options
        dcc.Dropdown(
            id='my_WBMS_country',
            options=options,
            value=['U.S.A.'],
            multi=True
        )
    # widen the Div to fit multiple inputs
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    html.Div([
        html.H3('Select date:', style={'paddingRight':'30px'}),
        dcc.Dropdown(
            id='my_date',
            #min_date_allowed=datetime(2015, 1, 1),
            #max_date_allowed=datetime.today(),
            #start_date=datetime(2018, 1, 1),
            #end_date=datetime.today()
            options=optionsdate,
            value=['1995 Jan'],
            
        )
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    html.Div([
        html.Button(
            id='submit-button',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'30px'}
        ),
    ], style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph',
        figure={
        'data': [
                {'x': wbms.index, 'y': [3,1]}
            ]
        }
    )
])

@app.callback(
    Output('my_graph', 'figure'),
    [Input('submit-button', 'n_clicks')],
    [State('my_WBMS_country', 'value'),
    State('my_date', 'value')])

def update_graph(selected_country, selected_date):
    return u'{} is a city in'.format(
        selected_city, selected_country,
    )

if __name__ == '__main__':
    app.run_server()