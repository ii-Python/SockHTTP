# Modules
from .statuscodes import status_codes
from .headers import generate_headers
from ..templates import render_template

# Main function
def process(core, request):

    # Check our endpoints
    if not request.endpoint in core.endpoints:

        return (render_template("""
        <!DOCTYPE html>
        <html lang = "en">
            <head>
                <title>404 Not Found</title>
            </head>
            <body>
                <h2>404 Not Found</h2>
                <hr>
                <p>The requested URL could not be found.</p>
                <br> <em>SockHTTP/Python %PY_VERSION</em>
            </body>
        </html>
        """), 404)

    # Check endpoint method
    ep = core.endpoints[request.endpoint]

    if ep["method"] != request.method:

        return (render_template("""
        <!DOCTYPE html>
        <html lang = "en">
            <head>
                <title>405 Method Not Allowed</title>
            </head>
            <body>
                <h2>405 Method Not Allowed</h2>
                <hr>
                <p>The requested method is not allowed for this endpoint.</p>
                <br> <em>SockHTTP/Python %PY_VERSION</em>
            </body>
        </html>
        """), 405)

    # Callback & response
    resp = ep["callback"]()

    return (resp, 200)

def send(conn, data, status, headers = {}):

    # Turn data into string
    data = str(data)

    # Fetch our status info
    if not str(status) in status_codes:

        raise ValueError("% is not a valid HTTP status code!" % status)

    # Load headers
    headers = generate_headers(headers, data)

    # Turn into a valid HTTP response
    data = f"""
HTTP/1.1 {status} {status_codes[str(status)]}
{headers}
{data}
    """

    # Encode & send
    data = data.encode("UTF-8")

    conn.sendall(data)
