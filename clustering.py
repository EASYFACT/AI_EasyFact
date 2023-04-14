import os
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
#from tensorflow.keras.applications.resnet50 import preprocess_input

import shutil

# Load the pre-trained VGG16 model
base_model = VGG16(weights='imagenet', include_top=False)

# Remove the classifier layers
model = Model(inputs=base_model.input, outputs=base_model.get_layer('block5_conv2').output)

# Define the path to the directory containing the unlabeled images
path = r'C:\Users\Rihab\Desktop\dataSetFactures\convertedPrivateDS'
# Define the output directory
output_path = r'C:\Users\Rihab\Desktop\dataSetFactures\testCodes\clusters'

# Define the target image size for resizing
target_size = (224, 224)

# Define the number of clusters
n_clusters = 2

# Load the images and extract features
X = []
image_paths = []
original_sizes = []
for filename in os.listdir(path):
    img_path = os.path.join(path, filename)
    img = Image.open(img_path)
    original_size = img.size
    img = img.resize(target_size)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    features = np.append(features.flatten(), original_size)
    X.append(features)
    image_paths.append(img_path)
    original_sizes.append(original_size)


# Cluster the feature vectors
kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(X)

# Create directories for each cluster label and save images
for i in range(n_clusters):
    os.makedirs(os.path.join(output_path, f'cluster_{i}'), exist_ok=True)

for filename, label, original_size in zip(os.listdir(path), kmeans.labels_, original_sizes):
    src_path = os.path.join(path, filename)
    dst_path = os.path.join(output_path, f'cluster_{label}', filename)
    img = Image.open(src_path)
    img_resized = img.resize(original_size)
    img_resized.save(dst_path)

# Print a message indicating that the clustering is done
print('Clustering is done!')
