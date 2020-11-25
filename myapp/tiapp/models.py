from django.db import models


class Matkul(models.Model):
      matakuliah=models.CharField(max_length=200)
      dosen=models.CharField(max_length=100,null=True)
      hari=models.CharField(max_length=50,null=True)
      jam=models.CharField(max_length=20,null=True)

      def __str__(self):
            return '%s %s %s %s' % (self.matakuliah,self.dosen,self.hari,self.jam)

class Info(models.Model):
      content=models.TextField()
      user=models.CharField(max_length=30,null=True)
      date = models.DateTimeField(auto_now_add=True,null=True)

      def __str__(self):
            return '%s %s %s' % (self.content,self.user,self.date)


class User(models.Model):
      username=models.CharField(max_length=30,null=True)
      password=models.CharField(max_length=30,null=True)

      def __str__(self):
            return '%s %s' % (self.username,self.password)

      
      