from rest_framework.response import Response


def envelope(data, status=200, status_text="OK", tests=None):
    body = {"status": status, "statusText": status_text, "data": data}
    if tests is not None:
        body["tests"] = tests
    return Response(body, status=status)