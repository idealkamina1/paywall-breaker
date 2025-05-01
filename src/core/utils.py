def log_error(message):
    with open('error.log', 'a') as f:
        f.write(f'ERROR: {message}\n')


def log_info(message):
    with open('info.log', 'a') as f:
        f.write(f'INFO: {message}\n')


def validate_url(url):
    import re
    pattern = re.compile(r'^(http|https)://')
    return pattern.match(url) is not None


def handle_exception(e):
    log_error(str(e))
    return {"error": str(e)}, 500


def format_response(data):
    return {"data": data} if data else {"data": None}