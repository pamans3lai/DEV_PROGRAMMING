import requests


def get_todo_data(todo_id):
    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    try:
        response = requests.get(url, timeout=5)

        # berikut akan memunculkan error saat status di 4xx atau 5xx
        response.raise_for_status()

        data = response.json()
        print(f"Data: {data}")

    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err}")
    except requests.exceptions.ConnectionError:
        print(f"Eerror: Mungkin tidak dapat terhubung ke server")
    except Exception as e:
        print(f"An error occured: {e}")


get_todo_data(1)
