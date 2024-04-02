## SyncConsumer

In SyncConsumer, there is not need any function because it's django ORM is a synchronous proccess.

## AsyncConsumer

In AsyncConsumer, Write your ORM queries in a seperate function or method and then it with database_synch_to async.Example

```
from channels.db import database_sync_to_async
...
async def websocket_connect(self,event):
    self.username=await database_sync_to async(self.get_name)()

def get_name(self):
    return User.objects.all()[0].name

...

Use it as decorator
@database_sync_to_async
def get_name(self):
    return User.objects.all()[0].name

```
