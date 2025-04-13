'''# create a api using flask

from flask import Flask, request, jsonify

app = Flask(__name__)

# roott - location or some place of api from where we get the data
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
          "user_id": user_id,
          "name": "John doe", # type: ignore
          "email": "anchal@gmail.com"
     }
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200


if __name__ == "__main__":
    app.run(debug=True)
'''