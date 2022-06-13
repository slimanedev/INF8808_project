'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html

def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    if style['visibility']=='hidden':
        return None, None, None, style


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    if style['visibility']=='hidden':
        return None, None, None, style

    return title, mode, theme,style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): 
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers   
    
    #find the tilte and the color
    title_txt=figure['data'][curve]['customdata'][point][1]
    color_title=figure['data'][curve]['marker']['color']
    title = [html.Span(title_txt , style={'color': color_title,'fontWeight':'bold'})]

    #find the mode
    mode_txt=figure['data'][curve]['customdata'][point][2]
    mode = [html.Span(mode_txt , style={'fontWeight':'bold'})]

    #find the theme
    theme_txt=figure['data'][curve]['customdata'][point][0]
    if theme_txt :
        theme_list=list(theme_txt.split('\n'))
        theme=[html.Span("Thématique :"),html.Ul(children=[html.Li(l) for l in theme_list])]
    else : theme=None
    
    #Update the style
    style['visibility']= 'visible'
    style['marginTop']= 25
  
    return title, mode,theme,style

    