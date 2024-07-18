source .env
echo "stopping any pre-existing db containers..."
sudo podman container stop $DB_CONTAINER_NAME & sudo podman container rm  $DB_CONTAINER_NAME

echo "removing existing networks"
sudo podman network rm notes
