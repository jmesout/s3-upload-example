# S3 File Uploader

This Python script allows you to upload files from a specified directory (including subdirectories) to an S3 bucket or compatible storage (Civo Object Store) using custom endpoint and authentication parameters managed via an `.env` file.

## Prerequisites

Before you can run this script, you will need:

- Python 3.x installed on your machine.
- An S3 bucket or S3 compatible Storage (Civo Object Store).
- An `.env` file configured with your credentials.

## Setup

1. **Clone the Repository**

   Start by cloning this repository to your local machine:
   ```bash
   git clone https://yourrepository.git
   cd yourrepository
   ```

2. **Install Python Dependencies**
    Install the required Python packages using the following command:

    ```bash
        pip install -r requirements.txt
    ```

3. **Configure the .env File**
    Create an .env file in the root directory of the project (an example is given), and populate it with the following variables:
    ```
        AWS_ACCESS_KEY_ID=your_access_key
        AWS_SECRET_ACCESS_KEY=your_secret_key
        S3_BUCKET=your_bucket_name
        S3_ENDPOINT_URL=objectstore.lon1.civo.com
    ```
    Replace your_access_key_id, your_secret_access_key, your_bucket_name, your_s3_endpoint_url, and path_to_your_directory with your actual  credentials, bucket details, and the directory from which you want to upload files (upload folder by default).

4. **Run the Upload Script**
    ```bash
        python3 main.py
    ```
