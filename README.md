# Recreation of Ultra-low bitrate video compression using deep animation models
This repository is a recreation of https://github.com/Goluck-Konuko/animation-based-codecs.

It contains the source code for the papers
[ULTRA-LOW BITRATE VIDEO CONFERENCING USING DEEP IMAGE ANIMATION](https://arxiv.org/abs/2012.00346v1),
[A HYBRID DEEP ANIMATION CODEC FOR LOW-BITRATE VIDEO CONFERENCING](https://arxiv.org/abs/2207.13530) and 
[PREDICTIVE CODING FOR ANIMATION-BASED VIDEO COMPRESSION](https://arxiv.org/abs/2307.04187)


## Installation

 ```python3``` is supported. To install the dependencies run:
```
pip install -r requirements.txt
```
Ideally inside of a virtual environment. It's recommended to set up the environment in Linux, as some packages may not be avaliable, at least under the name in the requirements file, on Windows.

## Components

### YAML Config
These files handle the configuration settings for for training and testing the models. 
See ```config/dac.yaml```, ```config/hdac.yaml```,```config/rdac.yaml```.


### Datasets
The datasets used in this project were: ```VoxCeleb```, ```Crema-d```, and ```Vox```.
These can be found online Others may be utilized at your own discretion.
The videos should be cropped to the speaker's face at a resoltution of 256x256.
Additionally, preprocessed videos were used for evalutation and can be obtained at the following link: (https://drive.google.com/drive/folders/1g0U1ZCTszm3yrmIewg7FahXsxyMBfxKj?usp=sharing)

If utilizing them, place ```VoxCeleb```, ```Crema-d```, and ```Vox``` in the datasets_inference directory.
Place the preprocessed videos in the datasets_directory.

### Pre-trained checkpoint
Checkpoints can be found under following link: [google-drive](https://drive.google.com/drive/folders/1_jIt9Bg-o_1-8_11DkVuHBvqHQH5e4tS). Download and place in the ```cpks/``` directory.



#### Metrics
Metrics used in the evaluation include: 'psnr', 'lpips', 'dists', 'msVGG', 'fsim', 'ms_ssim', and 'vmaf'.


## Training
Set the ```config/[MODEL_NAME].yaml``` parameters appropriately or use default  and run ```bash script_training.sh [MODEL_NAME]```. 
The default setup uses a single GPU (NVIDIA-A100). However, training DAC, HDAC and RDAC can be trained on multiple GPUs by using distributed dataparallel and setting ```--device_ids``` parameter as desired.
Additionally, the run.py file can be used to start the scripts.

## Testing
Conventional video codecs (HEVC, VTM) can be downloaded from this link: (https://drive.google.com/drive/folders/1KJELtQO_RvpFqu9YZYaXhyOksdbv9zWh) 
Place them in the ```conventional_codecs/``` folder.
Set the ```eval_params``` on the ```config/[MODEL_NAME].yaml``` file to your liking (or use default) and run ```bash script_test.sh [MODEL_NAME]```.
Additionally, the run.py file can be used to start the scripts.


## Attributions
This code base  contains source code from the following works:
1.  [First Order Motion Model for Image Animation](https://papers.nips.cc/paper/8935-first-order-motion-model-for-image-animation) for the base architecture of deep image animation with unsupervised keypoints.
2. [Compressai](https://github.com/InterDigitalInc/CompressAI) for Learned image compression.
3. [JPEG-AI](https://gitlab.com/wg1/jpeg-ai/jpeg-ai-qaf) for evaluation metrics.

## Additional Information
Email me at braswellry0607@gmail.com if there are any concerns regarding this project.
For additional assistance in setting up the code, consult this document: https://docs.google.com/document/d/1lF4P59IoeOmoaX6x3N7DGGZ8LMWUfIXGgIq4eVunSX0
