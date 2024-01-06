"""
Develop a RESTful API that allows users to create, read, update, and delete resources using Python and Flask.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for example
resources = [
    {"id": 1, "name": "Resource 1"},
    {"id": 2, "name": "Resource 2"},
    {"id": 3, "name": "Resource 3"}
]

# GET request to fetch all resources
@app.route('/resources', methods=['GET'])
def get_resources():
    return jsonify(resources)

# GET request to fetch a specific resource
@app.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = next((res for res in resources if res["id"] == resource_id), None)
    if resource:
        return jsonify(resource)
    else:
        return jsonify({"error": "Resource not found"}), 404

# POST request to create a new resource
@app.route('/resources', methods=['POST'])
def create_resource():
    new_resource = {"id": request.json["id"], "name": request.json["name"]}
    resources.append(new_resource)
    return jsonify(new_resource), 201

# PUT request to update an existing resource
@app.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    resource = next((res for res in resources if res["id"] == resource_id), None)
    if resource:
        resource["name"] = request.json["name"]
        return jsonify(resource)
    else:
        return jsonify({"error": "Resource not found"}), 404

# DELETE request to delete a resource
@app.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    resource = next((res for res in resources if res["id"] == resource_id), None)
    if resource:
        resources.remove(resource)
        return jsonify({"message": "Resource deleted"})
    else:
        return jsonify({"error": "Resource not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run()