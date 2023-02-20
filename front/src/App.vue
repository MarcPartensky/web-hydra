<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import DumbButton from './components/DumbButton.vue'
import HydraForm from './components/HydraForm.vue'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/hydra.png" width="125" height="125" />
  </header>
    <div class="wrapper">
        <DumbButton />
        <HydraForm />

        <!-- <TextInput :text="Choose url" /> -->
      <!-- <input class="e-input" type="text" placeholder="Enter url" /> -->
      <!-- <br> -->
      <!-- <input class="e-input" type="text" placeholder="Enter protocol" /> -->
      <!-- <br> -->
      <!-- <input class="e-input" type="text" placeholder="Enter port" /> -->

      <!-- <UrlInput message="url" /> -->
      <!-- <nav> -->
        <!-- <RouterLink to="/">Home</RouterLink> -->
        <!-- <RouterLink to="/about">About</RouterLink> -->
      <!-- </nav> -->
    <!-- <FormulateForm -->
    <!--     v-model="values" -->
    <!--     @submit="handleLogin" -->
    <!--   > -->
    <!--     <h2>Login</h2> -->
    <!--     <FormulateInput type="text" name="email" label="Email address" validation="required|email" /> -->
    <!--     <FormulateInput type="text" name="password" label="Password" validation="required" /> -->
    <!--     <FormulateInput name="terms" type="checkbox" label="I accept, just don't make me read the terms." validation="accepted" /> -->
    <!--     <FormulateInput type="submit" label="Login" /> -->
    <!--     <pre>{{ values }}</pre> -->
    <!--   </FormulateForm> -->
    </div>

      <!-- <RouterView /> -->
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

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
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
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
