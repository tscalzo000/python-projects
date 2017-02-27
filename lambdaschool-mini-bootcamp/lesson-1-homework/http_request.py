import requests

submit = {'name': 'Tori', 'lastname': 'Scalzo', 'email': 'vscalzo000@gmail.com', 'message': 'Testing out the extra credit portion of Lesson 1.'}

r = requests.post('https://lambdaschool.com/contact-form', json=submit)

print(r.text)
