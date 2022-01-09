

label_total_usage_header = tk.Label(text = "Total Usage:", font = "Quicksand 12 bold")
label_total_usage_header.pack()
label_total_usage = tk.Label(text = "Calculating...\n", font = "Quicksand 12")
label_total_usage.pack()

label_upload_header = tk.Label(text = "Upload speed:", font = "Quicksand 12 bold")
label_upload_header.pack()
label_upload = tk.Label(text = "Calculating...", font = "Quicksand 12")
label_upload.pack()

label_download_header = tk.Label(text = "Download speed:", font = "Quicksand 12 bold")
label_download_header.pack()
label_download = tk.Label(text = "Calculating...", font = "Quicksand 12")
label_download.pack()

tracker = Tracker()

# Updating Labels
def update():

	upload = tracker.__get_bytes_sent_total__() - tracker.init_total_sent
	download = tracker.__get_bytes_recv_total__() - tracker.init_total_recv
	total = upload + download

	down_speed = tracker.get_current_download_speed()
	up_speed = tracker.get_current_upload_speed()
	
	label_total_upload["text"] = f"{size(upload)} ({upload} Bytes)"
	label_total_download["text"] = f"{size(download)} ({download} Bytes)"
	label_total_usage["text"] = f"{size(total)}\n"
	
	label_upload["text"] = size(up_speed) + "/s"
	label_download["text"] = size(down_speed) + "/s"
	
	label_total_upload.pack()
	label_total_download.pack()
	label_total_usage.pack()
	label_upload.pack()
	label_download.pack()
	
	window.after(REFRESH_DELAY, update)  # reschedule event in refresh delay.

window.after(REFRESH_DELAY, update)
window.mainloop()
