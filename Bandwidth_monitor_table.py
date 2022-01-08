# NetworkBandwidthMonitor.py
# Written by: https://github.com/waterrmalann
# Written on: 15th May, 2020
# Written in: Python 3.7 w/ Tkinter

import tkinter as tk
from psutil import net_io_counters
from Tracker import Tracker

# Variables for use in the size() function.
KB = float(1024)
MB = float(KB ** 2) # 1,048,576
GB = float(KB ** 3) # 1,073,741,824
TB = float(KB ** 4) # 1,099,511,627,776

def size(B):
	B = float(B)
	if B < KB: return f"{B:.2f} Bytes"
	elif KB <= B < MB: return f"{B/KB:.2f} KB"
	elif MB <= B < GB: return f"{B/MB:.2f} MB"
	elif GB <= B < TB: return f"{B/GB:.2f} GB"
	elif TB <= B: return f"{B/TB:.2f} TB"

## Constants
WINDOW_SIZE = (400, 400)  # Width x Height
WINDOW_RESIZEABLE = False  # If the window is resizeable or not.
REFRESH_DELAY = 1000 # Window update delay in ms.

## Initializing
window = tk.Tk()

window.title("Network Bandwidth Monitor")  # Setting the window title.
window.geometry(f"{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}")  # Setting the window size.
window.resizable(width = WINDOW_RESIZEABLE, height = WINDOW_RESIZEABLE)  # We now lock the window.

label_total_upload_header = tk.Label(text = "Total Upload:", font = "Quicksand 12 bold")
label_total_upload_header.pack()
label_total_upload = tk.Label(text = "Calculating...", font = "Quicksand 12")
label_total_upload.pack()

label_total_download_header = tk.Label(text = "Total Download:", font = "Quicksand 12 bold")
label_total_download_header.pack()
label_total_download = tk.Label(text = "Calculating...", font = "Quicksand 12")
label_total_download.pack()
