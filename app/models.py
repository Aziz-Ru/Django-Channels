from django.db import models

class Group(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Chats(models.Model):
    group=models.ForeignKey(Group,on_delete=models.CASCADE)
    content=models.CharField(max_length=255)
    timestamp=models.DateTimeField(auto_now=True)
