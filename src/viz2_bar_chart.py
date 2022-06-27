import plotly.express as px
import pandas as pd
import collections
import template


def BarChart(data):
        tapAfter = data['tapAfter'].tolist()
        counter = collections.Counter(tapAfter)
        Number = counter.values()
        df = pd.DataFrame(counter.items(),
                columns=['Tap position', 'Number of Change'],
        )

        # Plot bar chart for viz 2
        fig = px.bar(df,
                x='Number of Change',
                y='Tap position',
                orientation='h',
        )

        # Add hover_template 
        fig.update_traces(hovertemplate =template.get_hover_template_viz2())
        # Update layout
        fig.update_layout(title="The number of tap changes of each tap position")

        return fig



