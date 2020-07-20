<template>
  <div class='main'>
    <h1>Login</h1>
    <b-form @submit.prevent="onSubmit">
      <b-form-input
        id='username'
        v-model='username'
        required
        placeholder='Username'
      ></b-form-input>
      <b-form-input
        id='password'
        v-model='password'
        type='password'
        required
        placeholder='Password'
      ></b-form-input>
      <b-button type="submit" class='btn-blue'>This is the start of your culinary journey...</b-button>
    </b-form>
    
    <b-button class="btn-blue back" size="lg">
      <nuxt-link to='/'> &lt; </nuxt-link>
    </b-button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  layout: 'no-nav',
  data(){
    return {
      username:'',
      password:''
    }
  },
  head() {
    return {
      title: 'PotluckParty | Login'
    }
  },
  methods: {
    async onSubmit(){
      axios.post('http://localhost:5000/login', {
        username: this.username,
        password: this.password
      }).then((res) => {
        console.log(res)
      }).catch((error) => {
        console.error('Cannot login')
      })
    }
  }
}
</script>

<style scoped>
h1{
  background-color: black;
  color: white;
  padding: 10px;
}
form {
  width: 50%;
  margin: auto;
}

input {
  margin: 10pt;
}

a {
  color: white;
}
</style>