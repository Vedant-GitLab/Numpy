#stacking means jodna. do tarah ke hote hai horizontal and vertical
import numpy as np
a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

#HORIZONTAL STACKING : [2x2][2x2]=[2x4]
print(np.hstack((a1,a2))) #a1 aur a2 dono apas me jud jayengi
print(np.hstack((a1,a2,a1,a2))) #aise hum jitni chahe utne arrays ko jod skte hai

#VERTICAL STACKING : [2x2][2x2]=[4x2]
c = np.vstack((a1,a2))
print(c)
print(np.vstack((a1,a2,a1,a2)))