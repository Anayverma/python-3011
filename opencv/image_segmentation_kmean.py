import numpy as np
import cv2
from sklearn.cluster import KMeans

# Load the image
image = cv2.imread('image.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB

# Flatten the image
pixels = image.reshape((-1, 3))

# Choose the number of clusters (K)
k = 3

# Apply K-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(pixels)

# Get the labels and clustered pixel values
labels = kmeans.labels_
clustered_pixels = kmeans.cluster_centers_.astype(int)

# Assign each pixel in the image to its corresponding cluster center
segmented_image = clustered_pixels[labels].reshape(image.shape)

# Display the original and segmented images
import matplotlib.pyplot as plt

plt.subplot(121), plt.imshow(image), plt.title('Original Image')
plt.subplot(122), plt.imshow(segmented_image), plt.title('Segmented Image')
plt.show()
