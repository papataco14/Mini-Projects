import cv2, time, pandas, os
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

first_frame = None

status_list = [None, None]  # to allow comparison in first iteration in line 41
times = []
df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # specify video soure
# triggers video capture object, arguments: 0,1,2 (indicates camera) or filepath. one webcam only = 0

while True:
    check, frame = video.read()
    status = 0
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(
        gray, (21, 21), 0
    )  # blur the image to increase accuracy later

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)

    # threshold method returns a tuple with 2 values. for thresh_binary we only need to access the frame, the 2nd item.
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    # to smoothen threshold frame
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=10)

    # to find all the contours of distinct objects in an image
    (cnts, _) = cv2.findContours(
        thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in cnts:  # to filter the contours
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(status)

    # the time an object enters and exits the frame is represented by a status change.
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Gray Frame", gray)  # 1st frame of video
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        if status == 1:
            times.append(
                datetime.now()
            )  # to capture exit time when closing with object in frame
        break

    print(status)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True)

os.makedirs(
    "vid", exist_ok=True
)  # doctest: +SKIP
df.to_csv("Times.csv")

# create plot
# ensure series is in datetime format
df["Start"] = pandas.to_datetime(df["Start"])
df["End"] = pandas.to_datetime(df["End"])

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)

# creating figure object
p = figure(
    x_axis_type="datetime",
    height=100,
    width=500,
    sizing_mode="scale_width",
    title="Motion Graph",
)
p.yaxis.minor_tick_line_color = None
p.yaxis[0].ticker.desired_num_ticks = 1

# create hover object (unable to read datetimes)
hover = HoverTool(tooltips=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

# plot glyph inside figure
q = p.quad(left="Start", right="End", bottom=0, top=1, color="red", source=cds)

# create output file
os.makedirs(
    "vid", exist_ok=True
)  # doctest: +SKIP
output_file("Graph.html")

show(p)

video.release()
cv2.destroyAllWindows()
