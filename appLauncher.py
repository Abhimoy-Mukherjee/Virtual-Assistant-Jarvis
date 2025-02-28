import subprocess

def open_app(app_name):
    """Opens a macOS application using the open command."""
    try:
        subprocess.run(["open", "-a", app_name])
        print(f"Opening {app_name}...")
    except Exception as e:
        print(f"Error opening {app_name}: {e}")
