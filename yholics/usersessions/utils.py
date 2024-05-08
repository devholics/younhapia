def get_session_token(request):
    return request.headers.get("x-session-token")
