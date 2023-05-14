<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String,
  },
}
</script>

<template>
  <div class="greetings">
    <h1>{{ msg }}</h1>
    <h3>
      Get information about popular movies!
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  color: #00d4ff;
}

h3 {
  font-size: 1.2rem;
  top: 10px;
}

.greetings h1,
.greetings h3 {
  text-align: center;
  color: #000;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
