# Usar una imagen base de Python
FROM python:3.8-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . .

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto en el que corre la aplicación
EXPOSE 80

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]