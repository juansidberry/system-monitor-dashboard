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


# Function to get system statistics (RAM, CPU, and Disk)
def get_system_stats():
    try:
        # Get memory stats
        memory = psutil.virtual_memory()
        ram = memory.percent

        # Get CPU usage
        cpu = psutil.cpu_percent(interval=1)

        # Get Disk usage
        disk = psutil.disk_usage('/').percent

        # Return RAM, CPU, and Disk data
        return {
            'RAM Usage (%)': ram,
            'CPU Usage (%)': cpu,
            'Disk Usage (%)': disk
        }
    except Exception as e:
        logging.error(f"Error fetching system stats: {e}")
        return {}
    

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)