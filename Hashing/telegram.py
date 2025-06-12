import hmac, hashlib

TELEGRAM_BOT_TOKEN = ""

def verify_telegram(data):
    check_hash = data.pop("hash", None)
    if check_hash is None:
        return False
    secret = hashlib.sha256(TELEGRAM_BOT_TOKEN.encode()).digest()
    data_str = "\n".join(f"{k}={v}" for k, v in sorted(data.items()))
    hmac_hash = hmac.new(secret, data_str.encode(), hashlib.sha256).hexdigest()
    return hmac_hash == check_hash
