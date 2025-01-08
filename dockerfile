# 使用 Python 3.9 镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 将项目的依赖文件复制到容器中
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目代码到容器中
COPY . .

# 暴露容器的端口
EXPOSE 8000

# 使用 Hypercorn 启动服务
CMD ["hypercorn", "main:app", "--bind", "0.0.0.0:8090", "--reload"]