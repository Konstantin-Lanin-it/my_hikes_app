<template>
  <footer class="footer">
    <div class="footer-content">
      <p>&copy; {{ currentYear }} My Hikes App. Все права защищены.</p>
      <div class="social-links">
        <nuxt-link to="/privacy-policy">Политика конфиденциальности</nuxt-link>
        |
        <nuxt-link to="/terms-of-service">Условия обслуживания</nuxt-link>
        |
        <a href="https://facebook.com" target="_blank" rel="noopener noreferrer">Facebook</a>
        <a href="https://twitter.com" target="_blank" rel="noopener noreferrer">Twitter</a>
        <a href="https://instagram.com" target="_blank" rel="noopener noreferrer">Instagram</a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  data() {
    return {
      currentYear: new Date().getFullYear() // Получаем текущий год
    };
  }
}
</script>

<style scoped>
.footer {
  background-color: #333; /* Цвет фона для подвала */
  color: white; /* Цвет текста в подвале */
  text-align: center; /* Выравнивание по центру */
  padding: 20px 0; /* Отступы по вертикали */
}

.footer-content {
  margin: 0 20px; /* Горизонтальные отступы */
}

.social-links a {
  color: white; /* Цвет ссылок */
  margin: 0 10px; /* Отступы между ссылками */
  text-decoration: none; /* Убираем подчеркивание у ссылок */
}

.social-links a:hover {
  text-decoration: underline; /* Подчеркивание при наведении */
}
</style>