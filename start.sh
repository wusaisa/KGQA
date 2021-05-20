echo vm.max_map_count=655360 >> /etc/sysctl.conf
if [ -d $PWD/relation/model ];then
  echo "未找到模型，正在下载模型中...."
  curl https://oss.jtyoui.com/data/wss-model.tar.gz
  echo "解压模型中...."
  tar -zxvf wss-model.tar.gz -C $PWD/relation
fi
sysctl -p
docker-compose up -d