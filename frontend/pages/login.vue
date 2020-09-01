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
    async onSubmit(info){
      
      try{
        //first arg: name of oauth strategy
        //second arg: a hash; data is the most important part of the hash
        let response = await this.$auth.loginWith('local', {
                        data: {
                          username: this.username,
                          password: this.password
                        }
                     })
        this.$router.push('/')
      } catch (err) {
        console.log(err)
      }
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
  width: 60%;
  margin: auto;
}
input{
  margin-top: 10pt;
  margin-bottom: 10pt;
}
a {
  color: white;
}
</style>