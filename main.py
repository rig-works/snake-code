import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


# #Bad Pratice1 - passwords 
# username = refael 
# password = "TobeORNO5TtoBe123" 

# aws_secret_access_key = 'tQtSurrh+N3zqFDPEPZ95050c+GGQs+Xx1AF/wVc' 
# api_token=glpat-e31Y_mAqvRTbZBXTZyFf 



# #Bad Pratice1 - passwords 
# username = user_refael 
# password = "TobeOR!=toBe123" 

# aws_secret_access_key = 'tQtSurrh+N3zqFDPEPZ95050c+GGQs+Xx1AF/wVc' 
# api_token=glpat-e31Y_mAqvRTbZBXTZyFf 
