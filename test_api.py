import requests
import io
import jwt
import os
from dotenv import load_dotenv

load_dotenv()

# Create a dummy token using SUPABASE_JWT_SECRET
secret = os.getenv('SUPABASE_JWT_SECRET')
if not secret:
    print("No SUPABASE_JWT_SECRET, testing without auth or using a fake one might fail if auth is required.")
    token = "fake_token"
else:
    token = jwt.encode({"sub": "test_user", "aud": "authenticated", "role": "authenticated"}, secret, algorithm="HS256")

print(f"Testing HTTP endpoint with token: {token[:10]}...")

pdf_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n" # tiny invalid PDF, should fail validation but return fast

files = {'resume': ('test.pdf', pdf_content, 'application/pdf')}
data = {'job_description': 'test job'}
headers = {'Authorization': f'Bearer {token}'}

try:
    res = requests.post("http://127.0.0.1:8000/api/v1/analyze-resume", files=files, data=data, headers=headers, timeout=120)
    print("Status:", res.status_code)
    print("Response:", res.text)
except Exception as e:
    print("HTTP Error:", e)
