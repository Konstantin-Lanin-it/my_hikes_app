<template>
  <div>
    <Header />
    <main>
      <nuxt /> <!-- Здесь будут отображаться ваши страниц -->
    </main>
    <Footer />
  </div>
</template>

<script>
import Header from '~/components/Header.vue';
import Footer from '~/components/Footer.vue';

export default {
  components: {
    Header,
    Footer
  }
}
</script>

<style>
/* Общие стили для всего приложения */
main {
  padding: 20px;
  min-height: 80vh; /* Обеспечивает минимальную высоту для контента */
  background-color: #f9f9f9; /* Светлый фон для основного контента */
}

header {
  background-color: #4DBA87; /* Цвет фона для хедера */
  color: white; /* Цвет текста в хедере */
}

footer {
  background-color: #333; /* Цвет фона для футера */
  color: white; /* Цвет текста в футере */
  text-align: center;
  padding: 10px 0;
}
</style>