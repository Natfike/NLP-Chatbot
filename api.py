from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource, fields
from bagOfWord import BagOfWord

app = Flask(__name__)
CORS(app)

api = Api(app, version="0.1", title="ChatBot", description="Documentation pour l'API des chatbots",
          default="Chatbot", default_label="All endpoint for the api", doc="/api/docs")
# Models
first_model = api.model('Case', {
    'this is a field': fields.String(description="Enter a parameter", exemple='')
})

bagOfWordModel = BagOfWord()

@api.route("/askBOWChatbot")
class askBOWChatbot(Resource):
    @api.doc(description="Ask a prediction to the BagOfWord Chatbot")
    @api.expect(first_model)
    @api.response(200, 'Success')
    def post(self):
        print('bonsoir')
        data = request.get_json()
        print(data["input"])
        intents = bagOfWordModel.pred_class(data["input"])
        return bagOfWordModel.get_response(intents)

if __name__ == '__main__':
    app.run(host='localhost', port=5010)