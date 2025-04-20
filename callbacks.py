from dash import Input, Output, html
from utils.data_loader import load_data
import plotly.graph_objects as go

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
            html.H4(f"Состояние воздуха в городе {data['city_name']} сейчас:", className="card-title"),
            html.H5(f"🏭 Концентрация оксида углерода (CO) в воздухе: {data['co_curr']} мг/м³", className="card-subtitle md-4 text-muted"),
            html.H5(f"☁︎  Концентрация диоксида азота (NO2) в воздухе: {data['no2_curr']} мг/м³", className="card-subtitle md-4 text-muted"),
            html.H5(f"⚡ Концентрация озона (O3) в воздухе: {data['o3_curr']} мг/м³", className="card-subtitle md-4 text-muted"),
            html.H5(f"😶‍🌫 Концентрация углекислого газа (CO₂) в воздухе: {data['so2_curr']} ppm", className="card-subtitle md-4 text-muted"),
            html.H5(f"🌪️ Концентрация микроскопических частиц в воздухе: {data['pm2_5_curr']} мкг/м³", className="card-subtitle md-4 text-muted"),
            html.H5(f"🪨 Концентрация крупной пыли в воздухе: {data['pm10_curr']} мкг/м³", className="card-subtitle md-4 text-muted")
        ])

        co_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['co'], mode='lines+markers', name='Концентрация оксида углерода (CO)')],
           layout=go.Layout(title='Концентрация оксида углерода (CO) в воздухе по часам', xaxis_title='Время', yaxis_title='(CO), мг/м³', template='plotly_dark')
        )

        no2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['no2'], mode='lines+markers', name='Концентрация диоксида азота (NO2)')], 
           layout=go.Layout(title='Концентрация диоксида азота (NO2) в воздухе по часам', xaxis_title='Время', yaxis_title='(NO2), мг/м³', template='plotly_dark')
        )

        o3_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['o3'], mode='lines+markers', name='Концентрация озона (O3)')],    
           layout=go.Layout(title='Концентрация озона (O3) в воздухе по часам', xaxis_title='Время', yaxis_title='(O3), мг/м³', template='plotly_dark')
        )

        so2_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['so2'], mode='lines+markers', name='Концентрация углекислого газа (CO₂)')],
           layout=go.Layout(title='Концентрация углекислого газа (CO₂) в воздухе по часам', xaxis_title='Время', yaxis_title='(CO₂), ppm', template='plotly_dark')
        )

        pm2_5_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm2_5'], mode='lines+markers', name='Концентрация микроскопических частиц')],
           layout=go.Layout(title='Концентрация микроскопических частиц в воздухе', xaxis_title='Время', yaxis_title='мкг/м³', template='plotly_dark') 
        )

        pm10_fig = go.Figure(
           data=[go.Scatter(x=data['hours'], y=data['pm10'], mode='lines+markers', name='Концентрация крупной пыли')],
           layout=go.Layout(title='Концентрация крупной пыли в воздухе', xaxis_title='Время', yaxis_title='мкг/м³', template='plotly_dark') 
        )


        return air_info, co_fig, no2_fig, o3_fig, so2_fig, pm2_5_fig, pm10_fig
    
