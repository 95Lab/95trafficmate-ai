# 95trafficmate-ai
TrafficMate is innovatively built upon a Multimodal framework, integrating diverse data sources to enhance traffic management and congestion prediction.

## Repository structure
- timeseries2raster: the algorithm to convert sensing data stored in time-series format to raster images.
- prep3Draster: the algorithm to individual raster images to video-like data.
- learning_model:
  - 3D_CNN: a deep learning model predict information by preserving both spartial and temporal relationships using 3D-CNN.
  - train_singlemodal.py: to train the model using only 1 factor (target factor)
  - predict_singlemodal.py: to predict data using the model produced from train_singlemodal
  - train_multimodal.py: to train the model using many factors
predict_multimodal.py: to predict data using the model produced from train_multimodal

- jpmesh: convert mesh code to coordinate 
- data_sample: sample dataset to run the algorithm