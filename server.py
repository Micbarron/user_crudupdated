from flask import Flask, render_template, request, redirect, session
from users import User
app = Flask(__name__)
app.secret_key = 'a totally new randomly generated string!!!'

@app.route('/')
def index():
    users = User.get_all_users()
    for user in users:
        print(user.id)
    return render_template('index.html', users = users)

@app.route('/users/create', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return redirect('/')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/user/<int:id>')
def show_user(id):
    data = {'id': id}
    singleuser = User.get_user_by_id(data)
    return render_template('show.html', user = singleuser)

@app.route('/delete/<int:id>')
def delete_user(id):
    data = {'id': id}
    User.delete_user_by_id(data)
    return redirect('/')


@app.route('/update/<id>')
def update_user(id):
    data = {'id': id}
    user = User.get_user_by_id(data)
    
    return render_template('update.html', user = user)
# need to make 2 routes for update?

@app.route('/update/<int:id>/return', methods=['POST'])
def update_return(id):
    data = {
        'id': id,
        'first_name' : request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']


    }
    User.update_user_by_id(data)
    return redirect(f'/user/{id}')



if __name__=='__main__':
    app.run(debug=True)