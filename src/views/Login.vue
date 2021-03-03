<template>
  <div id="login">
    <!-- <PasswordReset v-if="showPasswordReset" @close="togglePasswordReset()"></PasswordReset> -->
    <section>
      <div class="col1">
        <h1>Beeary</h1>
        <p>Webová aplikace pro všechny včelaře. Ovládněte včelařství.</p>
      </div>
      <div :class="{ 'signup-form': !showLoginForm }" class="col2">
        <form v-if="showLoginForm" @submit.prevent>
          <h1>Vítejte zpět</h1>
          <div>
            <label for="email1">Email</label>
            <input v-model.trim="loginForm.email" type="text" placeholder="you@email.com" id="email1" />
          </div>
          <div>
            <label for="password1">Heslo</label>
            <input v-model.trim="loginForm.password" type="password" placeholder="******" id="password1" />
          </div>
          <button @click="login()" class="button">Přihlásit se</button>
          <div class="extras">
            <!-- <a @click="togglePasswordReset()">Forgot Password</a> -->
            <a @click="toggleForm()">Zaregistrovat se</a>
          </div>
        </form>
        <form v-else @submit.prevent>
          <h1>Začínáme</h1>
          <div>
            <label for="name">Jméno</label>
            <input v-model.trim="signupForm.name" type="text" placeholder="Savvy Apps" id="name" />
          </div>
          <!-- <div>
            <label for="title">Title</label>
            <input v-model.trim="signupForm.title" type="text" placeholder="Company" id="title" />
          </div> -->
          <div>
            <label for="email2">Email</label>
            <input v-model.trim="signupForm.email" type="text" placeholder="you@email.com" id="email2" />
          </div>
          <div>
            <label for="password2">Heslo</label>
            <input v-model.trim="signupForm.password" type="password" placeholder="min 6 characters" id="password2" />
          </div>
          <button @click="signup()" class="button">Zaregistrovat se</button>
          <div class="extras">
            <a @click="toggleForm()">Zpátky k přihlášení</a>
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