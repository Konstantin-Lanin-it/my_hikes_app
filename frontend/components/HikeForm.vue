<template>
  <form @submit.prevent="submitForm" class="hike-form">
    <h2>{{ isEdit ? 'Редактировать' : 'Создать' }} Поход</h2>
    
    <div class="form-group">
      <label for="title">Название:</label>
      <input type="text" id="title" v-model="form.title" required />
    </div>
    
    <div class="form-group">
      <label for="description">Описание:</label>
      <textarea id="description" v-model="form.description" required></textarea>
    </div>

    <div class="form-group">
      <label for="image_url">URL изображения:</label>
      <input type="url" id="image_url" v-model="form.image_url" />
    </div>
    
    <button type="submit" class="submit-button">{{ isEdit ? 'Сохранить изменения' : 'Создать поход' }}</button>
  </form>
</template>

<script>
export default {
  name: 'HikeForm',
  props: {
    hike: {
      type: Object,
      default: () => ({
        title: '',
        description: '',
        image_url: ''
      })
    },
    isEdit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      form: {
        title: this.hike.title,
        description: this.hike.description,
        image_url: this.hike.image_url
      }
    };
  },
  methods: {
    submitForm() {
      // Логика для отправки данных формы
      this.$emit('submit', this.form);
    }
  }
}
</script>

<style scoped>
.hike-form {
  display: flex;
  flex-direction: column;
  max-width: 400px;
  margin: auto;
}

.form-group {
  margin-bottom: 15px;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

input, textarea {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
}

textarea {
  resize: vertical;
}

.submit-button {
  background-color: #4DBA87;
  color: white;
  border: none;
  border-radius: 4px;
  padding: 10px;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #3b9f73;
}
</style>