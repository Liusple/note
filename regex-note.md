1. ```regex
   import re
   result = re.match(正则表达式, 要匹配的字符串)#匹配返回match object, 不匹配返回None
   result.group() #返回字符串的匹配部分
   ```

2. ```
   .   匹配任意1字符（除了\n）
   []  匹配[]中列举的字符
   \d  匹配数字
   \D  匹配非数字
   \s  匹配空白，即空格，tab，换行
   \S  匹配非空白
   \w  匹配单词字符
   \W  匹配非单词字符
   ```

3. ```
   * 任意个数
   + 至少一个
   ? 0个或1个
   ```

4. ```
   r'\\nabc' --> '\\\\nabc'
   ```

5. ```
   #匹配变量名
   re.match("[a-zA-Z_]+[\w_]*", "_name")
   #匹配0~99
   re.match("[1-9]?[0-9]", "33")
   ```

6. ```
   \b 匹配一个单词边界
   \B 匹配非单词边界
   ve\b -->ve结尾
   \Bve\B -->ve左右都要出现字符
   ```

7. ```
   #分组
   |            
   (ab)         将括号中的字符做为一个分组
   \num         引用分组num匹配到的字符串
   (?P<name>)   分组起别名
   (?P=name)    引用别名为name分组匹配到的字符串

   re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<h1>hello</h1>")
   re.match(r"<([a-zA-Z]*)>"\w*</\1>, "<h1>hello</h1>")

   re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", "")
   ```

8. ```
   re.search(r"\d+", "There are 4 apples.")
   re.findall(r"\d+", "1 apple, 2 pears, 3 oranges")
   re.sub(r"\d+", "100", "1 apple, 2 pears, 3 oranges")

   #函数
   def add(temp):
   	strnum = temp.group()
   	num = int(strnum) + 1
   	return str(num)
   ret = re.sub(r"\d+", add, "python=100")

   re.split(r":| ", "info:apple pear") #按|和空格进行分割


   ```

9. ```
   非贪婪操作符“？”，这个操作符可以⽤在"*","+","?"的后面要求正则匹配的越少越好。
   >>>	re.match(r"aa(\d+)","aa2343ddd").group(1)
   '2343'
   >>>	re.match(r"aa(\d+?)","aa2343ddd").group(1)
   '2'
   >>>	re.match(r"aa(\d+)ddd","aa2343ddd").group(1)
   '2343'
   >>>	re.match(r"aa(\d+?)ddd","aa2343ddd").group(1)
   '2343'
   ```

10. ​