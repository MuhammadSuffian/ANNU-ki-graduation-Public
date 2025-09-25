import hashlib
HASHED_PASSWORD = hashlib.sha256("ANAA_GRAD_YAYYY".encode("utf-8")).hexdigest()
print(HASHED_PASSWORD)