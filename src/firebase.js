import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/firestore'

// var f = require('firebase/auth')

// firebase init - add your own config here
const firebaseConfig = {
  apiKey: "AIzaSyCv94xsouRseVSMRYrVcBnkRThC3QSEQ2o",
  authDomain: "bt-beeary.firebaseapp.com",
  databaseURL: "https://bt-beeary-default-rtdb.firebaseio.com",
  projectId: "bt-beeary",
  storageBucket: "bt-beeary.appspot.com",
  messagingSenderId: "273450148178",
  appId: "1:273450148178:web:965b501f05582d2a9d5a8b",
  measurementId: "G-TJNBC0Z80F"
};
const f = firebase.initializeApp(firebaseConfig)

// utils
const db = firebase.firestore()
const auth = firebase.auth()

// collection references
const usersCollection = db.collection('users')
const standsCollection = db.collection('stands')
const hivesCollection = db.collection('hives')
// const likesCollection = db.collection('likes')

// export utils/refs
export {
  db,
  auth,
  usersCollection,
  standsCollection,
  hivesCollection,
//   likesCollection
}

export default f