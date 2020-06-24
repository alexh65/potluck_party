import firebase from 'firebase/app'
import 'firebase/firestore'

export default ({ env, store }, inject) => {
  const firebaseConfig = {
    apiKey: 'AIzaSyCQCFkNF0-02Sm4Fv3WvnCH9GVJDkzkbAE',
    authDomain: 'potluck-party-3a15e.firebaseapp.com',
    databaseURL: 'https://potluck-party-3a15e.firebaseio.com',
    projectId: 'potluck-party-3a15e',
    storageBucket: 'potluck-party-3a15e.appspot.com',
    messagingSenderId: '156125128805',
    appId: '1:156125128805:web:5fef62db466583b4ac3e8c',
    measurementId: 'G-1VECZH2PT0'
  }

  if (!firebase.apps.length) {
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig)
  }

  inject('firebase', firebase)
}