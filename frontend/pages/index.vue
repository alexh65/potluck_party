<template>
  <div class="main">
    <div class="banner">
      <h1>WELCOME TO</h1>
      <img id="welcome" src="~/assets/icons/logo_mono_name.svg">
    </div>
    <div class="buttons">
      <b-button class="btn-blue">SIGN UP</b-button>
      <b-button class="btn-blue">LOGIN</b-button>
    </div>
  </div>
</template>

<script>
export default {
  layout: 'no-nav'
}
</script>

<style scoped>
h1 {
  padding: 3vh;
}
.main {
  background-color: #cd5c5c;
  height: inherit;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.banner{
  width:100%;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.buttons{
  padding-top: 2vh;
}
.btn-blue{
  background-color: #0F434F;
  color: white;
  border-color: #0F434F;
}
#welcome{
  width: 40%;
}
</style>