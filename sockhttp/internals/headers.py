# Main function
def generate_headers(additional, data):

    headers = {
        "Server": "SockHTTP/1.0.2",
        "Content-Length": f"{len(data)}",
        "Content-Type": "text/html"
    } | additional

    head_str = ""

    for header in headers:

        head_str += f"{header}: {headers[header]}\n"

    return head_str
