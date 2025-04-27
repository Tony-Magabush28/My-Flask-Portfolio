from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from datetime import timedelta
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'app.tony_magabush'
app.permanent_session_lifetime = timedelta(days=5)

users = {
    'Anthony': generate_password_hash('0549070835As')
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash("You need to log in first.")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# -------------------- Routes --------------------

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users and check_password_hash(users[username], password):
            session['user'] = username
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))
    
    return render_template('login.html', active_page='login')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html', active_page='home')

@app.route('/about')
@login_required
def about():
    return render_template('about.html', active_page='about')

@app.route('/projects')
@login_required
def projects():
    return render_template('projects.html', active_page='projects')

@app.route('/blog')
@login_required
def blog():
    return render_template('blog.html', active_page='blog')

@app.route('/testimonials')
@login_required
def testimonials():
    return render_template('testimonials.html', active_page='testimonials')

@app.route('/contact')
@login_required
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/skills')
@login_required
def skills():
    return render_template('skills.html', active_page='skills')

@app.route('/certifications')
@login_required
def certifications():
    return render_template('certifications.html', active_page='certifications')

@app.route('/admin')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html', active_page='admin')

@app.route('/toggle-dark-mode', methods=['POST'])
def toggle_dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
