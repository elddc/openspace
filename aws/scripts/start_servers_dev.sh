GREEN=`tput setaf 2`
RED=`tput setaf 1`
NC=`tput sgr0`

# check if pm2 is installed
pm2 --version > /dev/null 2>&1
if [[ $? -ne 0 ]]; then
        echo -e "${RED}ERROR: pm2 is not installed${NC}. Install it using ${GREEN}sudo npm install -g pm2${NC}"
        exit 1
fi

# get the path of the NextJS project. This is used to start the pm2 server later
while true; do
        read -p "Enter your NextJS project path: " path
        file="$path/next.config.js"
        if [ ! -e "$file" ]; then
                echo "${RED}\"$path\" is not a valid NextJS project path${NC}"
        else
                break
        fi
done

echo -n "Starting nginx..."
sudo systemctl restart nginx
sudo systemctl status  nginx | grep Active | grep running > /dev/null
if [[ `echo $?` -eq 0 ]]; then
        echo -e "${GREEN}Done${NC}"
else
        echo "${RED}nginx encountered ERROR${NC}"
        exit 1
fi

# create the out folder in the home directory if it does not exist
if [[ ! -d ~/logs ]]; then
        mkdir ~/logs
fi

echo -n "Starting pm2 server ..."
cd $path && pm2 start "npm run start -- -p 8080 > ~/logs/log.txt" --name alma >> ~/logs/pm2.out 2>~/logs/pm2.err >/dev/null
cd -
pm2 list | grep alma | grep online > /dev/null
if [[ `echo $?` -eq 0 ]]; then
        echo -e "${GREEN}Done${NC}"
else
        echo "${RED}pm2 encountered ERROR${NC}"
        echo "Check logs in ~/logs/pm2.out and ~/logs/pm2.err"
        exit 1
fi
