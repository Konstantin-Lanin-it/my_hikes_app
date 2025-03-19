<template>
  <div class="hike-card">
    <img :src="hike.image_url" alt="Hike Image" class="hike-image" />
    <div class="hike-info">
      <h3 class="hike-title">{{ hike.title }}</h3>
      <p class="hike-description">{{ hike.description }}</p>
      <button @click="onApply" class="apply-button">Подать заявку</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HikeCard',
  props: {
    hike: {
      type: Object,
      required: true
    }
  },
  methods: {
    onApply() {
      // Здесь можно реализовать логику обработки заявки
      // Например, показать модальное окно или перенаправить на страницу заявки
      this.$emit('apply', this.hike);
    }
  }
}
</script>

<style scoped>
.hike-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  margin: 16px;
  max-width: 300px;
  transition: transform 0.2s;
}

.hike-card:hover {
  transform: scale(1.05);
}

.hike-image {
  width: 100%;
  height: 180px;
  object-fit: cover;
}

.hike-info {
  padding: 16px;
}

.hike-title {
  font-size: 20px;
  margin: 0 0 8px;
}

.hike-description {
  font-size: 16px;
  margin: 0 0 16px;
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