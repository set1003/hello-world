import os
with open('index.html', 'r') as f:
    content = f.read()
replacements = {
    '__FIREBASE_API_KEY__': os.environ['FIREBASE_API_KEY'].strip(),
    '__FIREBASE_AUTH_DOMAIN__': os.environ['FIREBASE_AUTH_DOMAIN'].strip(),
    '__FIREBASE_PROJECT_ID__': os.environ['FIREBASE_PROJECT_ID'].strip(),
    '__FIREBASE_STORAGE_BUCKET__': os.environ['FIREBASE_STORAGE_BUCKET'].strip(),
    '__FIREBASE_MESSAGING_SENDER_ID__': os.environ['FIREBASE_MESSAGING_SENDER_ID'].strip(),
    '__FIREBASE_APP_ID__': os.environ['FIREBASE_APP_ID'].strip(),
}
for placeholder, value in replacements.items():
    content = content.replace(placeholder, value)
with open('index.html', 'w') as f:
    f.write(content)
