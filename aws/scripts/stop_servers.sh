GREEN=`tput setaf 2`
RED=`tput setaf 1`
NC=`tput sgr0`

echo -n "Stopping nginx..."
sudo systemctl stop  nginx
sudo systemctl status  nginx | grep Active | grep dead > /dev/null
if [[ `echo $?` -eq 0 ]]
then
        echo -e "${GREEN}Done${NC}"
else
        echo "nginx encountered ${RED}ERROR ${NC}"
        exit
fi

echo -n "Stopping pm2 server ..."
pm2 kill > /dev/null 2>&1
pm2 list | grep alma | grep online > /dev/null
if [[ `echo $?` -eq 1 ]]
then
        echo -e "${GREEN}Done${NC}"
else
        echo "pm2 encountered ${RED}ERROR ${NC}"
        exit
fi