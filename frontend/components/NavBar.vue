<template>
  <div id="nav">
    <b-navbar type="light">
      <b-navbar-nav>
        <b-navbar-brand href="#">
          <img src="~/assets/icons/small_logo.png" width="100%">
        </b-navbar-brand>
        <b-nav-form id="stuff">
          <div id="search">
            <b-form-input size="md" class="mr-sm-2" placeholder="Recipe, user, list,..."></b-form-input>
            <fa id="search" :icon="['fas', 'search']"/>
          </div>
          <b-nav-item-dropdown text="Hello, lexotterly!" right>
            <b-dropdown-item href="#">Profile</b-dropdown-item>
            <b-dropdown-item href="#">Saved</b-dropdown-item>
            <b-dropdown-item href="#">Settings</b-dropdown-item>
            <div class="dropdown-divider"></div>
            <b-dropdown-item href="#">Log Out</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-nav-form>
      </b-navbar-nav>
    </b-navbar>
  </div>
</template>

<style>

a{
  color: black;
}
.b-nav-item-dropdown{
  position: static;
  float: right;
}

#search{
  background-color: black;
  border-radius: 5px;
  padding-right: 5px;
}
#search input[type="text"]{
  width: 35vw;
}
li.form-inline{
  width: 100%;
  font-weight: bold;
}
svg{
  color: white;
}
nav input{
  margin-right: 5px;
}
.b-nav-dropdown{
  position: absolute;
  right: 10px;
}
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

.navbar-nav{
  width: 100%;
}
</style>
