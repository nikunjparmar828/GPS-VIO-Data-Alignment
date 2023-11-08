import numpy as np
from matplotlib import pyplot as plt
import math
from scipy.linalg import orthogonal_procrustes
from utils import latlon2xyz
import os

def manage_data(file_name):
  """
  Process gps and odom data and store them in lists
  """
  initial_lat_long = []
  gps_xy = []
  odom_xy = []
  i=0

  # read the csv data from the file
  with open(file_name, "r") as filestream:
    for line in filestream:
      currentline = line.split(",")
      
      # intial value of gps capture for latlon2xyz's 3rd and 4th arguments 
      if i==0:
        initial_lat_long.append([float(currentline[0]), float(currentline[1])])

      # converts lat, long to x, y coordinates
      x, y = latlon2xyz(float(currentline[0]), float(currentline[1]), initial_lat_long[0][0], initial_lat_long[0][1])
      
      gps_xy.append([x, y])
      odom_xy.append([float(currentline[8]), float(currentline[10])])

      i+=1

  return gps_xy, odom_xy


def find_rotation_translation(frame1_points, frame2_points):
    # Calculate the centroids of the points
    centroid1 = np.mean(frame1_points, axis=0)
    centroid2 = np.mean(frame2_points, axis=0)

    # Center the points by subtracting the centroids
    centered_frame1_points = frame1_points - centroid1
    centered_frame2_points = frame2_points - centroid2

    # Calculate the scaling factor
    scale_factor = np.sum(np.linalg.norm(centered_frame1_points, axis=1)**2) / np.sum(np.linalg.norm(centered_frame2_points, axis=1)**2)

    # Scale the centered points of the second frame
    scaled_frame2_points = centered_frame2_points * np.sqrt(scale_factor)

    # Apply orthogonal Procrustes analysis to find rotation matrix
    rotation_matrix, _ = orthogonal_procrustes(scaled_frame2_points, centered_frame1_points)

    # Calculate translation vector
    translation_vector = centroid1 - np.dot(centroid2, rotation_matrix)

    return rotation_matrix, translation_vector

if __name__ == '__main__':
  # Get the current path
  cwd = os.getcwd()  

  # Change the file name as per need
  file_name_txt = "gps_odom_data.txt"
  file_name = cwd + "/data/" + file_name_txt
  
  gps_xy, odom_xy = manage_data(file_name)

  gps_xy = np.array(gps_xy)
  odom_xy = np.array(odom_xy)

  #r, t = find_rotation_translation(gps_xy, odom_xy)

  # apply rotation to each data point
  #for i in range(odom_xy.shape[0]):
   # odom_xy[i] = (r@(odom_xy[i].T)).T

  # translation
  #odom_xy = odom_xy + t
  
  # plotting
  x1, y1 = gps_xy.T
  x2, y2 = odom_xy.T

  plt.plot(x1,y1)
  plt.plot(x2,y2)
  plt.legend(["gps", "odom_calibrated"], loc ="lower left")
  plt.show()