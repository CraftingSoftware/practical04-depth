import typer
import kv_get
import kv_put

app = typer.Typer()


@app.command()
def get(key: str):
    """
    Retrieve the value of the given key from the datastore and print it.

    Args:
        key: Key of value to print
    """
    filepath = "data.json"
    if not kv_get.check_file_exists(filepath):
        kv_get.create_empty_file(filepath)
    file = kv_get.open_file(filepath)
    data = kv_get.get_json(file)
    print(kv_get.get(key, data))


@app.command()
def put(key: str, value: str):
    """
    Store the key-value pair in the datastore.

    Args:
        key: Key to store
        value: Value to store
    """
    kv_put.put(key, value, "data.json")


if __name__ == "__main__":
    app()
