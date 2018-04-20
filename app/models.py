from django.db import models

# Create your models here.

class Mysql_info(models.Model):
    name = models.CharField(max_length=11,null=False)
    # 格言
    motto = models.TextField()
    profession = models.CharField(max_length=11,null=False)
    profession_info = models.TextField()
    student = models.TextField(null=False)
    student_info = models.TextField()
    address = models.CharField(max_length=11)
    address_info = models.TextField()
    school = models.CharField(max_length=11, null=False)
    school_info = models.TextField()
    class Meta:
        db_table = 'info'

    def __str__(self):

        return '姓名：{} 专业：{}'.format(self.name,self.profession)
