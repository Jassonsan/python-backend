from flask import Flask, request
from flask_restful import Resource, Api
from model.maindb import selectChatByIdI


# Instantiate the app
app = Flask(__name__)
api = Api(app)
        
class Chat(Resource):
	def get(self, chatId):
		try:
			response = selectChatByIdI(chatId)
			if response:
				return {"chatId": chatId}, 200
			else:
				return {}, 404
		except:
			return {"error": "internal error, verify input params."}, 500

# Create routes
api.add_resource(Chat, '/chat/<int:chatId>')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
