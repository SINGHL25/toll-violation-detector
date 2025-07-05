### 🔹 storage/upload_to_s3.py
```python
import boto3

def upload_file(file_name, bucket, object_name=None):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(file_name, bucket, object_name or file_name)
        print("Uploaded to S3")
    except Exception as e:
        print("❌ Upload failed:", e)
```
