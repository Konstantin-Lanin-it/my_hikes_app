<template>
  <div class="hike-detail">
    <h1>{{ hike.title }}</h1>
    <img :src="hike.image_url" alt="Hike Image" class="hike-image" />
    <p>{{ hike.description }}</p>

    <button @click="applyForHike" class="apply-button">Подать заявку на поход</button>
  </div>
</template>

<script>
export default {
  name: 'HikeDetail',
  data() {
    return {
      hike: null
    };
  },
  async asyncData({ params, $axios }) {
    try {
      const response = await $axios.get(`/api/hikes/${params.id}`); // Измените на ваш API
      return {
        hike: response.data
      };
    } catch (error) {
      console.error('Ошибка при загрузке данных о походе:', error);
      return {
        hike: {}
      };
    }
  },
  methods: {
    applyForHike() {
      // Логика для подачи заявки на поход
      console.log('Заявка подана на поход:', this.hike.title);
      // Здесь может быть кнопка для навигации к форме заявки или отправки данных на сервер
    }
  }
}
</script>

<style scoped>
.hike-detail {
  padding: 20px;
}

.hike-image {
  width: 100%;
  height: auto;
  border-radius: 8px;
  margin-bottom: 20px;
}

.apply-button {
  background-color: #4DBA87;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px 15px;
  cursor: pointer;
}

.apply-button:hover {
  background-color: #3b9f73;
}
</style>