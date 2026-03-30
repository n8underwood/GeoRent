from dash import Dash, dcc, html
import json
import plotly.express as px
from src.functions import import_data
from urllib.request import urlopen

app = Dash(__name__)

# Import data
with urlopen("http://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json") as response: 
        counties = json.load(response)
df = import_data("data/us_metrics.csv")

# Correct an error that reappears on importing (see data.ipynb for description)
df["fips_code"] = df["fips_code"].astype(str)
df['fips_code'] = df['fips_code'].str.zfill(5)

fig = px.choropleth(df, geojson=counties, color="median_household_income",
                        locations="fips_code", 
                        hover_name="area_name",
                        color_continuous_scale="Viridis",
                        range_color=(40000, 100000),
                        scope="usa",
                        labels={"median_household_income": "Median Household Income"}
                        )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Create a layout for the app
app.layout = html.Div([
    html.H4("Median Household Income in 2022"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)