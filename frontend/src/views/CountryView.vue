<script>
import countries from "/src/datasets/countries.json";

export default {
  name: "CountryView",
  components: {},
  data() {
    return {
      country: {},
    };
  },
  created() {
    this.country = countries.find(
      (country) => country.iso2 === this.$route.params.code
    );
  },
  methods: {},
};
</script>

<template>
  <div class="info">
    <img width="400" height="400" src="https://countryflagsapi.com/png/${country.numeric_code}" class="poster">
    <div>
      <h2>{{ country.name }}</h2>
      <div class="details">
        <span>Capital: {{ country.capital }}</span>
        <span>Moneda: {{ country.currency_name }} ({{ country.currency }})</span>
        <span>Región: {{ country.region }}</span>
      </div>
    </div>
  </div>
</template>

<style scoped>
/*
.country {
  position: relative;
  display: grid;
  grid-template-columns: 4fr 8fr;
  margin-top: 1.2em;
}
*/
@media (min-width: 1024px) {
}

.info{
    position: relative;
    display: grid;
    grid-template-columns: 4fr 8fr;
    margin-top: 1.2em;
}

.poster{
    width: 100%;
}

h2{
    text-align: center;
    font-size: 1.5em;
    font-weight: 600;
    letter-spacing: 0.06em;
}
/*
.traducciones {
  color: white;
  display: grid;
}

.nombre {
  font-size: 50px;
}*/
</style>
