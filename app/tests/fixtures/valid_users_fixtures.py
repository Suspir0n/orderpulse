from bson.objectid import ObjectId

USERS_DATA = [
    {
        '_id': ObjectId("61774b56c7091e830d495120"),
        'username': 'test_01',
        'first_name': 't01',
        'last_name': 'testing',
        'email': 'test_01@example.com',
        'password': 'test01'
    },
    {
        '_id': ObjectId("61774b56c7091e830d495121"),
        'username': 'test_02',
        'first_name': 't02',
        'last_name': 'testing',
        'email': 'test_02@example.com',
        'password': 'test02'
    },
    {
        '_id': ObjectId("61774b56c7091e830d495122"),
        'username': 'test_03',
        'first_name': 't03',
        'last_name': 'testing',
        'email': 'test_03@example.com',
        'password': 'test03'
    }
]

USER_DATA = {
    '_id': ObjectId("61774b56c7091e830d495123"),
    'username': 'test',
    'first_name': 'tst',
    'last_name': 'testing',
    'email': 'test@example.com',
    'password': 'test'
}