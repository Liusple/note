2017.10.14

```
1.Virtualenvwrapper
1)pip install virtualenvwrapper
2)创建目录用来存放虚拟环境
mkdir $HOME/.virtualenvs
3)在~/.bashrc中添加行： export WORKON_HOME=$HOME/.virtualenvs
4)在~/.bashrc中添加行：source /usr/local/bin/virtualenvwrapper.sh
5)运行： source ~/.bashrc
workon：列出虚拟环境列表
mkvirtualenv [虚拟环境名]
workon [虚拟环境名]
rmvirtualenv [虚拟环境名]
deactivate

2.pip pip3
sys.path
给python2安装包：pip install
给python3安装包：pip3 install

3.创建用户添加管理员权限
1)useradd -d /home/laowang -m laowang
passwd laowang  
2)修改用户使用的shell类型/etc/passwd
alex:x:1002:1002::/home/alex:/bin/bash
3)添加管理员权限
/etc/sudoers
# User privilege specification
root ALL=(ALL) ALL
alex ALL=(ALL) ALL

4.ngnix安装，配置
1)http://www.cnblogs.com/badboyf/p/6422547.html
2)sudo apt-get install nginx
3)nginx配置文件/etc/nginx/nginx.conf
4)sudo nginx -c /etc/nginx/nginx.conf 指定配置文件
5)停止sudo nginx -s stop  killall -9 nginx

5.sudo出现unable to resolve host问题
修改/ext/hosts
127.0.0.1       localhost name  #要保证这个名字与 /etc/hostname中的主机名一

6.阿里云无法登陆问题
安全组需要添加规则打开80端口

7.vim
sudo apt-get install vim
只对各个用户在自己的当前目录下的.vimrc修改的话，修改内容只对本用户有效,要想全部有效，可以修改/etc/vim/vimrc.

8.ssh 
sudo apt-get install openssh-server
```

