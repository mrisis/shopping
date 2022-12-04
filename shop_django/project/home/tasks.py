from bucket import bucket
from celery import shared_task

def all_bucket_objects_task():
    result = bucket.get_objects()
    if result['KeyCount']:
        return result['Contents']
    else:
        return None

@shared_task
def delete_object_task(key):
    bucket.delete_object(key)
