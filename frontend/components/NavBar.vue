<template>
  <div id="nav">
    <b-navbar type="light">
      <b-navbar-brand href="#">
        <img src="~/assets/icons/small_logo.png" width="100%">
      </b-navbar-brand>
      <b-nav-form id="search">
        <b-form-input size="sm" class="mr-sm-2" placeholder="Recipe, user, list,..."></b-form-input>
        <fa id="search" :icon="['fas', 'search']"/>
      </b-nav-form>
      <b-navbar-nav>
        <b-nav-item href="#">About</b-nav-item>
        <b-nav-item href="#">FAQ</b-nav-item>
        <b-nav-item href="#">Contact</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
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

.navbar-brand {
  width: 10vw;
  padding: 0;
}
svg{
  color: white;
}
#search{
  background-color: black;
  border-radius: 5px;
  padding-right: 5px;
}
nav input{
  margin-right: 5px;
}

</style>
