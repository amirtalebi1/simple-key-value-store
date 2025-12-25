class KeyValueStore:
    def __init__(self):
        self.store = {}

    def set_value(self, key, value):
        """Store a value with the given key."""
        self.store[key] = value
        print(f"Set {key} = {value}")

    def get_value(self, key):
        """Retrieve a value by key."""
        return self.store.get(key, None)


def main():
    kv = KeyValueStore()

    
    kv.set_value("name", "Alice")
    kv.set_value("age", 25)

    print("name:", kv.get_value("name"))
    print("age:", kv.get_value("age"))
    print("city:", kv.get_value("city"))  # None چون وجود ندارد


if __name__ == "__main__":
    main()
