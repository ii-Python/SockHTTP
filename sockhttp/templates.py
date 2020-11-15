# Modules
import sys
from os.path import exists

# Initialization
keys = {
    "PY_VERSION": f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}"
}

# Main function
def render_template(template):

    # Read from it
    if exists(template):

        data = open(template, "r").read()

    else:

        data = template

    # Parse custom strings
    for key in keys:

        data = data.replace(f"%{key}", keys[key])

    return data
