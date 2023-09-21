from flask import Flask, render_template
from app.repo.create_tables import create_tables_if_not_exist
from app import app
app = Flask(__name__)
# Creating list of tables if they don't exist
create_tables_if_not_exist()
if __name__ == '__main__':
    app.run(debug=True)

