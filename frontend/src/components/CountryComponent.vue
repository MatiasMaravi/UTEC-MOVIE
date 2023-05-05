<script>
export default {
  name: "CountryComponent",
  props: [
    "name",
    "capital",
    "currency_name",
    "currency",
    "region",
    "code",
    //TODO: crear una propiedad para determinar si al componente se le puede hacer click
    "clickable"
  ],
  methods: {
    handleClick() {
      if (this.clickable) {
        this.$router.push({path: '/countries/' + this.code})
      }
    }
  }
};
</script>

<template>
  <!--TODO: Utilizar la propiedad creada para controlar el click. Cuando el componente es "clickeable", redirigir a la pagina del pais.
  Mira las rutas para ver como redirigir al usuario.-->
  <div class="country" :class="{'country-hover': clickable}" @click="handleClick">
    <!--TODO: Poblar el HTML con las propiedades. Usar https://countryflagsapi.com/png/${code}-->
    <img
      src="https://countryflagsapi.com/png/${code}"
      width="200"
      height="200"
    />
    <h1>
      {{ name }}
    </h1>
    <h2>Capital: {{ capital }}</h2>
    <h3>Moneda: {{ currency_name }} ({{ currency }})</h3>
    <h3>Región: {{ region }}</h3>
  </div>
</template>

<style scoped>
.country {
  padding: 2px;
  white-space: nowrap;
  width: 350px;
  height: 350px;
  border-style: solid;
  border-radius: 5px;
  border-color: grey;
}

.country-hover:hover {
  background-color: rgb(49, 49, 49);
  cursor: pointer;
}

h1 {
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
