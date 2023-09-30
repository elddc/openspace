# When accessing the public IP of your EC2 we get a 500 internal server error. 
# Checking the logs of nginx at /var/log/nginx/error.log revela there is some 
# issue with access rights. Executing the below commands fixes this issue
cd ~
sudo cat /var/log/audit/audit.log | grep nginx | grep denied | audit2allow -M mynginx
sudo semodule -i mynginx.pp
cd -