'''
referred from: https://www.kaggle.com/gzuidhof/full-preprocessing-tutorial
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.ndimage
import dicom
import cv2
import os

from skimage import measure, morphology
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

INPUT_FOLDER = 'G:/DL/Lung-Cancer_Detection/sample_images/'
dimension = 224

patients = os.listdir(INPUT_FOLDER)
labels = pd.read_csv('G:/DL/Lung-Cancer_Detection/stage1_labels.csv/stage1_labels.csv')
print(labels.head())
patients.sort()	# sorting by names will always give same order of files
print(patients)

for patient in patients[:1]:
    # label = labels.get_value(patient, 'cancer')

    path = INPUT_FOLDER + patient
    slices = [dicom.read_file(path + '/' + s) for s in os.listdir(path)]
    slices.sort(key=lambda x: float(x.ImagePositionPatient[2]))

    '''
    slices contain n number of slices, where n can be around 200.
        Each slice in slices contain a number of non-homogenous attributes
            one of the attribute is pixel_array
            pixel_array is a numpy array with shape (512, 512), and it contains the actual data (the image)
    '''

    print(len(slices))
    print(slices[0].pixel_array.shape)

    new_slices = []
    for slice in slices:
        new_slices.append(cv2.resize(np.array(slice.pixel_array), (dimension, dimension)))
    new_slices = np.array(new_slices)

    print(new_slices.shape)
    slices = new_slices