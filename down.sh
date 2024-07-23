source .env
echo "stopping any pre-existing db containers..."
podman container stop $DB_CONTAINER_NAME & podman container rm  $DB_CONTAINER_NAME

echo "removing existing networks"
podman network rm notes
