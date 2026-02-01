# python-uv-template
使用uv管理的python项目模版
- 使用 uv 建立python虚拟环境、管理安装包
- 使用 requirements.in 管理依赖包，自动生成 requirements.txt 固定环境版本

## 项目启动
```
# 安装uv，方法一
curl -Ls https://astral.sh/uv/install.sh | bash
uv --version
uv python list

# 创建虚拟环境
uv venv --python 3.10.17
# 激活虚拟环境
source .venv/bin/activate  
# 安装依赖
uv pip compile requirements.in -o requirements.txt
uv pip sync requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

```