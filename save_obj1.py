import os.path
import pickle

weekdays = ["月", "火", "水", "木", "金", "土", "日"]
filename = "days.pickle"
file_path = os.path.join(os.path.dirname(__file__), filename)
out_file = open(file_path, "wb")
pickle.dump(weekdays, out_file)