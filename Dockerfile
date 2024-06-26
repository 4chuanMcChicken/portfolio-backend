# 使用官方Python基础镜像
FROM python:3.11-slim

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 创建并设置工作目录
WORKDIR /app

# 安装系统依赖和 pipenv
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev \
    && pip install pipenv

# 复制Pipfile和Pipfile.lock文件
COPY Pipfile Pipfile.lock /app/

# 安装Python依赖
RUN pipenv install --system --deploy

# 复制项目文件
COPY . /app/

# 暴露Django默认端口
EXPOSE 8000

# 启动Django应用
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
