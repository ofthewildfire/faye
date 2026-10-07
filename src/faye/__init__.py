from faye.main import test_docker_connection


def main() -> None:
    print(
        "Hello ~ I'm FAYE, your friendly Docker management tool! Let's check the Docker connection...\nI'll be sure to handle all your Docker needs with care and precision. Let's get started!\n    "
    )
    test_docker_connection()


if __name__ == "__main__":
    main()
