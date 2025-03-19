export default function ({ store, redirect }) {
    // Проверка, авторизован ли пользователь
    const isAuthenticated = store.state.auth.isAuthenticated; // Предполагается, что вы храните информацию о состоянии аутентификации в Vuex
  
    if (!isAuthenticated) {
      // Если пользователь не авторизован, перенаправляем его на страницу входа
      return redirect('/login');
    }
  }