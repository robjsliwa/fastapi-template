from abc import ABC, abstractmethod
import mysql.connector
import logging
logger = logging.getLogger(__name__)

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
            password='pass123',
            host='db',
            database='my_project'
        )
        # Check if the string_table exists in the my_project database


    def get(self, id: int):
        cursor = self.conn.cursor(dictionary=True)
        query = "SELECT * FROM string_table WHERE id = %s"
        cursor.execute(query, (id,))
        return cursor.fetchone()

    def create(self, data: dict):
        cursor = self.conn.cursor()
        logger.info("Creating string: %s", data)
        query = "INSERT INTO string_table (string_text, description) VALUES (%s, %s)"
        try:
            cursor.execute(query, (data["string_text"], data["description"]))
            self.conn.commit()
            return cursor.lastrowid
        except mysql.connector.Error as err:
            print("Error while inserting data: {}".format(err))
            return err

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

