# PCL 夹克

## 安装


第一步：

[Nvdia驱动](https://www.nvidia.com/download/index.aspx) 需确保支持 CUDA 10.2 版本

[Anaconda 2022.05](https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/?C=M&O=D)

```bash
# 在命令行输入以下命令，创建名为paddle_env的环境
# 此处为加速下载，使用清华源
conda create --name paddle_env python=3.8 --channel https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/  # 这是一行命令
```

```bash
# 激活paddle_env环境
conda activate paddle_env
# 查看当前python的位置
where python
```

[CUDA 10.2](https://developer.nvidia.com/cuda-10.2-download-archive)

[CUDNN 7.6.5](https://cdn.7x05.xyz/cudnn.zip)

以上版本为推荐版本

第二步：
```bash
pip install -r requirements.txt
```

第三步：
```bash
python -m pip install paddlepaddle-gpu -i https://mirror.baidu.com/pypi/simple
```

## 准备
直播界面全屏化（1920x1080）

在CDK出现的地方应不存有任何遮挡物

## 使用


```bash
python main.py
```

识别、输入、领取CDK的过程是全自动的，请勿挪动鼠标
