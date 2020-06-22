<template>
  <div class="main">
    <h1>New User Information</h1>
    <b-form @submit="onSubmit">
      <b-form-row>
        <b-col>
          <b-form-input
            id='first_name'
            v-model='first_name'
            required
            placeholder='First name'
          ></b-form-input>
       </b-col>
        <b-col>
          <b-form-input
            id='last_name'
            v-model='last_name'
            placeholder='Last name'
          ></b-form-input>
        </b-col>
      </b-form-row>
        
      <b-form-input
        id='email_address'
        v-model='email_address'
        type='email'
        required
        placeholder='Email address'
      ></b-form-input>

      <b-form-textarea
        id='user_bio'
        v-model='user_bio'
        placeholder='Bio - show us your personality :)'
        rows='5'
      ></b-form-textarea>

      <b-form-file
      v-model="file"
      :state="Boolean(file)"
      placeholder="Choose or drop a profile picture..."
      drop-placeholder="Drop file here..."
      accept=".jpg, .png, .gif"
    ></b-form-file>

    <b-button>
      <nuxt-link to='/'>Go Back</nuxt-link>
    </b-button>
    <b-button type="submit" class='btn-blue'>Next</b-button>
    
    </b-form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  layout: 'no-nav',
  data() {
    return {
      first_name: '',
      last_name: '',
      email_address: '',
      user_bio: '',
      profile_pic: null
    }
  },
  methods: {
    onSubmit() {
      
    }
  }
}
</script>

<style scoped>
.main {
  height: inherit;
  text-align: center;
}

form {
  width:80%;
  display: inline-block;
}

input {
  margin-bottom: 10px;
}
textarea {
  margin-bottom: 10px;
}

button {
  margin-top: 10px;
}
a {
  color: white;
}

.btn-blue {
  background-color: #0F434F;
  color: white;
  border-color: #0F434F;
}
.btn-blue:hover {
  background-color: #092b33;
  color: white;
  border-color: #092b33;
}
</style>