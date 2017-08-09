1. ```
   USE database;
   SHOW DATABASES;
   SHOW TABLES;
   SHOW COLUMNS FORM customers; DESCRIBE customers;
   SHOW STATUS;
   SHOW CREATE DATABASE; SHOW CREATE TABLE;
   ```

2. ```
   SELECT DISTINCT vend_id FROM products;
   SELECT name FROM products LIMIT 5, 4;
   SELECT products.name FROM crashcourse.products;
   ```

3. ```
   SELECT name, price FROM products ORDER BY name DESC, price LIMIT 1;

   ```

4. ```
   SELECT name, price FROM products WHERE price BETWEEN 1 AND 19;
   SELECT name FROM products WHERE price IS NULL;
   SELECT name, price FROM products WHERE id IN (1002, 1003) ORDER BY name;
   ```

5. ```
   SELECT id, name FROM products WHERE name LIKE 'jet%'
   SELECT name FROM products WHERE name LIKE '%' #不会匹配NULL

   SELECT id, name FROM products WHERE name LIKE '_ ton anvil'
   ```

6. ```
   SELECT name FROM products WHERE name REGEXP '.000' ORDER BY name;
   SELECT name FROM products WHERE name REGEXP '1000 | 2000';
   SELECT name FROM products WHERE name REGEXP '[123] TON';#[^123]却匹配除这些字符外的任何东西。
   #转义 \\.匹配.

   *     0个或多个匹配
   +     1个或多个匹配
   ？    0个或1个匹配
   {n}   指定数目的匹配
   {n,}  不少于指定数目的匹配
   {n,m} 匹配数目的范围
   ^     文本开始
   $     文本结尾

   SELECT name FROM products WHERE name REGEXP '^[0-9\\.]';
   ```

7. ```
   SELECT Contact(vend_name, '(', vend_country, ')')
   FROM vendors
   ORDER BY vend_name;
   ```

8. ```
   SELECT cust_id, order_num FROM orders WHERE Date(order_date) = '2017-08-02'
   SELECT cust_id, order_num FROM orders WHERE Year(order_date) = 2012 AND Month(order_date) = 9;
   ```

9. ```
   #DISTINCT ALL
   SELECT AVG(DISTINCT prod_price) AS avg_price
   FROM products
   WHERE vend_id = 1003;
   ```

10. ```
    #子查询
    SELECT cust_name, cust_state, 
    (SELECT COUNT(*) FROM orders WHERE orders.cust_id=customers.cust_id) AS orders
    FROM customers
    ORDER BY cust_name;
    #子查询最常见的使用是在WHERE字句的IN中。
    ```

11. ```
    #联结
    联结两个表时，实际做的是将第一个表中的每一行与第二个表中的每一行配对。WHERE子句做为过滤条件，只包含那些匹配给定条件的行。
    应该保证所有联结都有WHERE子句。
    内部联结=等值联结
    ```

12. ```
    #自联结
    SELECT p1.prod_id, p1.prod_name
    FROM products AS p1, products AS p2
    WHERE p1.vend_id = p2.vend_id
    AND p2.prod_id = 'DTNTR';
    #外部联结
    LEFT/RIGHT OUTER JOIN
    ```

13. ```
    #组合查询 UNION 自动去除重复的行
    UNION ALL
    ```

14. ```
    #全文本搜索
    CREATE TABLE product(
    id   	  int 		 NOT NULL AUTO_INCREMENT,
    date	  datetime   NOT NULL,
    note_text text		 NULL,
    PRIMARY KEY(id),
    FULLTEXT(note_text)
    );
    SELECT note_text
    FROM product
    WHERE Match(note_text) Against('young');

    ```

15. ```
    UPDATE customers SET email = 'test@qq.COM',
    name = 'alex'
    WHERE id = 1999;
    ```

16. ```
    DELETE FROM customers WHERE id = 1999;
    ```

17. ```
    #更新表
    ALTER TABLE vendors ADD phone CHAR(20);
    ALTER TABLE vendors DROP COLUMN phone;
    ALTER TABLE orderitems
    ADD CONSTRAINT fk_orderitems_orders
    FOREIGN KEY (order_num) REFERENCES orders (order_num);
    ```

18. ```
    CREATE VIEW product AS
    SELECT *
    FROM orders;
    DROP VIEW product;
    ```

19. ```
    #存储过程
    CREATE PROCEDURE ordertotal(
    	IN onnumber INT,
    	OUT ototal DECIMAL(8,2)
    )
    BEGIN
    	SELECT Sum(price*quantity)
    	FROM orderitems
    	WHERE order_num = onumber
    	INTO ototal;
    END;

    CALL ordertotal(20004, @total);
    SELECT @total;

    SHOW CREATE PROCEDURE ordertotal;#显示信息
    DROP PROCEDURE ordertotal;
    ```

20. ```
    游标（cursor）是一个存储在MySQL服务器上的数据库查询，
    它不是一条SELECT语句，而是被该语句检索出来的结果集。在存储了游
    标之后，应用程序可以根据需要滚动或浏览其中的数据。

    DECLARE o INT;
    DECLARE ordernumbers CURSOR
    FOR
    SELECT order_num FROM orders;
    OPEN ordernumbers;
    FETCH ordernumbers INTO o;
    CLOSE ordernumbers;
    ```

21. ```
    #触发器
    DELETE/INSERT/UPDATE
    ```

22. ```
    #事务
    START TRANSCTION;
    COMMIT;
    ROLLBACK;
    SAVEPOINT delete1;
    ROLLBACK TO delete1;
    ```

23. ​