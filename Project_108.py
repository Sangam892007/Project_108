import pandas as pd
import plotly.figure_factory as pff

data = pd.read_csv("data2.csv")
AvgRating = data["Avg Rating"]

RatingBellCurve = pff.create_distplot([AvgRating], ["Average Rating of different mobile brands"], show_hist = False)
RatingBellCurve.show()