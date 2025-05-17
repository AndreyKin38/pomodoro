import redis

from settings import Settings


def get_redis_connection() -> redis.Redis:
    settings = Settings()
    return redis.Redis(
        host=settings.CACHE_HOST,
        port=settings.CACHE_PORT,
        db=settings.CACHE_DB
    )


# def set_pomodoro_count():
#     redis_server = get_redis_connection()
#     redis_server.set('pomodoro_count', 1, ex=10)
    # redis_server.json('pomodoro_count', 1, ex=10)
    # value = redis_server.get('pomodoro_count')
    # return value


# if __name__ == '__main__':
#     print(set_pomodoro_count())