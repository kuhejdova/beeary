<template>
  <div id="login">
    <div :class="{ 'signup-form': !showLoginForm }" class="col2">
      <form v-if="showLoginForm" @submit.prevent>
        <h1>Vítejte zpět</h1>
        <div class="input-text">
          <label for="email1">Email </label>
          <input
            v-model.trim="loginForm.email"
            type="text"
            placeholder="maja@email.cz"
            id="email1"
          />
        </div>
        <div class="input-text">
          <label for="password1">Heslo </label>
          <input
            v-model.trim="loginForm.password"
            type="password"
            placeholder="******"
            id="password1"
          />
        </div>
        <button @click="login()" class="button">Přihlásit se</button>
        <br /><br />
        <div class="extras">
          <!-- <a @click="togglePasswordReset()">Forgot Password</a> -->
          <label> Jsem tady nový </label>
          <button @click="toggleForm()" class="button">Zaregistrovat se</button>
        </div>
      </form>
      <form v-else @submit.prevent>
        <h1>Začínáme</h1>
        <!-- <div class="input-text">
          <label for="name">Jméno </label>
          <input
            v-model.trim="signupForm.name"
            type="text"
            placeholder="Včelka Mája"
            id="name"
          />
        </div> -->
        <div class="input-text">
          <label for="email2">Email </label>
          <input
            v-model.trim="signupForm.email"
            type="text"
            placeholder="maja@email.cz"
            id="email2"
          />
        </div>
        <div class="input-text">
          <label for="password2">Heslo </label>
          <input
            v-model.trim="signupForm.password"
            type="password"
            placeholder="******"
            id="password2"
          />
        </div>
        <div class="input-text">
          <label for="password3">Heslo znovu </label>
          <input
            v-model.trim="signupForm.password2"
            type="password"
            placeholder="******"
            id="password3"
          />
        </div>
        <button @click="signup()" class="button">Zaregistrovat se</button>
        <br /><br />
        <div class="extras">
          <label> Už mám účet </label>
          <button @click="toggleForm()" class="button">
            Přihlásit se
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
// import * as fb from "../firebase";
import { EventBus } from "@/utils";

// import PasswordReset from '@/components/PasswordReset'
export default {
  // components: {
  //   PasswordReset
  // },
  data() {
    return {
      loginForm: {
        email: "",
        password: "",
      },
      signupForm: {
        email: "",
        password: "",
        password2: "",
      },
      showLoginForm: true,
      errorMsg: "",
      // showPasswordReset: false
    };
  },
  methods: {
    toggleForm() {
      this.showLoginForm = !this.showLoginForm;
    },

    login() {
      this.$store
        .dispatch("login", {
          email: this.loginForm.email,
          password: this.loginForm.password,
        })
        .then(() => this.$router.push("/home"));
    },
    signup() {
      if (this.signupForm.password != this.signupForm.password2) {
        alert("Zadaná hesla se neshodují");
      } else {
        this.$store
          .dispatch("register", {
            email: this.signupForm.email,
            password: this.signupForm.password,
          })
          .then(() => this.$router.push("/home"));
      }
    },
    // signup() {
    //   localStorage.removeItem("userData");

    //   this.$store.dispatch("signup", {
    //     email: this.signupForm.email,
    //     password: this.signupForm.password,
    //     name: this.signupForm.name,
    //   });
    // },
  },
  mounted() {
    EventBus.$on("failedRegistering", (msg) => {
      this.errorMsg = msg;
    });
    EventBus.$on("failedAuthentication", (msg) => {
      this.errorMsg = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off("failedRegistering");
    EventBus.$off("failedAuthentication");
  },
  // methods: {
  //   toggleForm() {
  //     this.showLoginForm = !this.showLoginForm;
  //   },
  //   // togglePasswordReset() {
  //   //   this.showPasswordReset = !this.showPasswordReset
  //   // },

  //   async login() {

  //   },

  //   async login() {
  //     const { user } = await fb.auth.signInWithEmailAndPassword(
  //       this.loginForm.email,
  //       this.loginForm.password
  //     );

  //     localStorage.setItem("user", user);

  //     const userProfile = await fb.usersCollection.doc(user.uid).get();
  //     localStorage.setItem("userProfile", userProfile);

  //     this.$store.dispatch("login", {
  //       email: this.loginForm.email,
  //       password: this.loginForm.password,
  //     });
  //   },
  //   signup() {
  //     localStorage.removeItem("user");

  //     this.$store.dispatch("signup", {
  //       email: this.signupForm.email,
  //       password: this.signupForm.password,
  //       name: this.signupForm.name,
  //     });
  //   },
  // },
};
</script>

<style scoped>
* {
  margin: 0;
}

body {
  font: 15px/1.3 "Open Sans", sans-serif;
  color: #5e5b64;
  text-align: left;
}

#login {
  margin-top: 150px;
  width: 100%;
  display: flex;
  justify-content: center;
}

label,
.input-text {
  display: flex;
  align-self: center;
  justify-content: space-between;
}

.extras {
  display: flex;
  justify-content: space-between;
}

div {
  margin-bottom: 10px;
}
h1 {
  margin-bottom: 20px;
}

footer,
header,
aside,
nav {
  display: block;
}

p {
  font-size: 22px;
  font-weight: bold;
  color: #7d9098;
}

p b {
  color: #ffffff;
  display: inline-block;
  padding: 5px 10px;
  background-color: #c4d7e0;
  border-radius: 2px;
  text-transform: uppercase;
  font-size: 18px;
}
.resource {
  margin: 20px 0;
}
</style>
