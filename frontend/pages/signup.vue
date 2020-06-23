<template>
  <div class="main">
    <h1>New User Information</h1>
    
      <b-form @submit="onSubmit">
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
            v-model="file"
            :state="Boolean(file)"
            placeholder="Choose or drop a profile picture..."
            drop-placeholder="Drop file here..."
            accept=".jpg, .png, .gif"
            @change="updateProfile"
            ></b-form-file>
          </div>
      </div>
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
      posted_img: require('../assets/icons/question.jpg'),
      first_name: '',
      last_name: '',
      email_address: '',
      user_bio: '',
      file: null
    }
  },
  methods: {
    async onSubmit() {
      axios.post('localhost:5000/signup/info', {
        first_name: this.first_name,
        last_name: this.last_name,
        email_address: this.email_address,
        user_bio: this.user_bio,
        profile_pic: this.file
      }).then((res) => {
        console.log(res)
      })
    },
    updateProfile(e) {
      const input_file = e.target.files[0]
      const reader = new FileReader()
      reader.readAsDataURL(input_file)
      reader.onload = e => {
        this.posted_img = e.target.result
        console.log(this.posted_img)
      }
    }
  }
}
</script>

<style scoped>
.main {
  height: inherit;
  text-align: center;
}

#flex_layout{
  display: flex;
}
#input_form {
  flex-grow: 5;
  padding: 2vw;
  margin:auto;
}
.circular {
  width: 20vw;
  height: 20vw;
  border-radius: 50%;
  position: relative;
  overflow: hidden;
  margin: 0 1vw;
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