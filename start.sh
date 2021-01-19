echo vm.max_map_count=655360 >> /etc/sysctl.conf
sysctl -p
docker-compose up -d