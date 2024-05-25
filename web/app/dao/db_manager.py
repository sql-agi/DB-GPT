import pymysql.cursors
from typing import Dict, Any, List


class DBManager:

    def __init__(self):
        self.connection = pymysql.connect(host='mysql',
                                          user='root',
                                          password='jiayuan',
                                          database='db-gpt',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS `chat_sessions` (
              `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '会话的唯一标识',
              `user_id` BIGINT UNSIGNED NOT NULL COMMENT '用户的唯一id',
              `user_name` VARCHAR(128) NOT NULL DEFAULT '' COMMENT '创建人',
              `is_del` TINYINT DEFAULT '0' COMMENT '删除标志（0：未删除，1：已删除）',
              `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
              `updated_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
            PRIMARY KEY (`id`) USING BTREE
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='会话表';
        ''')
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS `chat_history` (
              `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '记录的唯一标识',
              `session_id` BIGINT UNSIGNED NOT NULL COMMENT '会话的唯一标识',
              `message_type` VARCHAR(64) NOT NULL COMMENT '消息类型，代表用户或大模型类型',
              `message_content` TEXT NOT NULL COMMENT '会话中的消息内容',
              `is_del` TINYINT DEFAULT '0' COMMENT '删除标志（0：未删除，1：已删除）',
              `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
              `updated_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
               PRIMARY KEY (`id`) USING BTREE
             ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='聊天历史表';
        ''')
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS `database_connections` (
              `id` INT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '记录的唯一标识',
              `database_type` VARCHAR(50) NOT NULL COMMENT '数据库类型',
               `database_name` VARCHAR(128) NOT NULL COMMENT '数据库名',
               `username` VARCHAR(128) NOT NULL COMMENT '用户名',
               `password` VARCHAR(128) NOT NULL COMMENT '密码',
               `address` VARCHAR(256) NOT NULL COMMENT '地址',
               `port` INT UNSIGNED NOT NULL COMMENT '端口',
               `remark` TEXT COMMENT '备注',
               `is_del` TINYINT DEFAULT '0' COMMENT '删除标志（0表示未删除，1表示已删除）',
               `created_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
               `updated_time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
            PRIMARY KEY (`id`) USING BTREE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='数据库连接信息表'; 
        ''')

    def execute_query(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    # def fetch_query(self, query, params=()):
    #     self.cursor.execute(query, params)
    #     results = self.cursor.fetchall()
    #     return_list = []
    #     for d in results:
    #         return_list.append(tuple(d.values()))
    #     return return_list
    def fetch_query(self, query, params=()):
        self.cursor.execute(query, params)
        results = self.cursor.fetchall()
        return results

    def fetch_one(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

# 增加数据库连接
    def save_database(self, data: Dict[str, Any]):
        query = """
        INSERT INTO database_connections (database_type, database_name, username, password, address, port, remark)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data['database_type'], data['database_name'], data['username'], data['password'],
            data['address'], data['port'], data.get('remark')
        )
        self.execute_query(query, params)
        return self.cursor.lastrowid

    # 删除数据库连接
    def delete_database(self, connection_id: int) -> bool:
        query = "UPDATE database_connections SET is_del = 1 WHERE id = %s"
        self.execute_query(query, (connection_id,))
        return True

    # 更新数据库连接
    def update_database(self, connection_id: int, data: Dict[str, Any]) -> int:
        query = """
        UPDATE database_connections SET database_type = %s, database_name = %s, username = %s, password = %s,
        address = %s, port = %s, remark = %s
        WHERE id = %s
        """
        params = (
            data['database_type'], data['database_name'], data['username'], data['password'],
            data['address'], data['port'], data.get('remark'), connection_id
        )
        self.execute_query(query, params)
        return connection_id

    # 查询所有数据库连接
    def get_all_databases(self) -> List[Dict[str, Any]]:
        query = "SELECT id, database_type, database_name, remark FROM database_connections WHERE is_del = 0"
        return self.fetch_query(query)

    # 查询特定ID的数据库连接
    def get_database_by_id(self, connection_id: int) -> Dict[str, Any]:
        query = "SELECT id, database_type, database_name, username, address, port, remark FROM database_connections WHERE id = %s"
        return self.fetch_one(query, (connection_id,))

    # 根据database_name判断是否重复
    def get_database_by_name(self, database_name: str) -> bool:
        query = """
        SELECT COUNT(*) as count
        FROM database_connections
        WHERE database_name = %s
        """
        result = self.fetch_one(query, (database_name,))
        return result['count'] > 1

