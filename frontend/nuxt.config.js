export default {
    // Устанавливаем режим рендеринга: 'universal' или 'spa'
    mode: 'universal',
  
    // Заголовок страницы
    head: {
      title: 'My Nuxt App',
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', name: 'description', content: 'My Nuxt.js application' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ]
    },
  
    // Указываем директорию, где находятся страницы
    srcDir: 'src/',
  
    // Папка страниц
    pages: {
      // Вы можете определить страницы здесь, но в Nuxt автоматически найдутся все файлы в директории `pages`
    },
  
    // Указываем модули
    modules: [
      '@nuxtjs/axios', // Модуль для работы с HTTP-запросами
      '@nuxtjs/pwa' // Прогрессивные веб-приложения
    ],
  
    // Конфигурация Axios
    axios: {
      baseURL: 'https://api.example.com' // Базовый URL для всех запросов
    },
  
    // Конфигурация PWA
    pwa: {
      manifest: {
        name: 'My Nuxt App',
        short_name: 'NuxtApp',
        lang: 'en',
        display: 'standalone',
        background_color: '#ffffff',
        theme_color: '#4DBA87'
      }
    },
  
    // Плагины
    plugins: [
      '~/plugins/my-plugin.js' // Ваши плагины
    ],
  
    // Настройки сборки
    build: {
      // Дополнительные параметры сборки
      extractCSS: true, // Извлечение CSS в отдельный файл
      optimizeCSS: true // Оптимизация CSS
    }
  }