import pandas as pd
import preprocess
import plotly.express as px
import datetime as dt
import numpy as np

# Get the data (temporary solution until data are processed)
with open('./OLTCresults.csv', encoding='utf-8') as data_file:
    oltc_data = pd.read_csv(data_file)
   
oltc_data = preprocess.drop_irrelevant_time(oltc_data)


                           

# Chnage the Time format
oltc_data['Time']= oltc_data['Time'].apply(lambda x:dt.datetime.strptime(x, "%I:%M:%S %p").hour)

Time_sorted_data = oltc_data.sort_values('Time')
h = Time_sorted_data['Time']

####### in the next step, we design the radio button for this part #######
#tap = 'tapAfter'
tap = 'tapBefore'
################################################

### Select the suitable data and create new dataframe ####
output_tap = []
ind0 = 0
for i in range(24):
    for j in range(np.min(Time_sorted_data[tap]),np.max(Time_sorted_data[tap]+1)):
        ind = np.where(h==i)[0][-1]
        ind1 = np.where(Time_sorted_data[tap][ind0:ind]==j)
        output_tap.append([i,j,np.max(Time_sorted_data['TrafoLoadCurr'][ind1[0]]),
                             np.max(Time_sorted_data['tapPowerLossAmp'][ind1[0]]),
                             np.max(Time_sorted_data['tapEnergyLoss'][ind1[0]]),
                             np.max(Time_sorted_data['tapCircCurrAmp'][ind1[0]])])
    ind0 = ind

y = np.array(output_tap)

if tap == 'tapAfter':
    data = {'Time_in_Hours': y[:,0],
            'Tap_After' : y[:,1],
            'Max_loadCurr': y[:,2],
            'Max_PowerLoss': y[:,3],
            'Max_EnergyLoss': y[:,3],
            'Max_CircCurr': y[:,3]}
    tap1 = 'Tap_After'
else:
    data = {'Time_in_Hours': y[:,0],
            'Tap_Before' : y[:,1],
            'Max_loadCurr': y[:,2],
            'Max_PowerLoss': y[:,3],
            'Max_EnergyLoss': y[:,3],
            'Max_CircCurr': y[:,3]}
    tap1 = 'Tap_Before'
    
df1 = pd.DataFrame(data)

### Create the exact time #########
lst = list(np.int32(df1['Time_in_Hours']))
df1['Time_in_Hours'] = [dt.time(hour=x).strftime("%H:%M") for x in lst]

#######################
def bar_plot_Max_CircCurr(tap):
    fig = px.bar(df1, x="Time_in_Hours", y="Max_CircCurr", color=tap)
    return fig

def bar_plot_Max_EnergyLoss(tap):
    fig = px.bar(df1, x="Time_in_Hours", y="Max_EnergyLoss", color=tap)
    return fig

def bar_plot_Max_PowerLoss(tap):
    fig = px.bar(df1, x="Time_in_Hours", y="Max_PowerLoss", color=tap)
    return fig

def bar_plot_Max_loadCurr(tap):
    fig = px.bar(df1, x="Time_in_Hours", y="Max_loadCurr", color=tap)
    return fig

def bar_plot_animation_Max_CircCurr(tap):
    fig = px.bar(df1, x="Time_in_Hours", y="Max_CircCurr", animation_frame=tap)
    return fig

def bar_plot_animation_Max_EnergyLoss(tap):
    fig = px.bar(df1, x="Time_in_Hours", y="Max_EnergyLoss", animation_frame=tap)
    return fig

def bar_plot_animation_Max_PowerLoss(tap):
    fig = px.bar(df1, x="Time_in_Hours", y="Max_PowerLoss", animation_frame=tap)
    return fig

def bar_plot_animation_Max_loadCurr(tap):
    fig = px.bar(df1, x="Time_in_Hours", y="Max_loadCurr", animation_frame=tap)
    return fig

def fig_update(fig):
        fig.update_layout(
            xaxis = dict(
            tickmode = 'linear',
            tick0 = 0,
            dtick = 1
                )
            )
        return fig
   
fig = bar_plot_animation_Max_loadCurr(tap1)
#fig = bar_plot_Max_loadCurr(tap1)
fig_update(fig)
