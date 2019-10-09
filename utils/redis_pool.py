import redis

# 抽取封装成模块，全局使用（单例模式，redis_pool.py）
POOL = redis.ConnectionPool(host='116.62.155.103', port=6379, max_connections=1000)