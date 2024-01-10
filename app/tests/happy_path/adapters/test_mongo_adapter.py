def test_mongo_adapter_connection(mongo_adapter):
    assert mongo_adapter.check_connection() == True

def test_mongo_adapter_database(mongo_adapter):
    db = mongo_adapter.get_database('purchase_requests')
    assert db.name == 'purchase_requests'

def test_mongo_adapter_collection(mongo_adapter):
    collection_name = 'users'
    collection = mongo_adapter.get_collection('purchase_requests', collection_name)
    assert collection.name == collection_name