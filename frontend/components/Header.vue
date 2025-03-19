<template>
  <header class="header">
    <div class="logo">
      <nuxt-link to="/">My Hikes App</nuxt-link>
    </div>
    <nav>
      <ul class="nav-links">
        <li>
          <nuxt-link to="/">Главная</nuxt-link>
        </li>
        <li>
          <nuxt-link to="/about">О нас</nuxt-link>
        </li>
        <li>
          <nuxt-link to="/hikes">Походы</nuxt-link>
        </li>
        <li>
          <nuxt-link to="/contact">Контакты</nuxt-link>
        </li>
      </ul>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'Header'
}
</script>

<style scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #4DBA87; /* Цвет фона для заголовка */
  padding: 10px 20px;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: white; /* Цвет текста для логотипа */
}

.nav-links {
  list-style: none; /* Убираем маркеры списка */
  display: flex;
  margin: 0;
  padding: 0;
}

.nav-links li {
  margin-left: 20px; /* Отступ между ссылками */
}

.nav-links a {
  text-decoration: none; /* Убираем подчеркивание у ссылок */
  color: white; /* Цвет текста для ссылок */
}

.nav-links a:hover {
  text-decoration: underline; /* Подчеркивание при наведении */
}
</style>