<template>
  <div class="main">
    <h1>New User Information</h1>
    
    <b-form @submit.prevent="onSubmit">
      <div id='flex_layout'>
        <div class='circular'>
          <img :src="posted_img" alt=""/>
        </div>
        <div id='input_form'>
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
          v-model="input_file"
          :state="Boolean(input_file)"
          placeholder="Choose or drop a profile picture..."
          drop-placeholder="Drop file here..."
          accept=".jpg, .png, .gif"
          @change.prevent="updateProfile"
          ></b-form-file>
        </div>
    </div>

    <div class='login_info'>
      <b-form-input
        id='username'
        v-model='username'
        type='text'
        required
        placeholder='Username'
      ></b-form-input>
      <div class='password'>
        <b-form-input
          id='password'
          v-model='password'
          :type='fieldType'
          required
          placeholder='Password'
        ></b-form-input>
        <b-button class='btn-blue' name='toggle' @click.prevent='switchVisibility'>toggle</b-button>
      </div>
    </div>
    <b-button type="submit" class='btn-blue'>{{button_name}}</b-button>
    </b-form>
    <b-button class="btn-blue back" size="lg">
      <nuxt-link to='/'>></nuxt-link>
    </b-button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  transition: 'page',
  head() {
    return {
      title: 'PotluckParty | Sign Up'
    }
  },
  data() {
    return {
      username: '',
      password: '',
      fieldType: 'password',
      posted_img: require('../assets/icons/question.jpg'),
      first_name: '',
      last_name: '',
      email_address: '',
      user_bio: '',
      input_file: null,
      input_file_url: '',
      button_name: 'Submit'
    }
  },
  methods: {
    async onSubmit(e) {
      console.log(this.$firebase)
      //upload image to Firebase and obtain the url
      try {
        const ref = this.$firebase.storage().ref(`images/${this.username}`)
        const snapshot = await ref.put(this.input_file)
        this.input_file_url = await snapshot.ref.getDownloadURL()
      } catch(e) {
        console.log('Error uploading image', e);
      }

      console.log('Submitting user info....')
      this.$axios.post("signup/info", {
        first_name: this.first_name,
        last_name: this.last_name,
        email_address: this.email_address,
        user_bio: this.user_bio,
        profile_pic: this.input_file_url,
        username: this.username,
        password: this.password
      }).then((res) => {
        if (res.status == 200) {
          this.button_name = "Successful! Redirect to login...."
          this.$router.push('/login')
        }
      }).catch((error) => {
        console.error('Cannot submit user info')
      })
    },
    updateProfile(e) {
      this.input_file= e.target.files[0]
      console.log(this.input_file)
      const reader = new FileReader()
      reader.readAsDataURL(this.input_file)
      reader.onload = e => {
        this.posted_img = e.target.result
      }
    },
    switchVisibility(){
      this.fieldType = this.fieldType === 'password' ? 'text' : 'password'
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
#flex_layout{
  display: flex;
}
form{
  margin: auto;
  width: 85%;
}
#input_form {
  flex-grow: 5;
  padding: 2vw;
  margin:auto;
}
.login_info {
  margin-right: 2vw; 
  margin-left: 2vw;
}
.circular {
  width: 20vw;
  height: 20vw;
  border-radius: 50%;
  position: relative;
  overflow: hidden;
  margin-left: 2vw;
}
.circular img {
  min-width: 100%;
  min-height: 100%;
  width: 80%;
  height: auto;
  position: absolute;
  left: 50%;
  top: 50%;
  -webkit-transform: translate(-50%, -50%);
  -moz-transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
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

.password{
  position: relative;
  display: flex;
  flex-direction: row;
}

button[name='toggle']{
  position: absolute;
  top: 0;
  right: 0;
  margin-top:0;
}

.back {
  right: 0;
}
</style>