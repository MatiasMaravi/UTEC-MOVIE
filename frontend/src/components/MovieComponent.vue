<script>
export default {
  name: 'MovieComponent',
  props: [
    'title',
    'imageurl',
    'released',
    'rating',
    'imdbid',
    'clickable',
  ],
  data() {
    return {
      url: "",
      imageStyle: {
        boxShadow: '0 0 25px rgba(0, 212, 255, 0.5)',
      },
    };
  },
  created() {
    this.url = 'https://image.tmdb.org/t/p/original' + this.imageurl;
  },
  methods: {
    handleClick() {
      if (this.clickable) {
        this.$router.push({ path: '/movies/' + this.imdbid })
      }
    }
  },
}
</script>

<template>
  <div
    class="movie"
    :class="{ 'movie-hover': clickable }"
    @click="handleClick"
  >
    <h1>
      {{ title }}
    </h1>
    <div class="image">
      <img
        :src="url"
        :width="140"
        :style="imageStyle"
      />
    </div>
    <h3>Released: {{ released }}</h3>
    <div class="rating">
      <h3>{{ rating }}</h3>
      <img src="@/assets/star-icon.svg"/>
    </div>
  </div>
</template>

<style scoped>
.movie {
  padding: 2px;
  white-space: nowrap;
  width: 350px;
  height: 350px;
  border-style: solid;
  border-radius: 5px;
  border-color: rgb(25, 25, 25);
}

.movie-hover:hover {
  background-color: rgb(25, 25, 25);
  cursor: pointer;
}

.image {
  display: flex;
  align-items: center;
  justify-content: center;
}

h1 {
  overflow: hidden;
  text-overflow: ellipsis;
  font-weight: bold;
  color: #00d4ff;
  margin-block: 5px;
}

h3 {
  font-weight: bold;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-block-start: 5px;
}
.rating{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.6em;
    margin: 0.6em 0 0.9em 0;
}

.rating img{
    width: 1.2em;
}

.rating h3{
    display: inline-block;
    font-weight: bold;
    margin-block-start: -10px;
}
</style>
