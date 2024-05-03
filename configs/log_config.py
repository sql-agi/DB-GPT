import logging
import os
from logging.handlers import RotatingFileHandler
from datetime import datetime
import pytz  # 引入 pytz 库


LOG_FORMAT = "%(levelname) -5s %(asctime)s" "-1d: %(message)s"
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logging.basicConfig(format=LOG_FORMAT)

# 清除已有的处理器
logger.handlers.clear()

# 设置时区为东八区
tz = pytz.timezone('Asia/Shanghai')
os.environ['TZ'] = 'Asia/Shanghai'

# 强制刷新时区设置
datetime.now().astimezone(tz)

# 获取当前日期，并将其格式化为字符串
current_date = datetime.now(tz).strftime("%Y-%m-%d")

# 创建日志文件夹
log_folder = os.path.dirname(os.getcwd()) + "/logs"
# if os.getenv("ENV") != "dev":
#     log_folder = "/apps/logs"
os.makedirs(log_folder, exist_ok=True)

# 创建一个 RotatingFileHandler 实例，指定日志文件路径、模式（追加或覆盖）和文件大小阈值
file_handler = RotatingFileHandler(os.path.join(log_folder, f"logfile_{current_date}.log"), mode='a',
                                   maxBytes=1024 * 1024 * 500, backupCount=5)

# 设置文件处理器的格式
formatter = logging.Formatter(LOG_FORMAT)
file_handler.setFormatter(formatter)

# 将文件处理器添加到日志记录器
logger.addHandler(file_handler)

# 输出到控制台
to_console = logging.StreamHandler()
to_console.setFormatter(formatter)
logger.addHandler(to_console)

if __name__ == '__main__':
    import os

    project_root = os.path.dirname(os.getcwd())
    print("当前路径为：%s" % project_root)
