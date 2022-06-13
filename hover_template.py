'''
    Provides the templates for the tooltips.
'''


def map_base_hover_template():
    '''
        Sets the template for the hover tooltips on the neighborhoods.

        The label is simply the name of the neighborhood in font 'Oswald'.

        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template

    hover_map = '<span style="font-family:Oswald"></span>%{customdata}<br><extra></extra>'

    return hover_map


def map_marker_hover_template():
    '''
        Sets the template for the hover tooltips on the markers.

        The label is simply the name of the walking path in font 'Oswald'.

        Args:
            name: The name to display
        Returns:
            The hover template.
    '''
    # TODO : Generate the hover template

    hover_scatter = '<span style="font-family:Oswald"></span>%{hover_name}<br><extra></extra>'
    return hover_scatter