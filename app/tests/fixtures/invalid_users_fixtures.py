from bson.objectid import ObjectId

INVALID_FIELD_OR_MISSING_REQUIRED_USER_DATA = {
    '_id': ObjectId("61774b56c7091e830d495123"),
    'useame': 'test',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'test'
}

INVALID_TYPE_FIELD_USER_DATA = {
    '_id': ObjectId("61774b56c7091e830d495123"),
    'username': 123,
    'first_name': 'tst',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'test'
}

INVALID_DUPLICATE_USER_DATA = {
    '_id': ObjectId("61774b56c7091e830d495123"),
    'username': 'test',
    'first_name': 'tst',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'test'
}

INVALID_OBJECT_ID_USER_DATA = {
    '_id': 'test123',
    'username': 'test',
    'first_name': 'tst',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'test'
}

INVALID_USER_DATA_NO_EXISTS = {
    '_id': ObjectId("61774b56c7091e830d495798"),
    'username': 'test',
    'first_name': 'tst',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'test'
}

INVALID_FIELD_TO_USER_USE_CASE = {
    '_id': ObjectId("61774b56c7091e830d495123"),
    'useame': 'test',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'test'
}