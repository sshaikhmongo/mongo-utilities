# mongo-utilities

Welcome. Here you will find python utilities that allow you to work with data in MongoDB. This example was built using [MongoDB Atlas](https://account.mongodb.com/account/login). Click here to set up your free forever cluster today!

## loadMgenData.py

### Prerequisites

- Install [MgenerateJS](https://www.npmjs.com/package/mgeneratejs)
- Install [Python3](https://www.python.org/downloads/)
- Setup and configure a MongoDB Atlas cluster with sample data loaded
- Under the network settings -> IP Whitelist, add in your machine's IP or 0.0.0.0/0 for dev environments

### Steps to run loadMgenData.py

1. Clone repo
2. Edit the following in loadMgenData.py:
   - Line 7: CONNECTION_STRING = "mongodb+srv://<user_name>:<password>@<hostname>/sample_airbnb" <-- Insert your Mongo username, password, and hostname.

The current implementation assumes that you want to add 3 fields (generated using Mgenerate) into an existing MongoDB Airbnb sample dataset.
