# 启动prometheus grafana docker
docker pull prometheus
docker run --name prometheus -p 9090:9090 -v /root/config/prom.yml:/etc/prometheus/prometheus.yml -d prom/prometheus
docker run -d --name gra -p 3000:3000 grafana/grafana
docker run -d --name pushgateway -p 9091:9091 prom/pushgateway
wget https://github.com/prometheus/node_exporter/releases/download/v1.2.2/node_exporter-1.2.2.linux-amd64.tar.gz
