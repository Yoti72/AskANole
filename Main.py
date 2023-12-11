from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import sqlite3
import random

user = ['']


@app.route('/', methods = ['POST', 'GET'])
def index():
    user[0] = ""
    return render_template('LoginScreen.html')


@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    return render_template('SignUp.html')

@app.route('/signupvalid', methods = ['POST', 'GET'])
def signupvalid():
    if request.method == "POST":
        try:
            first = request.form['First']
            last = request.form['Last']
            fsuid = request.form['Fsuid']
            password = request.form['Password']
            confirm_pass = request.form['ConfirmPassword']
            user[0] = fsuid

            con = sqlite3.connect('database.db')

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                if(password == confirm_pass):
                    cur.execute("INSERT INTO Login (FSUID, Password,First,Last) VALUES (?,?,?,?)", (fsuid, password, first, last))
            return redirect("/")
        except:
            con.rollback()
            return render_template('Error.html')
        finally:
            con.close()

@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    if request.method == "POST":
        conn = sqlite3.connect('database.db')
        try:
            fsuid = request.form['FSUID']
            password = request.form['Password']

            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Login WHERE FSUID = ? AND Password = ?", (fsuid,password))
            rows = cursor.fetchall()
            if len(rows) == 0:
                return render_template("NoMatchingUser.html")
            user[0] = rows[0][0]
            return redirect('/main')
        except:
            return redirect("/")
        finally:
            conn.close()

@app.route('/main', methods = ['POST', 'GET'])
def main():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Posts ORDER BY Id DESC")
    posts = cur.fetchall()

    return render_template('MainPage.html', posts=posts)

@app.route('/addpost', methods = ['POST', 'GET'])
def addpost():
    return render_template("AddPost.html")

@app.route('/added', methods = ['POST', 'GET'])
def added():
    if request.method == "POST":
        try:
            title = request.form['Title']
            description = request.form['Description']

            con = sqlite3.connect('database.db')

            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO Posts (FSUID, Title,Description) VALUES (?,?,?)", (user[0], title, description))


        except:
            con.rollback()
            return render_template('Error.html')
        finally:
            con.close()

    return redirect("/main")

@app.route('/post_detail/<int:post_id>')
def post_detail(post_id):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM Posts WHERE Id = ?", (post_id,))
    post = cur.fetchall()

    authorFSUID = post[0][1]
    title = post[0][2]
    description = post[0][3]

    cur.execute("SELECT Author, Content FROM Comments WHERE PostId = ? ORDER BY CommentId ASC", (post_id,))
    comments = cur.fetchall()

    return render_template('PostDetail.html', post_id=post_id, title=title, description=description, fsuid=authorFSUID, comments=comments)

@app.route('/messages', methods = ['POST', 'GET'])
def messages():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT PrimaryUser, SecondaryUser FROM Replies WHERE PrimaryUser = ? OR SecondaryUser = ? ORDER BY Ind DESC", (user[0], user[0]))
    replies = cur.fetchall()


    fsuids = set()
    for reply in replies:
        if reply[0] != user[0]:
            fsuids.add(reply[0])
        else:
            fsuids.add(reply[1])

    query = "SELECT FSUID, First FROM Login WHERE FSUID IN ({})".format(', '.join('?' for _ in fsuids))
    cur.execute(query, tuple(fsuids))

    results = cur.fetchall()

    return render_template("Messages.html", replies=results)

@app.route('/sendmessages', methods = ['POST', 'GET'])
def sendmessages():
    if request.method == 'POST':
        try:
            other_person = request.form["fsuid"]
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()

            cur.execute("SELECT PrimaryUser, Message FROM Replies WHERE (PrimaryUser = ? AND SecondaryUser = ?) OR (PrimaryUser = ? AND SecondaryUser = ?) ORDER BY Ind ASC", (user[0], other_person, other_person, user[0]))
            authors_and_messages = cur.fetchall()

            return render_template("SendMessage.html", authors_and_messages=authors_and_messages, other=other_person)
        except:
            return render_template('Error.html')


@app.route('/send', methods = ['POST','GET'])
def sendMessages():
    if request.method == 'POST':
        try:
            other = request.form["other"]
            message = request.form["message"]
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()
            cur.execute("INSERT INTO Replies (PrimaryUser,SecondaryUser,Message) VALUES (?,?,?)", (user[0], other, message))
            conn.commit()
            cur.execute("SELECT PrimaryUser, Message FROM Replies WHERE (PrimaryUser = ? AND SecondaryUser = ?) OR (PrimaryUser = ? AND SecondaryUser = ?) ORDER BY Ind ASC", (user[0], other, other, user[0]))
            authors_and_messages = cur.fetchall()

            return render_template("SendMessage.html", authors_and_messages=authors_and_messages, other=other)

        except:
            conn.rollback()
            return render_template('Error.html')
        finally:
            conn.close()

@app.route("/search", methods = ["POST", "GET"])
def searched():
    if request.method == "POST":
        try:
            searched = request.form["searched"]
            conn = sqlite3.connect('database.db')
            cur = conn.cursor()

            query = """
                SELECT * FROM Posts
                WHERE FSUID LIKE ? COLLATE NOCASE
                OR Title LIKE ? COLLATE NOCASE
                OR Description LIKE ? COLLATE NOCASE
                ORDER BY Id DESC"""

            cur.execute(query, ('%' + searched + '%', '%' + searched + '%', '%' + searched + '%'))

            posts = cur.fetchall()
            return render_template('MainPage.html', posts=posts)

        except:
            conn.rollback()
            return render_template('Error.html')
        finally:
            conn.close()

@app.route("/comment", methods = ["POST", "GET"])
def comment():
    if request.method == "POST":
        try:
            print(1)
            post_id = request.form["post_id"]
            print(post_id)
            content = request.form["content"]
            print(content)
            conn = sqlite3.connect('database.db')
            print(4)
            cur = conn.cursor()
            print(user[0])
            cur.execute("INSERT INTO Comments (PostId,Content,Author) VALUES (?,?,?)", (post_id, content, user[0]))
            print(6)
            conn.commit()
            return redirect('/post_detail/' + post_id)

        except:
            conn.rollback()
            return render_template('Error.html')
        finally:
            conn.close()


if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.close()
    app.run(debug=True)
