import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)

tags_scores = {
    'rust': 2,
    'python': 3,
    'golang': 1,
    'redis': 1,
    'docker': 1,
    'linux': 1,
    'software': 1,
    'c': 1,
    'memcache': 1,
    'flask': 1,
}
    

# Add the keys with scores     
for tag, score in tags_scores.items():
    r.zadd('tags', score, tag)

# Retrieve the top 5 keys
for key, score in r.zrevrange('tags', 0, 4, 'withscores'):
    print(key, score)
