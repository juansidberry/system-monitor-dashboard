import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import psutil
import logging
from collections import deque
from datetime import datetime
import sys

# Set up basic logging to debug
logging.basicConfig(level=logging.INFO)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define fixed-size lists (deque) to store the last 20 data points for RAM, CPU, Disk usage, and time
history = {
    'ram': deque(maxlen=20),
    'cpu': deque(maxlen=20),
    'disk': deque(maxlen=20),
    'time': deque(maxlen=20)  # Store timestamps for x-axis
}

