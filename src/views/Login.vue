<template>
  <div id="login">
    <!-- <PasswordReset v-if="showPasswordReset" @close="togglePasswordReset()"></PasswordReset> -->
    <section>
      <div :class="{ 'signup-form': !showLoginForm }" class="col2">
        <form v-if="showLoginForm" @submit.prevent>
          <h1>Vítejte zpět</h1>
          <div>
            <label for="email1">Email </label>
            <input v-model.trim="loginForm.email" type="text" placeholder="maja@email.cz" id="email1" />
          </div>
          <div>
            <label for="password1">Heslo </label>
            <input v-model.trim="loginForm.password" type="password" placeholder="******" id="password1" />
          </div>
          <button @click="login()" class="button">Přihlásit se</button>
          <br><br>
          <div class="extras">
            <!-- <a @click="togglePasswordReset()">Forgot Password</a> -->
            <label> Jsem tady nový </label>
            <button @click="toggleForm()" class="button">Zaregistrovat se</button>
          </div>
        </form>
        <form v-else @submit.prevent>
          <h1>Začínáme</h1>
          <div>
            <label for="name">Jméno </label>
            <input v-model.trim="signupForm.name" type="text" placeholder="Včelka Mája" id="name" />
          </div>
          <div>
            <label for="email2">Email </label>
            <input v-model.trim="signupForm.email" type="text" placeholder="maja@email.cz" id="email2" />
          </div>
          <div>
            <label for="password2">Heslo </label>
            <input v-model.trim="signupForm.password" type="password" placeholder="******" id="password2" />
          </div>
          <button @click="signup()" class="button">Zaregistrovat se</button>
          <br><br>
          <div class="extras">
            <label> Už mám účet </label>
            <button @click="toggleForm()" class="button">Zpátky k přihlášení</button>
          </div>
        </form>
      </div>
    </section>
  </div>
</template>

<script>
// import PasswordReset from '@/components/PasswordReset'
export default {
  // components: {
  //   PasswordReset
  // },
  data() {
    return {
      loginForm: {
        email: '',
        password: ''
      },
      signupForm: {
        name: '',
        // title: '',
        email: '',
        password: ''
      },
      showLoginForm: true,
      // showPasswordReset: false
    }
  },
  methods: {
    toggleForm() {
      this.showLoginForm = !this.showLoginForm
    },
    // togglePasswordReset() {
    //   this.showPasswordReset = !this.showPasswordReset
    // },
    login() {
      this.$store.dispatch('login', {
        email: this.loginForm.email,
        password: this.loginForm.password
      })
    },
    signup() {
      this.$store.dispatch('signup', {
        email: this.signupForm.email,
        password: this.signupForm.password,
        name: this.signupForm.name,
        // title: this.signupForm.title
      })
    }
  }
}
</script>

<style scoped>
*{
  margin:0;
  padding:0;

}

body{
  font:15px/1.3 'Open Sans', sans-serif;
  color: #5e5b64;
  text-align:left;
}

div{
  margin-bottom: 10px;
}
h1 {
  margin-bottom: 20px;
}


section, footer, header, aside, nav{
  display: block;
}

/*-------------------------
  The menu
--------------------------*/

button{
  display:inline-block;
  padding: 10px 22px;
  color:rgb(0, 0, 0) !important;
  font-weight:bold;
  font-size:14px;
  text-decoration:none !important;
  line-height:1;
  text-transform: uppercase;
  background-color:#FF8181;

  -webkit-transition:background-color 0.25s;
  -moz-transition:background-color 0.25s;
  transition:background-color 0.25s;
}

button:hover {
  background-color: #FFCACA; /* #fadb6a nice light yellow */
}


p{
  font-size:22px;
  font-weight:bold;
  color:#7d9098;
}

p b{
  color:#ffffff;
  display:inline-block;
  padding:5px 10px;
  background-color:#c4d7e0;
  border-radius:2px;
  text-transform:uppercase;
  font-size:18px;
}
.resource {
  margin: 20px 0;
}
</style>