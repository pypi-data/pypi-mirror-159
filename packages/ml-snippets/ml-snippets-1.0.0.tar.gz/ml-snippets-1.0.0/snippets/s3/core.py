from minio import Minio

def new_bucket(bucket_name):
    client = Minio('minio:9000',
               access_key='symend',
               region ="my-region",
               secret_key='symend123',
              secure=False)
    client.make_bucket(bucket_name)
    
def list_buckets():
    client = Minio('minio:9000',
               access_key='symend',
               region ="my-region",
               secret_key='symend123',
              secure=False)
    return client.list_buckets()

def upload_file(bucket_name, filename):
    client = Minio('minio:9000',
               access_key='symend',
               region ="my-region",
               secret_key='symend123',
              secure=False)
    client.fput_object(bucket_name, filename, filename)
    
def download_file(bucket_name, filename):
    client = Minio('minio:9000',
               access_key='symend',
               region ="my-region",
               secret_key='symend123',
              secure=False)
    client.fget_object(bucket_name, filename, filename)
    
def delete_file(bucket_name, filename):
    client = Minio('minio:9000',
               access_key='symend',
               region ="my-region",
               secret_key='symend123',
              secure=False)
    client.remove_object(bucket_name, filename)
    
def delete_bucket(bucket_name):
    client = Minio('minio:9000',
               access_key='symend',
               region ="my-region",
               secret_key='symend123',
              secure=False)
    client.remove_bucket(bucket_name)
    
def list_objects(bucket_name):
    client = Minio('minio:9000',
               access_key='symend',
               region ="my-region",
               secret_key='symend123',
              secure=False)
    return client.list_objects(bucket_name)

