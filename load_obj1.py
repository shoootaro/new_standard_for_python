import os.path
import pickle

weekdays = []
filename = "days.pickle"
file_path = os.path.join(os.path.dirname(__file__), filename)
in_file = open(file_path, "rb")

days = pickle.load(in_file)
print(days)