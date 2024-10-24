from flask import Flask, redirect, request, render_template
import markdown
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

load_dotenv()

app = Flask(__name__)

BLOG_DIR = 'blog'

@app.route('/')
def home():
    return redirect("/blog", code=302)

@app.route('/blog')
def blog():
    # List Markdown files in the blog directory
    posts = []
    for filename in os.listdir(BLOG_DIR):
        if filename.endswith('.md'):
            post_path = os.path.join(BLOG_DIR, filename)
            with open(post_path, 'r') as f:
                title = f.readline().strip('# ').strip()    # Get the title from the first line
                posts.append({'filename': filename, 'title': title})
    test_var = "hello"
    return render_template('blog.html', posts = posts)

@app.route('/blog/<filename>')
def blog_post(filename):
    post_path = os.path.join(BLOG_DIR, filename)
    if os.path.exists(post_path):
        with open(post_path, 'r') as f:
            title = f.readline().strip('# ').strip()  # Get the title from the first line
            content = f.read()
            html_content = markdown.markdown(content)  # Convert Markdown to HTML
            return render_template('post.html', post={'title': title, 'content': html_content})
    else:
        return "Post not found", 404
    
@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Set up your email details
    to_email = os.getenv('EMAIL_USER')
    subject = 'New Contact Form Submission'
    
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    
    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as server:
            server.starttls()
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))  # Use email from env
            server.sendmail(email, to_email, msg.as_string())
        return "Thank you for your message!"
    except Exception as e:
        return f"There was a problem sending your message: {str(e)}"
    
if __name__ == '__main__':
    app.run(debug=True)
