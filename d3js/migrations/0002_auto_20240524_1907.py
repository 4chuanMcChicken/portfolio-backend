from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('d3js', '0001_initial'),  # 确保这里是你的初始迁移文件
    ]

    operations = [
        migrations.RunSQL(
            """
            INSERT INTO d3js_visitcount (ip_address, happen_time) VALUES 
            ('192.168.1.1', '2024-05-22 10:15:00'),
            ('192.168.1.2', '2024-05-22 11:20:00'),
            ('192.168.1.3', '2024-05-23 12:25:00'),
            ('192.168.1.4', '2024-05-23 13:30:00'),
            ('192.168.1.5', '2024-05-23 14:35:00'),
            ('192.168.1.6', '2024-05-24 15:40:00'),
            ('192.168.1.7', '2024-05-24 16:45:00');
            """
        ),
    ]
