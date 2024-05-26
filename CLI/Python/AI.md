### tensorflow
> 1. conda create --name (name) python=3.10.6
>> - python 버전 3.10.6일때 잘 동작함
> 2. pip install numpy==1.26.4
>> - numpy 버전 2 이상이면 동작 잘 안하는 거 같음
> 3. pip install tensorflow==2.10.0
>> - 테스트할 때 기준으로 2.10.0이 최신버전 이었음.
> 4. conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
>> - cuda 설치 CLI로 해야 오류없이 잘 됨.

- gpu 사용여부 체크

```python
import tensorflow as tf
tf.test.is_built_with_cuda()
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())
```

### opencv
pip install opencv-python=4.6.0.66
pip install opencv-contrib-python=4.6.0.66

pip install opencv-python
pip install opencv-contrib-python

pip install ultralytics
pip install deep-sort-realtime
12.6