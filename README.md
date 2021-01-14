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

## 安装环境
```shell
git clone https://github.com/wusaisa/KGQA.git
cd ./KGQA
docker-compose -f env-compose.yml up -d
```

### 安装后台服务环境
```shell
git clone https://github.com/wusaisa/KGQA.git
cd ./KGQA
docker built -t kgqa:1.0 .
docker run -d -p 11000:80 --name kgqa --restart=always kgqa:1.0
```

### 单元测试
`http://localhost:11000/docs`