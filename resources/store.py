from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return{'message': 'Store not found'}, 404


    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists.".format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()

        except:
            return {"message": "An error occured while creating the store."}, 500

        return store.json(), 201


    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


    #
    # def put(self, name):
    #
    #     data = Item.parser.parse_args()
    #
    #     item = ItemModel.find_by_name(name)
    #
    #     if item is None:
    #         item = ItemModel(name, **data)
    #     else:
    #         item.price = data['price']
    #
    #     item.save_to_db()
    #
    #     return item.json()


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
