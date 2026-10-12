
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Cloud Portal</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #eef2f7;
                text-align: center;
                padding: 60px 20px;
            }
            .container {
                background: white;
                max-width: 600px;
                margin: auto;
                padding: 30px;
                border-radius: 12px;
            }
            h1 {
                color: #234e70;
            }
            p {
                color: #444;
                font-size: 17px;
            }
            .status {
                color: green;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Student Cloud Portal</h1>
            <p>Cloud Computing and Computer Networks Lab</p>
            <p>Deployment Model: Platform as a Service (PaaS)</p>
            <p>Application: Student Information Portal</p>
            <p class="status">Status: Ready for Cloud Deployment</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
