To send an object between client and server by using Ajax, we need codes for both server-side and client-side.

#### views.py
```python
        from django.http import JsonResponse
        import json
        def data_exchanger(request):
                client_data=json.loads(request.GET.get('client_data'))
                server_data = {'server_data':[
                        {'key':'value0'},
                        {'key':'value1'},
                ]}
                return JsonResponse( server_data)
```

####home.html
```html
        var client_data={key:'value'};
        <script>
            $(document).ready(function(){
                $.ajax({
                        url: 'http://this.can.be.relative.path/data_exchanger',
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
