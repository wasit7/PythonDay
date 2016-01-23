from flask import Flask
from flask import request
app = Flask(__name__)
html='''<!DOCTYPE html><html>
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
<script>
$(document).ready(function() {
    setInterval("ajaxd()",1000);
});
function ajaxd() { 
  	$.ajax({
   		type: "GET",
   		url: "text",

   		data: "user=success",
   		success: function(text){
        var myTextarea = $('#myTextarea');
   	 		myTextarea.val(text);
     		
        if(myTextarea.length)
          myTextarea.scrollTop(myTextarea[0].scrollHeight - myTextarea.height());
   		}
 	});
}
</script>
</head>
<body>
<textarea id= 'myTextarea' 
  style="width:410px;height:300px">
</textarea>
<form id='myForm' action='/' method='POST'>
  <input style="width:100px" type="text" name="usr" value="%(usr)s">
  <input style="width:250px" type="text" name="msg" value="" autofocus>
  <input style="width:50px"type="submit" value="send">
</form>
Lastest message:
<div id="result"></div>
<script>
$('#myForm').submit(function( event ) {
  event.preventDefault();
  var $form = $( this ),
    _usr = $form.find( "input[name='usr']" ).val(),
    _msg = $form.find( "input[name='msg']" ).val(),
    url = $form.attr( "action" );

  var posting = $.post( url, {usr:_usr, msg:_msg} );
  
  posting.done(function( data ) {
  	console.log(data)
    $( "#result" ).empty().append( data );
  });
});
</script>
</body></html>'''
messages=[]
text=""
@app.route('/',methods=['GET'])
def index():
	return ( html%{'usr': 'Anonymous'})
@app.route('/',methods=['POST'])
def addText():
	global text
	usr=request.form.get('usr', 'Anonymous')
	if not usr:
		usr='Anonymous'
	msg=request.form.get('msg', '')[:100]
	if len(messages)>100:
		messages.pop(0)
	messages.append("{0}[{1}]:{2}".format(usr,request.environ['REMOTE_ADDR'],msg))
	text="Welcome to simple chat!"
	for m in messages:
		text=text+"\n"+m
	return '{} said "{}".'.format(usr,msg)
@app.route('/text')
def gettext():
	global text
	return text
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080,debug=True)