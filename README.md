# MS-COCO-DataSet-Converter

This repository is created to convert MS COCO dataset in simple format.

# Getting started 
1. Download MS COCO dataset from offical website ([link](https://cocodataset.org/ "link"))
2. Extract annotation files. Extracted file is in Json formate which need to be converted into simple formate to feed machine learning model.
3. Change the Input and output fie path in DatasetConverter.py file 
4. Repeat the above procedure for each Json file

**You can also use this repository to convert dataset and use to train your model on more than one dataset**

**I am using MS COCO 2014 version.**
**Sample of output file is also avilable in this repository**
# Data Formate
Data is stored in thr following way

**<Image_name>#<Caption_Number> <Caption>**
  
for each image MS-COCO has 5 associated caption with it
