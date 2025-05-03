from flask import Flask, render_template, redirect, url_for, request, session, flash, jsonify
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'app.tony_magabush'
app.permanent_session_lifetime = timedelta(days=5)

# -------------------- Routes --------------------

@app.route('/')
def index():
    return render_template('index.html', active_page='home')

@app.route('/about')
def about():
    return render_template('about.html', active_page='about')

@app.route('/projects')
def projects():
    return render_template('projects.html', active_page='projects')

@app.route('/blog')
def blog():
    return render_template('blog.html', active_page='blog')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html', active_page='testimonials')

@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

@app.route('/skills')
def skills():
    return render_template('skills.html', active_page='skills')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html', active_page='certifications')

@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html', active_page='admin')

@app.route('/toggle-dark-mode', methods=['POST'])
def toggle_dark_mode():
    session['dark_mode'] = not session.get('dark_mode', False)
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
