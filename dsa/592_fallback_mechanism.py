def primary_service():
    raise ConnectionError("Primary service unavailable")


def fallback_service():
    return "Response from fallback service"


def get_response():

    try:
        response = primary_service()
        print(response)

    except ConnectionError:
        print("Switching to fallback service...")
        response = fallback_service()
        print(response)


get_response()
