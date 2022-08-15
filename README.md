# PCL 夹克

## 安装


第一步：

[Nvdia驱动](https://www.nvidia.com/download/index.aspx) 需确保支持 CUDA 11.2 版本

[CUDA 11.2](https://developer.download.nvidia.com/compute/cuda/11.2.0/local_installers/cuda_11.2.0_460.89_win10.exe)

[CUDNN 8.2.1](https://developer.download.nvidia.com/compute/machine-learning/cudnn/secure/8.2.1.32/11.3_06072021/cudnn-11.3-windows-x64-v8.2.1.32.zip)

[Microsoft Visual C++ 2015-2022 Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)

[C++ 的桌面开发（Visual Studio 生成工具）](https://aka.ms/vs/17/release/vs_BuildTools.exe)

[Python 3.9.12](https://www.nvidia.cn/Download/index.aspx?lang=cn)

[FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases)
需解压到 PCL-JACKET 的根目录下

第二步：

```bash
# PCL-JACKET 这个目录下运行 cmd
pip install paddlepaddle-gpu==2.3.1.post112 -f https://www.paddlepaddle.org.cn/whl/windows/mkl/avx/stable.html && pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple && cd ./packages/PaddleOCR-2.5.0 && python setup.py build && python setup.py install && cd ../../
```

```bash
# 验证安装 
python -c "import paddle;paddle.utils.run_check()"

# 如果出现 PaddlePaddle is installed successfully! 说明您已成功安装
```

## 使用
游戏语言：繁体中文

显示模式：窗口化

分辨率：1280x720

需处于输入CDK的界面，方能自动兑换。

```bash
python main.py
```
