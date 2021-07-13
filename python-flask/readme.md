# Flask-Python  目录结构
-   applications（应用目录，多应用时使用蓝图）
-   bin（脚本目录，主要存放shell或者bat脚本）
-   celery_tasks（异步任务目录）
-   configs（配置文件目录）
-   folder （文件存放目录）
-   modules （数据表映射关系类目录）
-   static （静态文件）
-   utils （基础逻辑）
-   app_run.py (flask服务启动脚本)
-   manage.py (数据库迁移脚本，使用前初始化生成migrations目录)
-   start_app.sh (shell启动脚本)

### 本次框架在定义上，是先定义的SQLAlchemy()，再注册flask app实例，故在实例SQLAlchemy()类的基础逻辑中需要有管理上下文的操作
```Python
db.init_app(app)
app.app_context().push()
```

### 选择在configs/setting.py中引入蓝图应用，只是个人选择，也可以独立建立一个配置文件进行管理。

### 从资源访问的角度出发，flask支持直接访问静态资源。如http://0.0.0.0:8282/static/home.html