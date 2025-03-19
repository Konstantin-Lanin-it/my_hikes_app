<template>
  <div class="home">
    <h1>Добро пожаловать в приложение Походов</h1>
    <p>Здесь вы можете найти и создать походы!</p>
    
    <h2>Список Походов</h2>
    <div class="hike-list">
      <HikeCard
        v-for="hike in hikes"
        :key="hike.id"
        :hike="hike"
        @apply="handleApply"
      />
    </div>
    
    <h2>Создать Поход</h2>
    <HikeForm @submit="handleCreate" />
  </div>
</template>

<script>
import HikeCard from '~/components/HikeCard.vue';
import HikeForm from '~/components/HikeForm.vue';

export default {
  components: {
    HikeCard,
    HikeForm
  },
  data() {
    return {
      hikes: [
        {
          id: 1,
          title: 'Горный поход',
          description: 'Захватывающий поход по горным тропам.',
          image_url: 'https://example.com/image1.jpg'
        },
        {
          id: 2,
          title: 'Лесной поход',
          description: 'Исследуйте великолепные леса.',
          image_url: 'https://example.com/image2.jpg'
        }
      ]
    };
  },
  methods: {
    handleApply(hike) {
      // Логика обработки заявки на выбранный поход
      console.log('Заявка на поход:', hike);
    },
    handleCreate(formData) {
      // Логика создания нового похода
      const newHike = {
        id: this.hikes.length + 1,
        ...formData
      };
      this.hikes.push(newHike);
      console.log('Создан новый поход:', newHike);
    }
  }
}
</script>

<style scoped>
.home {
  padding: 20px;
}

h1, h2 {
  color: #333;
}

.hike-list {
  display: flex;
  flex-wrap: wrap;
  margin-bottom: 20px;
}
</style>