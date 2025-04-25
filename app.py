from flask import Flask, render_template, redirect, url_for, request, session, flash
from datetime import timedelta
from functools import wraps

app = Flask(__name__)
app.secret_key = 'app.tony_magabush'
app.permanent_session_lifetime = timedelta(days=5)

# Updated login credentials
users = {
    'Anthony': '0549070835As'
}

# --- Login Required Decorator for Dashboard ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash("You need to log in to access the dashboard.")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- Routes ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if users.get(username) == password:
            session['user'] = username
            return redirect(url_for('admin_dashboard'))  # Redirect to dashboard after login
        else:
            flash("Invalid username or password")
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))  # Redirect to home after logout

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

# Dashboard route requires login
@app.route('/admin')
@login_required
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/dark-mode', methods=['GET'])
def dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

