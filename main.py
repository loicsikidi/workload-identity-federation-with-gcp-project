import os

from google.cloud import storage

def main(request):
    client = storage.Client()

    blobs = client.list_blobs(os.environ["BUCKET_NAME"])
    
    return {'filenames': [b.name for b in blobs]}
