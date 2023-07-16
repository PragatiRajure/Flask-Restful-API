from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)

# MongoDB connection setup
client = MongoClient('mongodb://localhost:27017')
db = client['user']
collection = db['users']


class Item(Resource):
    def get(self, item_id=None):
        if item_id:
            item = collection.find_one({'id': int(item_id)})
            print(item)
            if item:
                item['_id'] = str(item['_id'])
                return item, 200
            else:
                return {'message': 'Item not found'}, 404
        else:
            print(item_id)
            items = list(collection.find())
            user_list = []
            if items:
                for user in items:
                    user['_id'] = str(user['_id'])
                    user_list.append(user)
                return user_list, 200
            
    def post(self, item_id=None):
        data = request.get_json()
        result = collection.insert_one(data)
        print('Inserted document ID:', result.inserted_id)
        response = {
            'Inserted document ID': str(result.inserted_id)
        }
        return response

    def put(self, item_id):
        data = request.get_json()
        query = {'id': int(item_id)}
        result = collection.update_one(query, {'$set': data})
        response = {
            'matched_count': result.matched_count,
            'modified_count': result.modified_count
        }
        return response

    def delete(self, item_id):
        result = collection.delete_one({"id": int(item_id)})
        if result.deleted_count == 1:
            response = {'message': 'User deleted successfully'}
        else:
            response = {'message': 'User not found'}
        return response


api.add_resource(Item, '/item', '/item/<string:item_id>')

if __name__ == '__main__':
    app.run(debug=True)
