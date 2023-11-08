# GPS-VIO Data Alignment

It is essential to note that the data originating from various sensors used in an Autonomous Vehicle is typically not in the same coordinate frame. Often, this data requires alignment before it can be effectively used for localization or mapping. This code provides a detailed explanation of how to seamlessly synchronize and align GPS and VIO (Visual-Inertial Odometry) data that exist in different coordinate systems. This alignment enables the fusion of data and even allows for visualization of VIO data in the GPS coordinate frame. The code is designed to align the data using as few as 20 high-quality GPS data points.

## Ground Truth Data of GPS and VIO
![Unaligned GPS and VIO Data](https://github.com/nikunjparmar828/GPS-VIO-Data-Alignment/assets/26133653/3bebb768-b114-4648-8602-3cbb44be7528)

## Aligned Data of GPS and VIO
![Aligned GPS and VIO Data](https://github.com/nikunjparmar828/GPS-VIO-Data-Alignment/assets/26133653/76f25116-c2b9-4aea-b097-76bef35f0177)
