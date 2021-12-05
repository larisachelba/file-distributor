from flask import Flask, request
from flask_restful import Resource, Api

from get_filesystem_info import pathto_dict
from size import copy_files, delete_old_directories

app = Flask(__name__)
api = Api(app)


class Home(Resource):
    def get(self):
        return 'Hello World!', 200


class Rules(Resource):
    def post(self):
        rules = request.json
        if rules.get('rules').get('creation_date'):
            date = rules.get('rules').get('creation_date')
            return date, 200

        elif rules.get('rules').get('size'):
            size = rules.get('rules').get('size')
            copy_files(size)
            result = pathto_dict('new_filesystem')
            delete_old_directories()
            return result, 200
        elif rules.get('rules').get('extension'):
            # TODO: sort files by extension
            return "Sorted extension", 200
        else:
            return "Rules not understood", 500


class FileSystem(Resource):
    def get(self):
        result = pathto_dict('filesystem')
        return result, 200


api.add_resource(Home, '/home', '/')
api.add_resource(Rules, '/rules')
api.add_resource(FileSystem, '/file-system')

if __name__ == '__main__':
    app.run(debug=True)
