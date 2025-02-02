//  Creates 50 random points on both X-Axis and Y-Axis.

import pandas as pd
import numpy as np
import plotly.express as px
x_data=np.random.random(50)
y_data=np.random.random(50)
fig=px.scatter(x=x_data,y=y_data)
fig.show()


// OUTPUT : Discrete_points_plotly.png
