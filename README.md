# mnbvc mutilmodal doc parse
将使用 mmda 将多个 pdf 文档解析为 jsonl 文件

## Setup
```shell
conda create -n mmdp python=3.8
conda activate mmdp

git submodule init
git submodule update

cd mnbvc_mmda
pip install -e '.[dev,recipes]'
```


