from django.db import models


class VisitorRecord(models.Model):
    """访客记录"""
    addr = models.CharField(max_length=16, verbose_name="远程主机IP")
    host = models.CharField(max_length=32, verbose_name="远程主机名")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="访问时间")


class CityWeather(models.Model):
    """获取当前天气"""
    city = models.CharField(max_length=16, verbose_name="地名")
    city_num = models.CharField(max_length=16, verbose_name="地名编号")
    temperature = models.CharField(max_length=10, verbose_name="温度")
    humidity = models.CharField(max_length=10, verbose_name="湿度")
    wind = models.CharField(max_length=10, verbose_name="风向风力")
    aqi = models.CharField(max_length=10, verbose_name="空气指数")
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")


class Machine(models.Model):
    """机器状态信息"""
    pass
