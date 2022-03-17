from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

db = 'login_and_reg_schema'
class User:
    
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def register_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        print(connectToMySQL(db).query_db(query, data), "%"*60)
        return connectToMySQL(db).query_db(query, data)

    
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        if len(results) > 0 :
            return cls(results[0])
        return False
    
    
    
    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash('First Name must be more than a single character.', "error")
            is_valid = False
        if len(user['last_name']) < 2:
            flash('Last Name must be more than a single character.', "error")
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must be more than 7 characters long.', "error")
            is_valid = False
        if user['confirm_password'] != user['password']:
            flash('Password must match', "error")
            is_valid = False
        return is_valid
    
        
    
    
    
    
           
        
        