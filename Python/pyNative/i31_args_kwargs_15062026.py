def log_event(message, *args, **kwargs):
    print(f"Event: {message}")

    if args:
        print(f"Details: {args}")

    if kwargs:
        print(f"Metadata: {kwargs}")


log_event("User Login", "admin", "dashboard", timestamp="10:00", status="Succes")

