<script>
import countries from "/src/datasets/countries.json";
import CountryComponent from "../components/CountryComponent.vue";

export default {
  name: "CapitalsGameView",
  components: {
    CountryComponent,
  },
  data() {
    return {
      country: {},
      capital: "",
      puntaje: 0,
    };
  },
  created() {
    this.country = countries[Math.floor(Math.random() * countries.length)];
  },
  methods: {
    setCapital(e) {
      //TODO: implementar. fija la capital del input.
      this.capital = e;
    },
    adivinarCapital() {
      //TODO: implementar. verifica se la adivinanza es correcta.
      if (this.capital == this.country["capital"]) this.puntaje++;
      this.created();
    },
  },
};
</script>

<template>
  <h1>Puntaje: {{ puntaje }}</h1>
  <div class="countries">
    <!-- TODO: usar los metodos definidos arriba dentro del input para llenar el estado de la capital a adivinar-->
    <input placeholder="Adivina la capital" @input="setCapital" />
    <button @click="adivinarCapital">Adivina!</button>
    <div class="countries-container">
      <!--TODO: CREAR EL COMPONENTE PARA VISUALIZAR EL PAIS-->
      <img
        src="https://countryflagsapi.com/png/${country.numeric_code}"
        width="200"
        height="200"
      />
      <h1>
        {{ country.name }}
      </h1>
      <h2>Capital: ???</h2>
      <h2>Capital: {{ country.capital }}</h2>
      <h3>Moneda: {{ country.currency_name }} ({{ country.currency }})</h3>
      <h3>Región: {{ country.region }}</h3>
    </div>
  </div>
</template>

<style scoped>
@media (min-width: 1024px) {
  .countries {
    align-items: center;
  }

  input {
    line-height: em;
  }

  .countries-container {
    margin-left: 35%;
    align-items: center;
    overflow-y: auto;
    vertical-align: middle;
    padding: 10px;
    white-space: nowrap;
    width: 375px;
    height: 375px;
    border-radius: 2px;
    border-color: grey;
  }
}
</style>
