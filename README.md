# CoachAI
Tensorflow implementation of badminton serving machine parameter predictions using AI models.

## Paper
**Training a Group of Badminton Serving Machines to Reproduce a Rally (Work in Progress)**

Yu-Fu Wu, Huang-Yi Cheng, Yun-Tang Lin, Jen-Jee Chen, Ting-Hui Chiang, Yu-Chee Tseng
ICPAI 2020

For more details:

[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9302654)

## Requirements
This code was tested with Tensorflow 1.13.1, CUDA 10.0 and Ubuntu 16.04.

Packages install:
```shell
pip install pydot==1.2.3
apt install graphviz
pip install piexif
pip install similaritymeasures
```

## Dataset
You can download datasets from [here](https://drive.google.com/drive/folders/17TZa2yybmFq-Imuk4zIMyQKSJ2T3P-T7?usp=sharing) (permission needed).

## Training
We provide several models for training. You can choose one of the following models for training.
* cnn_regression_rmse_image.ipynb
* cnn_regression_rmse_trajectory.ipynb
* dense_regression_rmse_image.ipynb
* dense_regression_rmse_trajectory.ipynb
* lstm_regression_rmse.ipynb

You can monitor the learning process using `tensorboard` and pointing it to your chosen `logs`.

## Testing
We provide a single model (LSTM model). You can try it by runnung `lstm_regression_rmse.ipynb` and uncomment by following:
```python
# Load model
model_dir = "models/20201216_lstm-rmse-position5-trajectory3-all-diff-euclidean-32-8-batchsize128-relu-epoch1000/"
model_name = "20201216_lstm-rmse-position5-trajectory3-all-diff-euclidean-32-8-batchsize128-relu-epoch1000.h5"
model_path = os.path.join(model_dir, model_name)
model = keras.models.load_model(model_path,
                                custom_objects={'root_mean_squared_error': root_mean_squared_error})

# eval_his = model.evaluate_generator(test_generator(), steps=len(test_list), verbose=1)
```
