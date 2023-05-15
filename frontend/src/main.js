import { createApp } from "vue";
import { createPinia } from "pinia";

import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

const app = createApp(App);
// Variable global para almacenar el estado de inicio de sesión
app.config.globalProperties.isLoggedIn = false;
app.config.globalProperties.userName = "";
app.config.globalProperties.userId = null;

// Función para actualizar el estado de inicio de sesión
app.config.globalProperties.updateIsLoggedIn = function(value) {
  this.isLoggedIn = value;
};

app.use(createPinia());
app.use(router);

app.mount("#app");
