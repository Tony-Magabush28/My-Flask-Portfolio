from flask import Flask, render_template, redirect, url_for, request, session
from datetime import timedelta

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(days=5)

# Dummy data for login
users = {
    'admin': 'adminpassword'  
}

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if users.get(username) == password:
            session['user'] = username
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials.")
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/admin')
def admin_dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    
    return render_template('admin_dashboard.html')

@app.route('/dark-mode', methods=['GET'])
def dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
