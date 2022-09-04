# 启动prometheus grafana docker
docker pull prometheus
docker run --name prometheus -p 9090:9090 -v /root/config/prom.yml:/etc/prometheus/prometheus.yml -d prom/prometheus
docker run -d --name gra -p 3000:3000 grafana/grafana