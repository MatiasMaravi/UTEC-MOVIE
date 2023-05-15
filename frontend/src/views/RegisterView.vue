<script>
  export default {
    name: 'RegisterView',
    data() {
      return {
        username: '',
        email: '',
        password: '',
      };
    },
    methods: {
      async register() {
        try {
          // Realiza la solicitud de registro a tu API
          const response = await fetch('http://lb-pp-prod-1168650394.us-east-1.elb.amazonaws.com:8004/register', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({
              username: this.username,
              email: this.email,
              password: this.password,
            }),
          });
          console.log("awd")
          if (response.ok) {
            // Registro exitoso, puedes redirigir a la página de inicio de sesión
            this.$router.push('/login');
          } else {
            // El registro falló, maneja el error (mostrar mensaje de error, limpiar campos, etc.)
            console.error('Registro fallido');
          }
        } catch (error) {
          console.error(error);
        }
      },
    },
  };
  </script>

<template>
    <div class="register-view">
      <h1>Register</h1>
      <form @submit.prevent="register">
        <input type="text" v-model="username" placeholder="Username" />
        <input type="text" v-model="email" placeholder="Email" />
        <input type="password" v-model="password" placeholder="Password" />
        <button type="submit">Register</button>
      </form>
    </div>
  </template>
  
  <style scoped>
  .register-view {
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
  
  button {
    display: block;
    width: 100%;
    padding: 10px;
    border-radius: 0.4em;
    font-size: 16px;
    font-weight: bolder;
    background-color: #00d4ff;
    color: white;
    border: none;
  }
  </style>