import requests

r = requests.get('https://id.atlassian.com/manage-profile/profile-and-visibility', auth=('user',
                                                                                         'pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()
