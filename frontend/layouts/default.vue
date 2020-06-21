<template>
  <div id="page">
    <b-navbar toggleable="md" type="dark" variant="info">
      <b-navbar-brand tag="h1" class="mb-0" href="#">Potluck Party</b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="#">About</b-nav-item>
        <b-nav-item href="#">FAQ</b-nav-item>
        <b-nav-item href="#">Contact</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <nuxt />
  </div>
</template>

<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}

#page {
  height:100vh;
} 
</style>
