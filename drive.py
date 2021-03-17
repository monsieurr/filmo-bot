from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Download client_secrets.json from Google API Console and OAuth2.0 is done in two lines. 
# You can customize behavior of OAuth2 in one settings file settings.yaml
gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)
