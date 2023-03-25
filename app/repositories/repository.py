from abc import ABC, abstractmethod
import mysql.connector


class Repository(ABC):
    """
    Abstract class defining the interface for a database repository
    """

    @abstractmethod
    def get(self, id: str):
        pass

    @abstractmethod
    def create(self, data: dict):
        pass

    @abstractmethod
    def update(self, id: str, data: dict):
        pass

    @abstractmethod
    def delete(self, id: str):
        pass


class MySqlRepository(Repository):
    """
    Concrete class implementing the Repository interface for MySQL database
    """

    def __init__(self):
        self.conn = mysql.connector.connect(
            user='root',
            password='admin123',
            host='db',
            database='pass123'
        )

    def get(self, id: int):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM string_table WHERE id=%s"
        cursor.execute(query, (id,))
        return cursor.fetchone()

    def create(self, data: dict):
        cursor = self.conn.cursor()
        query = "INSERT INTO string_table (string_text, description) VALUES (%s, %s)"
        cursor.execute(query, (data["string_text"], data["description"]))
        self.conn.commit()
        return cursor.lastrowid

    def update(self, id: int, data: dict):
        cursor = self.conn.cursor()
        query = "UPDATE string_table SET string_text=%s, description=%s WHERE id=%s"
        cursor.execute(query, (data["string_text"], data["description"], id))
        self.conn.commit()

    def delete(self, id: int):
        cursor = self.conn.cursor()
        query = "DELETE FROM string_table WHERE id=%s"
        cursor.execute(query, (id,))
        self.conn.commit()

