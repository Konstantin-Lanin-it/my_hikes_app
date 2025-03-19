export const state = () => ({
    hikes: [] // Состояние для хранения списка походов
  });
  
  export const mutations = {
    setHikes(state, hikes) {
      state.hikes = hikes; // Устанавливаем массив походов
    },
    addHike(state, hike) {
      state.hikes.push(hike); // Добавляем новый поход в массив
    }
  };
  
  export const actions = {
    async fetchHikes({ commit }) {
      try {
        const response = await this.$axios.get('/api/hikes'); // Измените на ваш API
        commit('setHikes', response.data);
      } catch (error) {
        console.error('Ошибка при загрузке походов:', error);
      }
    },
    async createHike({ commit }, hike) {
      try {
        const response = await this.$axios.post('/api/hikes', hike); // Измените на ваш API
        commit('addHike', response.data);
      } catch (error) {
        console.error('Ошибка при создании похода:', error);
      }
    }
  };
  
  export const getters = {
    allHikes(state) {
      return state.hikes; // Возвращает все походы
    },
    hikeCount(state) {
      return state.hikes.length; // Возвращает количество походов
    }
  };