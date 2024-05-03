# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX data into a pandas DataFrame
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the application
app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    
    # Launch Site Dropdown
    html.Div([
        html.Label('Launch Site Selection:', style={'font-weight': 'bold'}),
        dcc.Dropdown(
            id='site-dropdown',
            options=[
                {'label': 'All Sites', 'value': 'ALL'},
                {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
            ],
            value='ALL',
            placeholder="Select a Launch Site",
            searchable=True
        )
    ]),

    # Success Pie Chart
    html.Div([
        html.Label('Success Pie Chart:', style={'font-weight': 'bold'}),
        dcc.Graph(id='success-pie-chart')
    ]),
    
    # Payload Range Slider
    html.Div([
        html.Label('Payload Range (Kg):', style={'font-weight': 'bold'}),
        dcc.RangeSlider(
            id='payload-slider',
            min=0, max=10000, step=1000,
            value=[min_payload, max_payload]
        )
    ]),

    # Success Payload Scatter Chart
    html.Div([
        html.Label('Success Payload Scatter Chart:', style={'font-weight': 'bold'}),
        dcc.Graph(id='success-payload-scatter-chart')
    ])
])

# Define the callback function for updating the success pie chart
@app.callback(Output(component_id='success-pie-chart', component_property='figure'),
               Input(component_id='site-dropdown', component_property='value'))
def update_pie_chart(entered_site):
    filtered_df = spacex_df
    if entered_site != 'ALL':
        filtered_df = filtered_df[filtered_df['Launch Site'] == entered_site]
    fig = px.pie(filtered_df, names='class', 
                 title=f'Total Success Launches for {entered_site}' if entered_site != 'ALL' else 'Total Success Launches by Site')
    return fig

# Define the callback function for updating the success payload scatter chart
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='figure'),
              [Input(component_id='site-dropdown', component_property='value'), 
               Input(component_id="payload-slider", component_property="value")])
def update_scatter_plot(entered_site, payload):
    filtered_df = spacex_df
    if entered_site != 'ALL':
        filtered_df = filtered_df[(filtered_df['Launch Site']==entered_site) \
                                  & (filtered_df['Payload Mass (kg)'] >= payload[0]) \
                                  & (filtered_df['Payload Mass (kg)'] <= payload[1])]
    fig = px.scatter(filtered_df, x='Payload Mass (kg)', y="class", 
                     color="Booster Version Category",
                     title=f'Correlation between Payload and Success for {entered_site}' if entered_site != 'ALL' else 'Correlation between Payload and Success for all Sites')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server()
