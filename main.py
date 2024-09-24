import os

from flask import Flask

app = Flask(__name__)

# Bad Pratice1 - passwords
username = refael
password = "TobeORNOTtoBe123"

# Bad Pratice2 - keys
# Hardcoded AWS credentials (for demonstration purposes only)
aws_access_key_id = 'AKIAABCDCFGIJKLMMOP1'
aws_secret_access_key = 'tQtSurrh+N3zqFDPEPZ95050c+GGQs+Xx1AF/wVc'
region_name = 'us-west-2'

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
