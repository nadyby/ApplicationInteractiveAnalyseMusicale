import os

interface_path = os.path.join("src", "music_analysis_app", "main.py")
os.system(f"streamlit run {interface_path}")
