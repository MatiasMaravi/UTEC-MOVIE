<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/BEST-MOVIES-OF-2021.webp" />
    <div class="wrapper">
      <HelloWorld msg="UTEC Movie" />
      <nav>
        <nav class="Navbar">
          <ul class="nav-links">
            <div class="menu">
              <li><router-link to="/">home</router-link></li>
              <li><RouterLink to="/countries">Movies</RouterLink></li>
              <li><RouterLink to="/cities">Cities</RouterLink></li>
              <li>
                <RouterLink to="/capitalsGame">Capitals Game</RouterLink>
              </li>
            </div>
          </ul>
        </nav>
      </nav>
    </div>
  </header>
  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}
@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
    top: -100px;
  }
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  a {
    text-decoration: none;
  }

  li {
    list-style: none;
  }
  .Navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px;
    background-color: rgb(0, 0, 0);
    color: #fff;
  }
  .nav-links a {
    color: #fff;
  }
  .logo {
    font-size: 32px;
  }
  .menu {
    display: flex;
  }
  .menu li:hover {
    background-color: #4c9e9e;
    border-radius: 5px;
    transition: 0.3s ease;
  }
  .menu li {
    padding: 5px 14px;
  }

  .Dropdown {
    background-color: rgb(1, 139, 139);
    padding: 1em 0;
    position: absolute;
    display: none;
    border-radius: 8px;
    top: 35px;
  }
  .Dropdown li + li {
    margin-top: 10px;
  }
  .Dropdown li {
    padding: 0.5em 1em;
    width: 8em;
    text-align: center;
  }
  .Dropdown li:hover {
    background-color: #4c9e9e;
  }
}
header {
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #4096f8;
  min-height: 100%;
}
</style>
