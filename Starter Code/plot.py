import matplotlib.pyplot as plt
import pickle
import numpy as np

losses = pickle.load(open("losses",'rb'))
loss_xy = list(zip(*losses))
xpoint_raw = loss_xy[0]
ypoint_raw = loss_xy[1]
sum_x = 0
sum_y = 0

xpoints = []
ypoints = []
for i in range(0, len(xpoint_raw)):
    sum_x += xpoint_raw[i]
    sum_y += ypoint_raw[i]
    if i % 50000 == 0 and i != 0:
        xpoints.append(float(sum_x/50000))
        ypoints.append(float(sum_y/50000))
        sum_x = 0
        sum_y = 0

plt.title('Loss Graph')
plt.xlabel('num_frames')
plt.ylabel('average loss per 50000 frames')
plt.plot(xpoints, ypoints)
plt.show()
