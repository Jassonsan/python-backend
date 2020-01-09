from flask import Flask, request
from flask_restful import Resource, Api
from model.maindb import selectChatByIdI


# Instantiate the app
app = Flask(__name__)
api = Api(app)
        
class Chat(Resource):
    def post(self):
        try:
            print(request)
            data = request.get_json()
            print(data)
            response = selectChatByIdI(data['chatId'])
            return {"data": response}, 200
        except:
            return {"error": "internal error, verify input params"}, 500

# Create routes
api.add_resource(Chat, '/chat')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)