'''
    Contains the template to use in the data visualization.
'''
import plotly.graph_objects as go
import plotly.io as pio


THEME = {
    'plot_background_color': 'beige',
    'font_family': 'Roboto',
    'accent_font_family': 'Roboto Slab',
    'dark_color': '#2A2B2E',
    'pale_color': '#DFD9E2',
    'label_font_size': 14,
    'label_background_color': '#ffffff',
}


def create_custom_theme():
    '''
        Adds a new layout template to pio's templates.

        The template sets the font color and
        font to the values defined above in
        the THEME dictionary, using the dark
        color.

        The plot background and paper background
        are the background color defined
        above in the THEME dictionary.

        Also, sets the hover label to have a
        background color and font size
        as defined for the label in the THEME dictionary.
        The hover label's font color is the same
        as the theme's overall font color. The hover mode
        is set to 'closest'.

        Sets the line chart's line color to the one
        designated in the THEME dictionary. Also sets
        the color scale to be used by the heatmap
        to the one in the THEME dictionary.

        Specifies the x-axis ticks are tilted 45
        degrees to the right.
    '''
    # TODO : Generate template described above
    pio.templates['custom'] = dict(
        layout=go.Layout(
        title_font=dict(family = THEME['font_family'], color= THEME['dark_color']),
        font=dict(family = THEME['font_family'], color= THEME['dark_color']),
        plot_bgcolor = THEME['plot_background_color'], 
        hoverlabel=dict(font=
                        dict(family=THEME['font_family'],
                             size=THEME['label_font_size'],
                             color=THEME['dark_color']),
                             bgcolor = THEME['label_background_color'])))

def set_default_theme():
    '''
        Sets the default theme to be a combination of the
        'plotly_white' theme and our custom theme.
    '''
    # TODO : Set default theme
    fig = go.Figure()

    fig.update_layout(
        template = pio.templates['plotly_white'],
        dragmode = False,
        barmode = 'relative'
    )
    
    #setting the tempalte
    pio.templates.default = 'plotly_white+custom'
    fig.update_layout(template = pio.templates.default)

# Define chart templates when needed

def get_hover_template_viz1():
    hovertemplate= '<b>Day: %{x}<br><b>New Tap Number: %{y} <extra></extra>'
    return hovertemplate

def get_hover_template_viz2():
    hovertemplate= '<b>%{y}</b><br><br><b>Number of Change: %{x} <br><b>Tap position: %{y}<extra></extra>'
    return hovertemplate

def get_hover_template_viz8():
  hovertemplate= '<b> Year: %{text}<br><b>Month: %{x} <br><b>Circulatiing current: %{y}(kA) <extra></extra>'
  return hovertemplate

def get_hover_template_viz9_barchart():
    hovertemplate= '<b>Time (hour): %{x}<br><b>Maximum load current: %{y} (KA) <extra></extra>'
    return hovertemplate

def get_hover_template_viz9_linechart():
    hovertemplate= '<b>Time (hour): %{x}<br><b>Average load current: %{y} (KA) <extra></extra>'
    return hovertemplate




