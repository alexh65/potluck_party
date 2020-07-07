<template>
  <div class="main">
    <div class="banner">
      <h1>WELCOME TO</h1>
      <img id="welcome" src="~/assets/icons/logo_mono_name.svg">
    </div>
    <p>A simple tool to share your recipe to the whole wide world</p>
    <div class="buttons">
      <b-button class="btn-blue" size="lg">
        <nuxt-link to='/signup'>
        SIGN UP</nuxt-link>
        </b-button>
      <b-button class="btn-blue" size="lg"><nuxt-link to='/login'>
        LOGIN</nuxt-link></b-button>
    </div>
  </div>
</template>

<script>
export default {
  layout: 'no-nav',
  head() {
    return {
      title: 'PotluckParty | Home'
    }
  }
}
</script>

<style scoped>
h1 {
  padding: 3vh;
}
p{
  padding: 2vh;
  font-size: 2vw;
}
.main {
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
a {
  color: white;
}

#welcome{
  width: 40%;
}


</style>