from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc
import settings as st
import plotly.io as pio


pio.templates['custom'] = pio.templates['plotly'].update(
    layout=dict(colorway=st.MY_PALETTE)
)
pio.templates.default = "custom"



def register_callbacks(app):
    @app.callback(
        Output('air-output', 'children'),
        Output('co-graph', 'figure'),
        Output('no2-graph', 'figure'),
        Output('o3-graph', 'figure'),
        Output('so2-graph', 'figure'),
        Output('pm2_5-graph', 'figure'),
        Output('pm10-graph', 'figure'),
        Input('city-input', 'value')
    )

    def update_dashboard(city):
        data = load_data(city)

        air_info = html.Div([
            html.H4(
    f"Состояние воздуха в городе {data['city_name']} сейчас:",
    className="card-title",
    style={"font-size": "20px", "font-weight": "normal",  "text-shadow": "1px 1px 0 black", "line-height": "2"}
),
            html.H5(
    [
        "🏭 Концентрация оксида углерода (CO) в воздухе: ",
        html.Span(
            f"{data['co_curr']}", 
            style={"color": "#5D3FD3"}  
        ),
        " мг/м³"
    ],
    className="card-title",
    style={"font-size": "16px", "font-weight": "normal", "line-height": "1"}
),

            html.H5(
    [
        "☁︎ Концентрация диоксида азота (NO2) в воздухе: ",
        html.Span(
            f"{data['no2_curr']}", 
            style={"color": "#5D3FD3"} 
        ),
        " мг/м³"
    ],
    className="card-title",
    style={"font-size": "16px", "font-weight": "normal", "line-height": "1"}
),

            html.H5(
    [
        "⚡ Концентрация озона (O3) в воздухе: ",
        html.Span(
            f"{data['o3_curr']}", 
            style={"color": "#5D3FD3"}  
        ),
        " мг/м³"
    ],
    className="card-title",
    style={"font-size": "16px", "font-weight": "normal", "line-height": "1"}
),

            html.H5(
    [
        "😶‍🌫 Концентрация углекислого газа (CO₂) в воздухе: ",
        html.Span(
            f"{data['so2_curr']}", 
            style={"color": "#5D3FD3"} 
        ),
        " ppm"
    ],
    className="card-title",
    style={"font-size": "16px", "font-weight": "normal", "line-height": "1"}
),
            html.H5(
    [
        "🌪️ Концентрация микроскопических частиц в воздухе: ",
        html.Span(
            f"{data['pm2_5_curr']}", 
            style={"color": "#5D3FD3"}  
        ),
        " мкг/м³"
    ],
    className="card-title",
    style={
        "font-size": "16px", 
        "font-weight": "normal", 
        "line-height": "1"
    }
),
         html.H5(
    [
        "🪨 Концентрация крупной пыли в воздухе: ",
        html.Span(
            f"{data['pm10_curr']}",
            style={"color": "#5D3FD3"} 
        ),
        " мкг/м³"
    ],
    className="card-title",
    style={
        "font-size": "16px", 
        "font-weight": "normal", 
        "line-height": "1"
    }
),

        ])


        co_fig = go.Figure(
           data=[
               go.Scatter(
               x=data['hours'], 
               y=data['co'], 
               mode='lines+markers', 
               name='Концентрация оксида углерода (CO)', 
               line=dict(color='rebeccapurple'), 
               marker=dict(size=8))],
           layout=go.Layout(
               title=dict(
                   text='Концентрация оксида углерода (CO)', 
                   x=0.5,
                   font=dict(size=17)
                   ),
                   xaxis_title='Время', 
                   yaxis_title='(CO), мг/м³', 
                   plot_bgcolor='rgba(0, 255, 255, 0.13)',
                   paper_bgcolor='rgba(0, 0, 0, 0)',
                   margin=dict(l=40, r=40, t=60, b=40)))


        no2_fig = go.Figure(
           data=[
               go.Scatter(
               x=data['hours'], 
               y=data['no2'], 
               mode='lines+markers', 
               name='Концентрация диоксида азота (NO2)', 
               line=dict(color='rebeccapurple'), 
               marker=dict(size=8))],
           layout=go.Layout(
               title=dict(
                   text='Концентрация диоксида азота (NO2)', 
                   x=0.5,
                   font=dict(size=17)
                   ),
                   xaxis_title='Время', 
                   yaxis_title='(NO2), мг/м³', 
                   plot_bgcolor='rgba(0, 255, 255, 0.13)',
                   paper_bgcolor='rgba(0, 0, 0, 0)',
                   margin=dict(l=40, r=40, t=60, b=40)))
        


        o3_fig = go.Figure(
           data=[
               go.Scatter(
               x=data['hours'], 
               y=data['o3'], 
               mode='lines+markers', 
               name='Концентрация озона (O3)', 
               line=dict(color='rebeccapurple'), 
               marker=dict(size=8))],
           layout=go.Layout(
               title=dict(
                   text='Концентрация озона (O3)', 
                   x=0.5,
                   font=dict(size=17)
                   ),
                   xaxis_title='Время', 
                   yaxis_title='(O3), мг/м³', 
                   plot_bgcolor='rgba(0, 255, 255, 0.13)',
                   paper_bgcolor='rgba(0, 0, 0, 0)',
                   margin=dict(l=40, r=40, t=60, b=40)))

        so2_fig = go.Figure(
           data=[
               go.Scatter(
               x=data['hours'], 
               y=data['so2'], 
               mode='lines+markers', 
               name='Концентрация углекислого газа (CO₂)', 
               line=dict(color='rebeccapurple'), 
               marker=dict(size=8))],
           layout=go.Layout(
               title=dict(
                   text='Концентрация углекислого газа (CO₂)', 
                   x=0.5,
                   font=dict(size=17)
                   ),
                   xaxis_title='Время', 
                   yaxis_title='(CO₂), ppm', 
                   plot_bgcolor='rgba(0, 255, 255, 0.1)',
                   paper_bgcolor='rgba(0, 0, 0, 0)',
                   margin=dict(l=40, r=40, t=60, b=40)))

        pm2_5_fig = go.Figure(
           data=[
               go.Scatter(
               x=data['hours'], 
               y=data['pm2_5'], 
               mode='lines+markers', 
               name='Концентрация микроскопических частиц', 
               line=dict(color='rebeccapurple'), 
               marker=dict(size=8))],
           layout=go.Layout(
               title=dict(
                   text='Концентрация микроскопических частиц', 
                   x=0.5,
                   font=dict(size=17)
                   ),
                   xaxis_title='Время', 
                   yaxis_title='мкг/м³', 
                   plot_bgcolor='rgba(0, 255, 255, 0.13)',
                   paper_bgcolor='rgba(0, 0, 0, 0)',
                   margin=dict(l=40, r=40, t=60, b=40)))
        
        pm10_fig = go.Figure(
           data=[
               go.Scatter(
               x=data['hours'],
               y=data['pm10'],
               mode='lines+markers',
               name='Концентрация крупной пыли',
               line=dict(color='rebeccapurple'),  
               marker=dict(size=8)
           )
       ],
           layout=go.Layout(
               title=dict(
                   text='Концентрация крупной пыли',
                   x=0.5, 
                   font=dict(size=17)
               ),
               xaxis_title='Время',
               yaxis_title='мкг/м³',
               plot_bgcolor='rgba(0, 255, 255, 0.13)', 
               paper_bgcolor='rgba(0, 0, 0, 0)',
               margin=dict(l=40, r=40, t=60, b=40) 
       )
           )


        return air_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig
    
