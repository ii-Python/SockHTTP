# Modules
from sockhttp import SockHTTP, render_template

# Initialization
app = SockHTTP(
    log_requests = False
)

# Routes
@app.endpoint("GET", "/")
def index():

    return render_template("hi")

# Run
app.run("0.0.0.0", 80)
