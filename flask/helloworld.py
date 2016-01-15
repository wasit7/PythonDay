from flask import Flask
from flask import request
app = Flask(__name__)
html='''<!DOCTYPE html>
<html>
<body>
<textarea 
  style="width:400px;height:180px">
  {0}
</textarea>
<form action="/chat">
  <input type="text" name="usr" value="{1}">
  <input type="text" name="msg" value="" autofocus>
  <input type="submit" value="Submit">
</form> 

</body>
</html>'''
text=""
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/chat')
def user():
	global text
	usr=request.args.get('usr', 'Anonymous')
	if not usr:
		usr='Anonymous'
	msg=request.args.get('msg', '')
	text=text+'''{0}: {1}\n'''.format(usr,msg)
	return html.format(text,usr)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000,debug=True)