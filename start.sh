echo vm.max_map_count=655360 >> /etc/sysctl.conf
sysctl -p

# 下载模型
if [ ! -d $PWD/relation/model ];then
  echo "未找到模型，正在下载模型中...."
  curl -O https://oss.jtyoui.com/data/wss-model.tar.gz
  echo "解压模型中...."
  tar -zxvf wss-model.tar.gz -C $PWD/relation
fi

# 启动
docker-compose up -d