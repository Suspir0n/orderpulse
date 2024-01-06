def valid_users(user_data):
    all_fields = ['username', 'first_name', 'last_name', 'email', 'password']
    required_fields = ['username', 'email', 'password']

    for field in required_fields:
        if field not in user_data:
            raise ValueError(f"The required field '{field}' is missing from the user data.")

    for field in all_fields:
        if not isinstance(user_data[field], str):
            raise TypeError("All fields must be strings.")