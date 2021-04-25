from motiondetection import df #from "filename" of your motion detection program should be given and df is the data frame in that program
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"]=df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"]=df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")


cds=ColumnDataSource(df)

p=figure(x_axis_type='datetime',height=100, width=500, sizing_mode = "scale_width", title="Motion Graph")
p.yaxis.minor_tick_line_color=None
#p.ygrid[0].ticker.desired_num_ticks=1 https://stackoverflow.com/questions/62369221/unable-to-use-bokeh-plots-desired-num-ticks-error-thrown-is-nonetype-obj

hover=HoverTool(tooltips=[("Start","@Start_string"),("End","@End_string")])
p.add_tools(hover)

q=p.quad(left="Start",right="End",bottom=0,top=1,color="green",source=cds)

output_file("Graph1.html")
show(p)