# -*- coding: utf-8 -*-
from application import app, manager
from flask_script import Server
import www
from jobs.launcher import runJob

# 应用flask_script对manager对象进行封装，用manager代替app运行服务。
# web server
manager.add_command("runserver", Server(host='0.0.0.0', port=app.config['SERVER_PORT'], use_debugger=True, use_reloader=True))

# job entrance
manager.add_command('runjob', runJob())


# 封装run函数的数据库环境和启动
def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()
