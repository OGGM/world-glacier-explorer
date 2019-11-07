from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the glaciers.ipynb directory with bokeh server"""
    Popen(["panel", "serve", "app.ipynb", "--allow-websocket-origin=*"])

