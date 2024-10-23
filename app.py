from flask import Flask, request, render_template
import smtplib
import markdown
from email.mime.text import MIMEText
import os

app = Flask(__name__)

BLOG_DIR = 'blog'

@app.route('/')
def home():
    return render_template('contact.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Set up your email details
    to_email = 'your-email@example.com'  # Replace with your email
    subject = 'New Contact Form Submission'
    
    body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    
    # Create the email
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to_email

    # Send the email
    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:  # Replace with your SMTP server
            server.starttls()
            server.login('your-email@example.com', 'your-email-password')  # Use app password if using Gmail
            server.sendmail(email, to_email, msg.as_string())
        return "Thank you for your message!"
    except Exception as e:
        return f"There was a problem sending your message: {str(e)}"

@app.route('/blog')
def blog():
    # List Markdown files in the blog directory
    posts = []
    for filename in os.listdir(BLOG_DIR):
        if filename.endswith('.md'):
            post_path = os.path.join(BLOG_DIR, filename)
            with open(post_path, 'r') as f:
                title = f.readline().strip('# ').strip()  # Get the title from the first line
                posts.append({'filename': filename, 'title': title})
    return render_template('blog.html', posts=posts)

@app.route('/blog/<filename>')
def blog_post(filename):
    post_path = os.path.join(BLOG_DIR, filename)
    if os.path.exists(post_path):
        with open(post_path, 'r') as f:
            content = f.read()
            html_content = markdown.markdown(content)  # Convert Markdown to HTML
            return render_template('post.html', post={'title': filename[:-3], 'content': html_content})
    else:
        return "Post not found", 404
    
if __name__ == '__main__':
    app.run(debug=True)
