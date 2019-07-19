from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/flask')
def hello_flask():
  return 'Hello Flask!'

@app.route('/python/')
def hello_python():
  return 'Hello Python!'

@app.route('/hello/<name>')
def hello_name(name):
  return 'Hello %s!' % name

@app.route('/blog/<int:postID>')
def show_blog(postID):
  return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
  return 'Revision Number%f' % revNo

# url_for() is used for dynamically building a URL for a specific function
@app.route('/admin')
def hello_admin():
  return 'Hello Admin!'

@app.route('/guest/<guest>')
def hello_guest(guest):
  return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
  if name == 'admin':
    return redirect(url_for('hello_admin'))
  else:
    return redirect(url_for('hello_guest',guest = name))


if __name__ == '__main__':
  app.run(debug = True)
