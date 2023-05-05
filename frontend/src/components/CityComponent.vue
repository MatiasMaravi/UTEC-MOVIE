<script>
export default {
  name: "CityComponent",
  props: [
    "name",
    "country_name",
    "country_code",
    "state_name",
    "state_code",
    "latitude",
    "longitude",
  ],
};
</script>

<template>
  <!--TODO: Utilizar la propiedad creada para controlar el click. Cuando el componente es "clickeable", redirigir a la pagina del pais.
  Mira las rutas para ver como redirigir al usuario.-->
  <div class="city">
    <!--TODO: Poblar el HTML con las propiedades. Usar https://countryflagsapi.com/png/${code}-->
    <h1>
      {{ name }}
    </h1>
    <h2>País: {{ country_name }} ({{ country_code }})</h2>
    <h3>Estado: {{ state_name }} ({{ state_code }})</h3>
    <h3>Latitud: {{ latitude }}</h3>
    <h3>Longitud: {{ longitude }}</h3>
    <img src="/src/assets/city.jpg" width="200" height="170" />
  </div>
</template>

<style scoped>
.city {
  padding: 2px;
  white-space: nowrap;
  width: 350px;
  height: 350px;
  border-style: solid;
  border-radius: 5px;
  border-color: grey;
}
h1 {
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>
