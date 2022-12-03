from bucket import bucket

def all_bucket_objects_task():
    result = bucket.get_objects()
    if result['KeyCount']:
        return result['Contents']
    else:
        return None
