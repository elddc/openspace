sudo mkdir -p /etc/nginx/ssl/almamarket.com
cd /etc/nginx/ssl/almamarket.com/
sudo openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out myserver.crt -keyout myserver.key
cd -