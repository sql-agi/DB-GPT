import pymysql.cursors
from typing import Dict, Any, List, Optional


class DBManager:

    def __init__(self):
        self.connection = pymysql.connect(
            host='mysql',
            user='root',
            password='ls1234qwer',
            database='db_gpt',
            cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()
        self._initialize_database()

    def _initialize_database(self):
        # # 创建数据库
        # self.execute_query('CREATE DATABASE IF NOT EXISTS db_nlp')
        # # 切换到新创建的数据库
        # self.connection.select_db('db_nlp')
        self.execute_query('''
            CREATE TABLE IF NOT EXISTS `chat_session` (
              `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '会话的唯一标识',
              `user_id` BIGINT UNSIGNED NOT NULL DEFAULT 0 COMMENT '用户的唯一id',
              `user_name` VARCHAR(128) NOT NULL DEFAULT '' COMMENT '创建人',
              `database_id` BIGINT UNSIGNED NOT NULL COMMENT '数据库的唯一id',
              `model` VARCHAR(64) NOT NULL DEFAULT '' COMMENT '大模型名称',
              `title` VARCHAR(64) NOT NULL  COMMENT '会话的标题',
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
              `database_id` BIGINT UNSIGNED NOT NULL COMMENT '数据库的唯一id',
              `model` VARCHAR(64) NOT NULL DEFAULT '' COMMENT '大模型名称',
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
        """Executes a SQL query and commits the transaction."""
        affected_rows = self.cursor.execute(query, params)
        self.connection.commit()
        return affected_rows

    # def fetch_query(self, query, params=()):
    #     self.cursor.execute(query, params)
    #     results = self.cursor.fetchall()
    #     return_list = []
    #     for d in results:
    #         return_list.append(tuple(d.values()))
    #     return return_list
    def fetch_query(self, query, params=()):
        """Executes a SQL query and returns all results as a list of dictionaries."""
        self.cursor.execute(query, params)
        results = self.cursor.fetchall()
        return results

    def fetch_one(self, query, params=()):
        """Executes a SQL query and returns the first result as a dictionary, or None if no result."""
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    # 增加数据库连接
    def save_database(self, data: Dict[str, Any]) -> int:
        """Inserts a new database connection and returns the new record's ID."""
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
        """Logically deletes a database connection by setting its is_del flag to 1."""
        query = "UPDATE database_connections SET is_del = 1 WHERE id = %s"
        affected_rows = self.execute_query(query, (connection_id,))
        return affected_rows > 0

    # 更新数据库连接
    def update_database(self, connection_id: int, data: Dict[str, Any]) -> int:
        """Updates a database connection and returns the connection's ID."""
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

    def get_all_databases(self) -> List[Dict[str, Any]]:
        """Retrieves all database connections that are not logically deleted."""
        query = "SELECT id, database_type, database_name, remark FROM database_connections WHERE is_del = 0"
        return self.fetch_query(query)

    def get_database_by_id(self, connection_id: int) -> Dict[str, Any]:
        """Retrieves a single database connection by its ID."""
        query = "SELECT id, database_type, database_name, username, password,address, port, remark FROM database_connections WHERE id = %s"
        return self.fetch_one(query, (connection_id,))

    def get_database_by_name(self, database_name: str) -> bool:
        """Checks if a database with the given name exists and returns True if more than one record found."""
        query = """
        SELECT COUNT(*) as count
        FROM database_connections
        WHERE database_name = %s
        """
        result = self.fetch_one(query, (database_name,))
        return result['count'] > 1

    def insert_chat_session(self, database_id: int, model: str, title: str) -> int:
        """Inserts a new chat session and returns the session's ID."""
        query = """
        INSERT INTO chat_session (database_id,model,title)
        VALUES (%s, %s, %s)
        """
        params = (database_id, model, title)
        self.execute_query(query, params)
        return self.cursor.lastrowid

    def fetch_database_id_and_model(self, session_id: int) -> Optional[Dict[str, Any]]:
        """Fetches the database_id and model for a given session ID."""
        query = """
        SELECT database_id, model
        FROM chat_session
        WHERE id = %s
        """
        params = (session_id,)
        self.execute_query(query, params)
        result = self.cursor.fetchone()
        if result:
            return result
        return None
    def check_session_exists_by_id(self, session_id: int) -> bool:
        """Checks if a chat session exists by its ID and is not deleted."""
        query = """
        SELECT COUNT(*) as count
        FROM chat_session
        WHERE id = %s AND is_del = 0
        """
        result = self.fetch_one(query, (session_id,))
        return result['count'] > 0

    def get_chat_session_by_user_id(self, user_id: int = None) -> List[Dict[str, Any]]:
        """
        Retrieve chat sessions by user ID. If no user ID is provided, retrieve all active sessions.
        :param user_id: Optional; The ID of the user whose sessions are to be retrieved.
        :return: A list of dictionaries, each representing a chat session.
        """
        # 基础查询语句，只选取需要的字段，并仅包括未删除的会话
        query = """
        SELECT id, user_id, user_name, title
        FROM chat_session
        WHERE is_del = 0
        """
        params = []

        # 如果提供了 user_id，则添加特定的条件
        if user_id is not None:
            query += " AND user_id = %s"
            params.append(user_id)

        return self.fetch_query(query, tuple(params))

    def insert_chat_history(self, session_id: int, database_id: int, model: str, message_type: str,
                            message_content: str) -> int:
        """
        Insert a new chat history record.
        :param session_id: The session ID to which the chat history belongs.
        :param database_id: The database ID associated with the chat history.
        :param model: The name of the model associated with the chat history.
        :param message_type: The type of message (e.g., user or system).
        :param message_content: The content of the message.
        :return: The ID of the newly created chat history record.
        """

        query = """
        INSERT INTO chat_history (session_id, database_id, model, message_type, message_content)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (session_id, database_id, model, message_type, message_content)
        self.execute_query(query, params)
        return self.cursor.lastrowid

    def get_chat_history_by_session_id(self, session_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve chat history records for a given session ID.
        :param session_id: The session ID for which chat history is to be retrieved.
        :return: A list of dictionaries, each representing a chat history record.
        """
        query = """
        SELECT session_id, message_type, message_content
        FROM chat_history
        WHERE session_id = %s AND is_del = 0
        """
        params = (session_id,)
        return self.fetch_query(query, params)

    def delete_chat_session_by_id(self, session_id: int) -> bool:
        """
        Logically delete a chat session by marking it as deleted.
        :param session_id: The ID of the session to delete.
        :return: True if the operation was successful.
        """
        query = """
        UPDATE chat_session
        SET is_del = 1
        WHERE id = %s
        """
        params = (session_id,)
        affected_rows = self.execute_query(query, params)
        return affected_rows > 0

    def delete_chat_history_by_session_id(self, session_id: int) -> bool:
        """
        Logically delete all chat history records associated with a specific session ID.
        :param session_id: The session ID whose chat histories are to be deleted.
        :return: True if the operation was successful.
        """
        query = """
        UPDATE chat_history
        SET is_del = 1
        WHERE session_id = %s
        """
        params = (session_id,)
        affected_rows = self.execute_query(query, params)
        return affected_rows > 0
