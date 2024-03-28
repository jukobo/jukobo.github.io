import pandas as pd
from bokeh.models import ColumnDataSource, Legend
from bokeh.plotting import figure, show
from bokeh.transform import jitter
from bokeh.palettes import Category20b
from bokeh.models import DatetimeTickFormatter


## Load files
file = "Data/Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240130.csv"
# file = "..\..\Data\Police_Department_Incident_Reports__Historical_2003_to_May_2018_20240206.csv"
crime = 'PROSTITUTION'

df = pd.read_csv(file)
df = df[df['Date'].str.contains('2018') == False]

focusdf = df[df['Category']== crime]


pd_districts = focusdf['PdDistrict'].dropna().astype(str).unique()


# Convert 'time' column to datetime
focusdf['time'] = pd.to_datetime(focusdf['Time'])

# Set 'datetime' column as index
focusdf['datetime'] = pd.to_datetime(focusdf['Date'])
focusdf.set_index('datetime', inplace=True)

# Make sure 'DayOfWeek' column is categorical
focusdf['DayOfWeek'] = pd.Categorical(focusdf['DayOfWeek'], categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], ordered=True)

p = figure(width=800, height=300, y_range=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], x_axis_type='datetime',
           title="Prostitution")

# Add axis titles
p.xaxis.axis_label = "Time"
p.yaxis.axis_label = "Day of Week"

items = []
b = {}
for d in range(len(pd_districts)):
    df_temp = focusdf[focusdf['PdDistrict'] == pd_districts[d]]
    
    # Create a new DataFrame with columns for 'day' and 'time'
    Data = df_temp[['DayOfWeek', 'time']]

    source = ColumnDataSource(Data)

    b[d] = p.scatter(x='time', y=jitter('DayOfWeek', width=0.6, range=p.y_range),  source=source, muted_alpha=0.005, color=Category20b[14][d], muted=True)
    # Create legend items
    items.append((pd_districts[d], [b[d]]))

# Create legend
legend = Legend(items=items, location='center_right')
p.add_layout(legend, 'right')


p.xaxis.formatter = DatetimeTickFormatter(hours=["%H:%M"])
p.x_range.range_padding = 0
p.ygrid.grid_line_color = None
p.legend.click_policy = "mute"


show(p)
