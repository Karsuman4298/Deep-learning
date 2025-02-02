
import plotly.graph_objects as go
import numpy as np

x=np.linspace(-1,1,100)    // x-axis range [-1 , 1 ] &&  100 subpoints
y=np.linspace(-1,1,100)   //  y-axis range [-1 , 1 ] &&  100 subpoints
X,Y=np.meshgrid(x,y)
Z=np.sin(2*X**2+3*Y**3)   // eqation 
fig=go.Figure(go.Surface(z=Z,x=X,y=Y))  // defining axis 
fig.update_layout(title="Surface Plot")  // giving title name 
fig.show() // for showing the output 


//OUPUT : newplot.png
