### 配置工具启动说明

1.  到 github 克隆程序源码
``` bash
cd /usr/dynas/
git clone --depth=1 https://github.com/yuanyaru/deploy-configTool.git
```
2. 安装 pip 工具 
``` bash
cd /usr/dynas/deploy-configTool/configTool
python get-pip.py
```
3. 根据实际情况修改 监控界面 和 ice接口 对应的 IP、port
``` bash
cd /usr/dynas/deploy-configTool
vim Makefile.inc
```
4. 启动程序
``` bash
cd /usr/dynas/deploy-configTool
make
```
稍等片刻，看到程序成功启动，Ctrl+c关闭即可。

5. 验证
``` bash
[root@localhost deploy-configTool]# docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
48279a1aa533        configtool          "python /code/tool/c…"   10 minutes ago      Up 9 minutes        0.0.0.0:5000->5000/tcp              configtool
```
看到容器启动，则完成配置工具的部署。通过浏览器访问：ip:5000 进入配置页面。