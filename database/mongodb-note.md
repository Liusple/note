1. ```
   sudo service mongod start/restart
   ps ajx | grep mongod
   /etc/mongod.conf
   mongo #客户端
   db #查看当前数据库
   show dbs
   use dbname
   db.status()
   ```

2. ```
   db.createCollection('stu') 
   show collections
   db.stu.drop()
   ```

3. ```
   db.stu.insert({})
   db.stu.find(条件)
   db.stu.findOne().pretty()
   du.stu.update({条件}, {$set:{name:'alex'}}, {multi:true})
   db.stu.remove({gender:0}, {justOne:true})
   db.stu.remove({})
   db.stu.save({})#如果存在则修改，不存在则创建
   db.createCollection('stu', {capped:true, size:10})
   ```

4. ```
   db.stu.find({name:'lius'})
   db.stu.find({age:{$gt:19}})
   $lt小于
   $lte小于等于
   $ne不等于
   $gte大于等于
   #逻辑运算符
   db.stu.find({age:{$gte:18}, gender:1}) #与
   db.stu.find({$or:[{age:{$gt:19}}, {gender:1}]}) #或
   #范围运算符
   db.stu.find({age:{$in:[14, 25]}})
   db.stu.find({name:/^刘/}) or db.stu.find({name:{$regex:'^刘'}})
   db.stu.find({$where:function(){return this.age>20}})
   db.stu.find().skip(1).limit(2)
   ```

5. ```
   #投影
   db.stu.find({}, {name:1, _id:0})
   #排序
   db.stu.find().sort({gender:-1})
   #统计
   db.stu.find().count()
   db.stu.count({age:{$gt:20}, gender:1})
   #消除重复
   db.stu.distinct('去重字段', {条件})
   db.stu.distinct('gender', {age:{$gt:19}})#查找年龄大于19岁的性别，去重
   ```

6. ```
   管道：
   $group 
   $match 过滤数据，只输出符合条件的文档
   $project 修改输入文档的结构，如重命名，增加，删除字段，创建计算结果
   $sort
   $limit
   $skip
   $unwind 拆分

   表达式：
   $sum
   $avg
   $min
   $max
   $push 在结果文档中插入值到一个数组中
   $first 
   $last

   db.stu.aggregate([
     {$group:
     	{
       	_id:'$gender',
       	counter:{$sum:1}
     	}
     }
   ])
   #group by null将集合所有文档分为一组
   db.stu.aggregate([
     {$group:
       {
         _id:null,
         counter:{$sum:1},
         avgAge:{$avg:'$age'}
       }
     }
   ])

   db.stu.aggregate([
     {$group:
     	{
     	  _id:'$gender',
         name:{$push:'$name'}  #name:{$push:'$$ROOT'} $$ROOT将文档内容加入到结果集的数组中
     	}
     }
   ])

   db.stu.aggregate([
     {$match:{age:{$gt:20}}},
     {$group:{_id:'$gender', counter:{$sum:1}}}
   ])

   db.stu.aggregate([
     {$group:{_id:'$gender', counter:{$sum:1}}},
     {$project:{_id:0, counter:1}}
   ])

   db.stu.aggregate([
     {$group:{_id:'$gender', counter:{$sum:1}}},
     {$sort:{counter:-1}},
     {$skip:1},
     {$limit:1}
   ])

   db.stu.aggregate([{$unwind:'$字段名称'}])
   db.stu.aggregate([{
     $uwind:{
       path:'$字段',
       preserveNullAndEmptyArrays:<boolean>#防止数据丢失
     }
   }])
   ```

7. ```
   1)
   use admin
   db.createUser({
     user:'admin',
     pwd:'123',
     roles:[{role:'root', db:'admin'}]
   })
   2)
   vi /etc/mongod.conf
   security:
   	authorization: enabled

   3)mongo -u 'admin' -p --authenticationDatabase 'admin'
   4)use test1
   db.createUser({
     user:'t1',
     pwd:'123',
     roles:[{role:'readWrite', db:'test1'}]
   })
   5)mongo -u t1 -p --authenticationDatabase test1
   ```

8. ```
   #备份 mongodump -h dbhost -d dbname -o dbdirectory
   #恢复 mongorestore -h dbhost -d dbname --dir dbdirectory
   ```

9. ```
   副本集
   1. mongod --bind_ip 192.168.196.128 --port 27017 --dbpath ~/Desktop/t1 --replSet rs0
   mongod --bind_ip 192.168.196.128 --port 27018 --dbpath ~/Desktop/t2 --replSet rs0
   2. 
   mongo --host 192.168.196.128 --port 27017
   rs.initiate()
   rs.add('192.168.196.128:27018')
   use test1
   for(i=0;i<10;i++){db.t1.insert({_id:i})}
   db.t1.find()
   3.
   mongo --host 192.168.196.128 --port 27018
   rs.slaveOk()
   db.t1.find()
   删除从节点
   rs.remove('192.168.196.128:27018')
   ```

10. ​