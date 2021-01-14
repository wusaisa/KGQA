# KGQA
一个问答系统

## 安装环境
```docker
docker-compose -f env-compose.yml up -d
```

### 安装后台服务环境
```docker
docker built -t kgqa:1.0 .
docker run -d -p 11000:80 --name kgqa --restart=always kgqa:1.0
```

### 单元测试
`http://localhost:11000/docs`