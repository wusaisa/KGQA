# KGQA
一个问答系统

## 需要修改系统配置
```shell
vim /etc/sysctl.conf
# 最后一行追加
vm.max_map_count = 655360
# 执行命令重新加载
sysctl -p 
```

## 安装环境(dockerUI-elasticsearch-neo4j-kibana-mysql)
```shell
git clone https://github.com/wusaisa/KGQA.git
cd ./KGQA
docker-compose -f env-compose.yml up -d
```

### 安装后台服务环境(uvicorn-gunicorn-fastapi)
```shell
git clone https://github.com/wusaisa/KGQA.git
cd ./KGQA
docker build -t kgqa:1.0 .
docker run -d -p 11000:80 --name kgqa --restart=always kgqa:1.0
```

### 单元测试
`http://localhost:11000/docs`

### 插入数据在es，执行命令
```shell
pip3 install -r requirements.txt -i https://pypi.douban.com/simple
python3 operateES.py
```