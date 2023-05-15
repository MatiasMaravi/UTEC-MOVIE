<script>
export default {
  name: "LoginView",
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await fetch("http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8004/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          }),
        });
        console.log("awdawd")
        if (response.ok) {
          const data = await response.json();
          console.log(data)
          const token = data.token;
          const userId = data.user_id; // Obtener el ID del usuario desde la respuesta de la API

          // Guarda variables globales
          this.$root.userName = this.username; // Guarda el username
          this.$root.isLoggedIn = true; // Actualiza el valor de si el usuario esta logeado
          this.$root.userId = userId; // Guarda el ID del usuario en la raíz de Vue
          
          // Redirige a la página deseada después del inicio de sesión exitoso
          this.$router.push("/");
        } else {
          // El inicio de sesión falló, maneja el error (mostrar mensaje de error, limpiar campos, etc.)
          console.error("Inicio de sesión fallido");
        }
      } catch (error) {
        console.error(error);
      }
    },
    logOut() {
      this.$root.isLoggedIn = false;
      this.$root.userName = "";
      this.$router.push("/");
    },
    goToRegister() {
      this.$router.push("/register"); // Navega a la vista de registro
    },
  },
};
</script>

<template>
  <div v-if="$root.isLoggedIn">
    <h1>You're logged in!</h1>
    <h2>Username: {{ $root.userName }}</h2>
    <div class="button-container">
      <button class="logout-button" @click="logOut">Log out</button>
    </div>
  </div>
  <div class="login-view" v-else>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input type="text" v-model="username" placeholder="Username" />
      <input type="password" v-model="password" placeholder="Password" />
      <button type="submit">Sign in</button>
    </form>
    <div class="button-container">
      <button @click="goToRegister">Register</button>
    </div>
  </div>
</template>

<style scoped>
.login-view {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}

h1 {
  font-size: 24px;
  font-weight: bolder;
  margin-bottom: 20px;
}

input {
  display: block;
  width: 100%;
  margin-bottom: 10px;
  padding: 10px;
  font-size: 16px;
  border-radius: 0.4em;
}

.button-container {
  margin-top: 10px;
}

button {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border-radius: 0.4em;
  font-weight: bolder;
  background-color: #00d4ff;
  color: white;
  border: none;
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #00a7cc;
}

.logout-button {
  width: 100%;
  max-width: 200px; /* Ajusta el valor según el ancho deseado */
  margin: 0 auto; /* Centra horizontalmente el botón */
}
</style>