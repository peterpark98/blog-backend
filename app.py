# app.py

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求

blogs = [
    {"id": 1, "title": "First Blog", "content": "This is the first blog content"},
    {"id": 2, "title": "Second Blog", "content": "This is the second blog content"},
]

@app.route('/api/blogs', methods=['GET'])
def get_blogs():
    return jsonify(blogs)

@app.route('/api/blogs/<int:blog_id>', methods=['GET'])
def get_blog(blog_id):
    blog = next((b for b in blogs if b["id"] == blog_id), None)
    if blog:
        return jsonify(blog)
    else:
        return jsonify({"error": "Blog not found"}), 404

@app.route('/api/blogs', methods=['POST'])
def create_blog():
    new_blog = request.json
    new_blog["id"] = len(blogs) + 1
    blogs.append(new_blog)
    return jsonify(new_blog), 201

@app.route('/api/blogs/<int:blog_id>', methods=['PUT'])
def update_blog(blog_id):
    blog = next((b for b in blogs if b["id"] == blog_id), None)
    if not blog:
        return jsonify({"error": "Blog not found"}), 404
    updated_blog = request.json
    blog.update(updated_blog)
    return jsonify(blog)

@app.route('/api/blogs/<int:blog_id>', methods=['DELETE'])
def delete_blog(blog_id):
    global blogs
    blogs = [b for b in blogs if b["id"] != blog_id]
    return jsonify({"message": "Blog deleted successfully"}), 204

if __name__ == '__main__':
    app.run(debug=True)
