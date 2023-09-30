script_dir=$(dirname $(readlink -f "$0"))

echo
echo "******************"
echo "Stopping servers"
echo "******************"
$script_dir/stop_servers.sh
echo
echo "******************"
echo "Starting servers"
echo "******************"
$script_dir/start_servers.sh
echo