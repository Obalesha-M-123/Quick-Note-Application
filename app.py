from flask import Flask, render_template, request, redirect, url_for
from database import create_table, add_note, get_notes, delete_note

app = Flask(__name__)

# Create database table
create_table()


@app.route("/")
def home():
    notes = get_notes()
    return render_template("index.html", notes=notes)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    content = request.form.get("content", "").strip()

    if title and content:
        add_note(title, content)

    return redirect(url_for("home"))


@app.route("/delete/<int:note_id>", methods=["POST"])
def delete(note_id):
    delete_note(note_id)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)