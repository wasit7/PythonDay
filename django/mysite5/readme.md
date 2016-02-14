To send object between client and server by using Ajax, we need to code for both server-side and client-side

#### views.py
```python
        from django.http import JsonResponse
        import json
        def set_data_to_server(request):  
            server_data = {'server_data':[
                    {'key':'value0'},
                    {'key':'value1'},
                ]}
            client_data=json.loads(request.POST.get('client_data'))
            return JsonResponse( server_data)
            
```


####home.html
```html
        var client_data={key:'value'};
        <script>
            $(document).ready(function(){
                $.ajax({
                    url: 'http://this.can.be.relative.path',
                    type: 'GET',
                    data:{
                        client_data: JSON.stringify(client_data)
                    },
                    success: function(data_from_server) {
                            console.log( JSON.stringify(server_data) );
                    }
                });
            });
        </script>
```