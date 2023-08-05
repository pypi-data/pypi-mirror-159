# CheXpert Classification with EfficientNet B3 🫁⚕️
![picture](https://drive.google.com/uc?export=view&id=11NQIH2k1jZxBC1uzb7l25z8un_DSj0Ta)

This Package contains EfficientNet B3 model which has been trained over CheXpert Small version for 30 epochs and can be used to classify chest X-ray images for 14 classes including:
- No Finding
- Enlarged Cardiomediastinum
- Cardiomegaly
- Lung Opacity
- Lung Lesion
- Edema
- Consolidation
- Pneumonia
- Atelectasis
- Pneumothorax
- Pleural Effusion
- Pleural Other
- Fracture
- Support Devices


# What is CheXpert?
[CheXpert](https://stanfordmlgroup.github.io/competitions/chexpert/) is a large dataset of chest X-rays [this paper](https://arxiv.org/abs/1901.07031) and competition for automated chest x-ray interpretation, which features uncertainty labels and radiologist-labeled reference standard evaluation sets.

![picture](https://drive.google.com/uc?export=view&id=1tnYxCsA_iSrqSSvBJWjsdZB9QwBVL18P)

##### Why CheXpert? 🫁⚕️:

Chest radiography is the most common imaging examination globally, critical for screening, diagnosis, and management of many life threatening diseases. Automated chest radiograph interpretation at the level of practicing radiologists could provide substantial benefit in many medical settings, from improved workflow prioritization and clinical decision support to large-scale screening and global population health initiatives. For progress in both development and validation of automated algorithms, we realized there was a need for a labeled dataset that (1) was large, (2) had strong reference standards, and (3) provided expert human performance metrics for comparison.

##### Why is EfficientNet efficient? 🏛️:


- EfficientNet uses a technique called compound coefficient to scale up models in a simple but effective manner. Instead of randomly scaling up width, depth or resolution, compound scaling uniformly scales each dimension with a certain fixed set of scaling coefficients.

- EfficientNets have been the SOTA for high quality and quick image classification. They were released about 2 years ago and were quite popular for the way they scale which made their training much faster compared to other networks.


![picture](https://drive.google.com/uc?export=view&id=1UUJBDuqWLhWp-KDz20r9DcXfkQjXaxdh)
![picture](https://drive.google.com/uc?export=view&id=1I2uXduRmUCikEe7-H1Pv8Zetn_SarHqF)



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mehdihosseinimoghadam/Chexpert/blob/main/Chexpert.ipynb)





Prerequisites 🧰
-------------
- `Python 3.6` 
- `Pytorch`
- `Numpy`
- `Pandas`
- `gdown`



# Accuracy 📈
Here is the Area Under ROC for the model:

![picture](https://drive.google.com/uc?export=view&id=1TUw3IXe_OvZRKSYaa59wtHXBfYLHPtzn)






## Features

- Easy to use
- Fast
- Accurate

## Usage

Pip install the package:
```
pip install ChexpertClassifier==0.0.1
```
Download Weights :

```sh
gdown https://drive.google.com/uc?id=1--QV0N-Zb2xJfQlhIoawREpT8sGH4zWA
```

Some Imports
```py
from Chexpert_Classifier import chexpert_classifier
```

Run the model:

```py
chexpert_classifier(pathInputImage = '/content/download (3).jpeg',pathOutputImage = 'heatmap_view1_frontal.png',pathModel = '/content/m-epoch0-12072022-085549.pth.tar')
```



## Author

| Name | Github | Home Page |
| ------ | ------ | ------|
| Mehdi Hosseini Moghadam | https://github.com/mehdihosseinimoghadam |https://mehdihosseinimoghadam.github.io/|


## License

MIT

**Free Software, Hell Yeah!**


