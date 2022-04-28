# https://scikit-image.org/docs/stable/auto_examples/features_detection/plot_template.html
# https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Rectangle.html

from skimage import io, data, color
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import match_template

woman = io.imread('Woman.png', as_gray=True)
woman_eye_template = io.imread('Woman_eye.png', as_gray=True)

result = match_template(woman, woman_eye_template)
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]
print(x, y)

# fig = plt.figure(figsize=(8, 5))
ax1 = plt.subplot(1, 4, 1)
ax2 = plt.subplot(1, 4, 2)
ax3 = plt.subplot(1, 4, 3, sharex=ax2, sharey=ax2)
ax4 = plt.subplot(1, 4, 4, sharex=ax2, sharey=ax2)

ax1.imshow(woman_eye_template, cmap=plt.cm.gray)
ax1.set_axis_off()
ax1.set_title('template')

ax2.imshow(woman, cmap=plt.cm.gray)
ax2.set_axis_off()
ax2.set_title('image')

# highlight matched region
h_template, w_template = woman_eye_template.shape
rect = plt.Rectangle((x, y), w_template, h_template,
                     edgecolor='r', facecolor='none')
ax2.add_patch(rect)

print(w_template, h_template)

# i,y - linha - inicio altura
# j, x - coluna - inicio largura
for i in range(y-1, y+h_template+1):
    for j in range(x-1, x+w_template+1):
        woman[i][j] = 1

ax3.imshow(woman, cmap=plt.cm.gray)
ax3.set_axis_off()
ax3.set_title('Removendo Olho')

result = match_template(woman, woman_eye_template)
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]
print(x, y)

ax4.imshow(woman, cmap=plt.cm.gray)
ax4.set_axis_off()
ax4.set_title('image')

# highlight matched region
h_template, w_template = woman_eye_template.shape
rect = plt.Rectangle((x, y), w_template, h_template,
                     edgecolor='r', facecolor='none')
ax4.add_patch(rect)

print(w_template, h_template)

plt.show()
