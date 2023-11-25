from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    new_user = User(username=data['username'], email=data['email'])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
