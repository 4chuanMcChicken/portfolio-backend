# 使用 Python 官方提供的镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将 Pipfile 和 Pipfile.lock 复制到容器中
COPY Pipfile Pipfile.lock ./

# 安装 Pipenv
RUN pip install pipenv

# 使用 Pipenv 安装依赖
RUN pipenv install --system --deploy

# 将项目文件复制到容器中（假设你的项目文件在当前目录中）
COPY . .

# 执行你的应用程序，比如启动 Django 服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]