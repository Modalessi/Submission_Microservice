from fastapi import Request, HTTPException, Depends
import redis
from app.Settings import Settings

settings = Settings()
RATE_LIMIT = settings.rate_limit
TIME_WINDOW = settings.time_window


r = redis.Redis(host=settings.redis_url, port=6379, db=0, decode_responses=True)


def get_identifier(request: Request):
    user = getattr(request.state, "user", None)
    if user and hasattr(user, "ID"):
        return f"user:{user.ID}"
    return f"ip:{request.client.host}"


def rate_limiter(request: Request):
    identifier = get_identifier(request)
    key = f"rate_limit:{identifier}"
    current = r.get(key)
    if current is None:

        r.set(key, 1, ex=TIME_WINDOW)
    else:
        current = int(current)
        if current >= RATE_LIMIT:
            raise HTTPException(status_code=429, detail="Rate limit exceeded. Try again later.")
        r.incr(key)


rate_limit_dep = Depends(rate_limiter)
