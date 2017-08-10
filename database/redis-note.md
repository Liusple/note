1. ```
   安装
   apt-get install redis-server
   ps ajx | grep redis
   redis-cli
   ```

2. ```
   #key
   keys *
   exists key
   type key
   del key
   expire key seconds 
   ttl key
   ```

3. ```
   #string
   set key value
   get key 
   setex key seconds value
   mget key []
   incr key/decr key
   incrby key increment
   decrby key increment
   append key value
   strlen key
   ```

4. ```
   #hash
   hset key field value []
   hgetall key
   hkeys key
   hvals key
   hlen key
   hget key field
   hdel key field []
   hexists key field
   ```

5. ```
   #list
   lpush key value []
   lpop/rpop key 
   insert before/after pivot value
   lrange key 0 -1
   llen key
   lindex key index
   ltrim key 0 2 裁剪
   ```

6. ```
   #set
   sadd key member []
   smembers key #获取所有值
   scard key  #获取个数
   sismember key value 
   sinter key1 key2
   sdiff key1 key2
   sunion key1 key2
   ```

7. ```
   #zset
   zadd key score member []
   zrange key start stop
   zcard key 
   zcount key min max
   zscore key member
   ```

8. ```reStructuredText
   subscribe    频道 []
   unsubscribe  频道 []
   publish      频道 消息
   ```

9. ```
   #主从
   主：bind ip
   从：bind ip  / slave of ip port

   ```

10. ​