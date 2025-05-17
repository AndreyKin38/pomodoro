import json

from redis import Redis

from cache import get_redis_connection
from schema.task import TaskSchema


class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_task(self) -> list[TaskSchema]:
        with self.redis as redis:
            task_json = redis.lrange("tasks", 0, -1)
            res = [TaskSchema.model_validate(json.loads(task)) for task in task_json]
            return res

    def set_tasks(self, tasks: list[TaskSchema]):
        tasks_json = [task.json() for task in tasks]
        with self.redis as redis:
            redis.lpush("tasks", *tasks_json)


# if __name__ == '__main__':
#     g = get_redis_connection()
#     t = TaskCache(g)
#     print(t.get_task())
