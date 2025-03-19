# Используем официальный образ Node.js в качестве базового
FROM node:16 AS build

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл package.json и package-lock.json для установки зависимостей
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем весь код в контейнер
COPY . .

# Собираем приложение
RUN npm run build

# Используем nginx для обслуживания собранного приложения
FROM nginx:alpine

# Копируем собранные файлы в папку, откуда nginx будет их обслуживать
COPY --from=build /app/build /usr/share/nginx/html

# Экспонируем порт 80
EXPOSE 80

# Команда для запуска nginx
CMD ["nginx", "-g", "daemon off;"]