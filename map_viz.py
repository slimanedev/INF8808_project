'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover
import numpy

def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure 000every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    fig=go.Figure(go.Choroplethmapbox(
            name=montreal_data['name'],
            geojson=montreal_data,
            locations=locations,
            z=z_vals,
            customdata= locations,
            featureidkey="properties.NOM",
            below="",
            showscale=False,
            hovertemplate= hover.map_base_hover_template(),
            marker = dict(line=dict(color='white')),
            colorscale=colorscale))
    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base
    fig_temp=px.scatter_mapbox(street_df,
                          lat= "properties.LATITUDE", 
                          lon="properties.LONGITUDE", 
                          color="properties.TYPE_SITE_INTERVENTION",
                          color_continuous_scale=px.colors.cyclical.IceFire,
                          opacity=0.6,
                          zoom = 12,
                          custom_data=numpy.stack(["properties.OBJECTIF_THEMATIQUE", "properties.NOM_PROJET",'properties.MODE_IMPLANTATION'], axis=-1),
                          mapbox_style="carto-positron",
                          hover_data={"properties.LATITUDE":False,"properties.LONGITUDE":False, "properties.TYPE_SITE_INTERVENTION":False},
                          hover_name="properties.TYPE_SITE_INTERVENTION",
                         )

    fig_temp.update_traces(marker={'size': 10}) # adapt marker size
    
    for i in range(len(fig_temp.data)):
        fig.add_trace(fig_temp.data[i]) # add each scatter over the map

    fig_temp.update_traces(hovertemplate=hover.map_marker_hover_template()) # call the hover template

    return fig
