import os
import boto3
from dotenv import load_dotenv

def upload_files(directory, bucket_name, endpoint_url):
    """
    Uploads all files from a specified directory to an S3 bucket, excluding any '.gitkeep' files.

    Parameters:
    - directory: str, the path to the directory containing the files to be uploaded.
    - bucket_name: str, the name of the target S3 bucket where files will be uploaded.
    - endpoint_url: str, the custom endpoint URL for the S3 service, used for regions or special configurations.

    The function walks through all files in the directory and its subdirectories, and uploads each to the specified S3 bucket.
    """
    # Create an S3 client using credentials and endpoint URL loaded from environment variables.
    # This client will handle all interactions with the Amazon S3 service.
    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),  # Fetch the AWS access key from environment variables
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),  # Fetch the AWS secret access key from environment variables
        endpoint_url=endpoint_url  # Set the custom endpoint URL for S3
    )

    # Traverse the directory tree using os.walk, which generates the file names in a directory tree
    # by walking either top-down or bottom-up.
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # Skip uploading '.gitkeep' files, which are placeholders to keep empty dirs in version control.
            if file.endswith('.gitkeep'):
                continue
            # Construct the full file path
            full_path = os.path.join(subdir, file)
            # Open the file in binary mode for reading
            with open(full_path, 'rb') as data:
                # Upload the file to S3, using the path as the key name in the bucket
                s3_client.upload_fileobj(data, bucket_name, full_path.replace("\\", "/"))
                # Print the path of the uploaded file to the console for confirmation
                print(f"Uploaded {full_path} to S3 bucket {bucket_name}")

if __name__ == "__main__":
    # Load environment variables from the .env file before running the rest of the script.
    load_dotenv()

    # Fetch the directory path, bucket name, and endpoint URL from the environment variables.
    directory_path = os.getenv('DIR_PATH')
    bucket = os.getenv('S3_BUCKET')
    endpoint = os.getenv('S3_ENDPOINT_URL')

    # Check if the essential environment variables are set, otherwise raise an error.
    if not bucket:
        raise ValueError("S3_BUCKET is not set in the environment variables.")
    if not endpoint:
        raise ValueError("S3_ENDPOINT_URL is not set in the environment variables.")

    # Call the upload_files function with the directory path, bucket, and endpoint.
    upload_files(directory_path, bucket, endpoint)
