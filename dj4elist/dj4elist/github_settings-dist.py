
# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App - Give it a name

# If you are running on localhost, make the callback url be
# http://127.0.0.1:8000/oauth/complete/github/

# If you are on the real internet (or using ngrok) make the callback url be
# https://samples.dj4e.com/oauth/complete/github/

# Then copy the client_key and secret to this file

SOCIAL_AUTH_GITHUB_KEY = '224642424242424230ee'
SOCIAL_AUTH_GITHUB_SECRET = 'f1afce7ffa5424242424242424242412af40ec57'
