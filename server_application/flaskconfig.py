import os 
# For debug mode change the FLASK_DEBUG flag in .env
# For some reason flask doesn't repect the ordinary DEBUG flag.
TESTING = False

if os.environ["FLASK_ENV"] == "production":
    HOST = "0.0.0.0" # runs flask on public IP instead of localhost
elif os.environ["FLASK_ENV"] == "develop":
    HOST = None
else:
    print("Invalid flask environment set in, FLASK_ENV environment variable")
    exit(-1)

PORT = 5000