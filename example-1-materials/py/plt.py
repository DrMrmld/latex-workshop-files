import plotly.graph_objects as go
import numpy as np

arr1 = np.random.normal(loc = 50, scale = 8, size = 50)
arr2 = np.random.normal(loc = 60, scale = 11, size = 50)

fig = go.Figure()
fig.add_traces([
    go.Box(
        name = "Category 1",
        y = arr1,
        boxpoints = "all"
    ),
    go.Box(
        name = "Category 2",
        y = arr2,
        boxpoints = "all"
    )
])
fig.update_layout(
    template = "simple_white",
    margin = dict(
        r = 15
    ),
    width = 800,
    title = "A plot of two random samples",
    yaxis_title = "Some metric, unit",
    font = dict(
        family = "TeXGyreSchola",
        size = 14
    ),
    showlegend = False
)
fig.write_image("plt.svg")
