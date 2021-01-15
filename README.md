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

## 安装环境(dockerUI-elasticsearch-neo4j-kibana-mysql) + 安装后台服务环境(uvicorn-gunicorn-fastapi)

```shell
git clone https://github.com/wusaisa/KGQA.git
cd ./KGQA
docker-compose -f env-compose.yml up -d
```

### 单元测试地址
`http://localhost:11000/docs`

### dockerUi地址:账号admin，密码自己设置
`http://localhost:9000/#/init/admin`

### kibana地址
`http://localhost:5601/app/kibana`

### neo4j地址：账号/密码都是neo4j
`http://localhost:7474/browser/`

### mysql的配置
```python
HOST = 'mysql'
USER = 'root'
PASSWORD = 'password'
CHARSET = 'utf8mb4'
DB = 'wss'
```
