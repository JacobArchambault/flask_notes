source .env
echo "stopping any pre-existing db containers..."
podman container stop $DB_HOST & podman container rm  $DB_HOST

echo "removing existing networks"
podman network rm notes
