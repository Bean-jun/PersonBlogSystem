"""
bootstrap插件样式
"""


class BootStrapForm(object):
    """创建Bootstrap样式"""
    def __init__(self, *args, **kwargs):
        super(BootStrapForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = "请输入{}".format(field.label)