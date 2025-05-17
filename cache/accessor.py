import os

import redis


def get_redis_connection() -> redis.Redis:
    return redis.Redis(
        host="localhost",
        port=6379,
        db=0
    )


# def set_pomodoro_count():
#     redis_server = get_redis_connection()
#     redis_server.set('pomodoro_count', 1, ex=10)
    # redis_server.json('pomodoro_count', 1, ex=10)
    # value = redis_server.get('pomodoro_count')
    # return value


# if __name__ == '__main__':
#     print(set_pomodoro_count())