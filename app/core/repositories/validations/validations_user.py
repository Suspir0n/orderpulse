from bson.objectid import ObjectId

def fields_required(user_data):
    required_fields = ['username', 'email', 'password']

    for field in required_fields:
        if field not in user_data:
            raise ValueError(f"The required field '{field}' is missing from the user data.")

def type_fields_valid(user_data):
    all_fields = ['username', 'first_name', 'last_name', 'email', 'password']

    for field in all_fields:
        if not isinstance(user_data[field], str):
            raise TypeError("All fields must be strings.")

def has_user_in_db(is_existing_user):
    if is_existing_user:
        raise ValueError("There is already a user with this email.")

def has_user_id_valid(_id):
    if not ObjectId.is_valid(_id):
        raise ValueError("Invalid user ID.")