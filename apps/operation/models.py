from datetime import datetime

from django.db import models

from users.models import UserProfile
from course.models import Course

# Create your models here.
class UserAsk(models.Model):
    '''
    用户咨询
    '''
    name = models.CharField(verbose_name="姓名", max_length=20)
    mobile = models.CharField(verbose_name="手机", max_length=11)
    course_name = models.CharField(verbose_name="课程名", max_length=50)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserMessage(models.Model):
    '''
    用户消息表
    '''
    user = models.IntegerField(verbose_name="接受用户", default=0)
    message = models.CharField(verbose_name="消息内容", max_length=500)
    has_read = models.BooleanField(verbose_name="是否已读", default=False)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    '''
    用户评论
    '''
    user = models.ForeignKey(UserProfile, verbose_name="用户", \
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", \
                               on_delete=models.CASCADE)
    comments = models.CharField(verbose_name="评论", max_length=200)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "课程评论"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    '''
    用户学习的课程
    '''
    user = models.ForeignKey(UserProfile, verbose_name="用户", \
                             on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name="课程", \
                               on_delete=models.CASCADE)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户课程"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    '''
    用户收藏
    '''
    FAV_TYPE = (
        (1, '课程'),
        (2, '课程机构'),
        (3, '讲师')
    )

    user = models.ForeignKey(UserProfile, verbose_name="用户", \
                             on_delete=models.CASCADE)
    fav_id = models.IntegerField(verbose_name="数据id", default=0)
    fav_type = models.IntegerField(verbose_name="收藏类型", \
                                   choices=FAV_TYPE, default=1)
    add_time = models.DateTimeField(verbose_name="添加时间", default=datetime.now)

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name