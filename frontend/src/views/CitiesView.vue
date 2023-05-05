<script>
import cities from "/src/datasets/cities.json";
import CityComponent from "../components/CityComponent.vue";

export default {
  name: "CitiesView",
  components: {
    CityComponent,
  },
  data() {
    return {
      cities: [],
    };
  },
  created() {
    this.cities = cities;
  },
};
</script>

<template>
  <div class="cities-container">
    <CityComponent
      v-for="(city, index) in cities"
      :key="index"
      :name="city.name"
      :country_name="city.country_name"
      :country_code="city.country_code"
      :state_name="city.state_name"
      :state_code="city.state_code"
      :latitude="city.latitude"
      :longitude="city.longitude"
    ></CityComponent>
  </div>
</template>

<style scoped>
@media (min-width: 1024px) {
  .cities-container {
    text-align: center;
    overflow-y: auto;
    vertical-align: middle;
    display: grid;
    grid-template-columns: auto auto auto;
    grid-gap: 10px;
    padding: 10px;
  }
}
</style>
