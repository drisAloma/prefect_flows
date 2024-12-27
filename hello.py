from prefect import flow


@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = True):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")

# print(hello_world())

# if __name__ == "__main__":
#     hello_world()
