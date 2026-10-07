import docker


def test_docker_connection():
    print("Initializing Faye...")
    try:
        client = docker.from_env()
        # Ping the Docker daemon to ensure it is running and reachable
        client.ping()
        print("[SUCCESS] Faye connected to Docker daemon successfully!\n")

        containers = client.containers.list(all=True)
        print(f"Total containers found: {len(containers)}")

        for container in containers:
            network_settings = container.attrs["NetworkSettings"]["Networks"]
            network_names = list(network_settings.keys())
            print(
                f"- Name: {container.name} | Status: {container.status} | Networks: {network_names}"
            )

    except Exception as e:
        print("[ERROR] Could not connect to Docker daemon.")
        print(f"Details: {e}")


def main():
    test_docker_connection()


if __name__ == "__main__":
    main()
