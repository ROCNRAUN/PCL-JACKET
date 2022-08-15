# PCL 夹克

## 安装


第一步：

[Nvdia驱动](https://www.nvidia.com/download/index.aspx) 需确保支持 CUDA 11.2 版本

[CUDA 11.2](https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda_11.2.0_460.89_win10.exe)

[CUDNN 8.2.1](https://developer.download.nvidia.com/compute/machine-learning/cudnn/secure/8.2.1.32/11.3_06072021/cudnn-11.3-windows-x64-v8.2.1.32.zip)

第二步：

```bash
# PCL-JACKET 这个目录下运行 cmd
pip install ./packages/paddlepaddle_gpu-2.3.1.post112-cp39-cp39-win_amd64.whl && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && cd ./packages/PaddleOCR-2.5.0 && python setup.py build && python setup.py install && cd ../../
```

## 准备
直播界面全屏化（1920x1080）

在CDK出现的地方应不存有任何遮挡物

## 使用


```bash
python main.py
```

识别、输入、领取CDK的过程是全自动的
