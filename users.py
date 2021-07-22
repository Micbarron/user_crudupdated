from mysqlconnection import connectToMySQL

class User():
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('user_schema').query_db(query)

        users = []

        for item in results:
            users.append(User(item))

        return users


    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s)"

        return connectToMySQL('user_schema').query_db(query, data)


    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        results = connectToMySQL('user_schema').query_db(query, data)

        shitsngiggles = cls(results[0])

        return shitsngiggles
    
    @classmethod
    def delete_user_by_id(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s;"

        results = connectToMySQL('user_schema').query_db(query, data)

        
    @classmethod
    def update_user_by_id(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"

        return connectToMySQL('user_schema').query_db(query, data)



        