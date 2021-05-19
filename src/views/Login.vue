<template>
  <div id="login">
    <div :class="{ 'signup-form': !showLoginForm }" class="col2">
      <form v-if="showLoginForm" @submit.prevent class="form-background">
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
<span id="displayError" ref="displayError"></span>

        <button @click="login()" class="button">Přihlásit se</button>
        <br /><br />
        <div class="extras">
          <label> Jsem tady nový </label>
          <button @click="toggleForm()" class="button">Zaregistrovat se</button>
        </div>
      </form>
      <form v-else @submit.prevent class="form-background">
        <h1>Začínáme</h1>
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

        <span id="displayError" ref="displayError"></span>
        <button @click="signup()" class="button" type="button">Zaregistrovat se</button>
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
import { EventBus } from "@/utils";

export default {
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
    };
  },
  methods: {
    toggleForm() {
      this.showLoginForm = !this.showLoginForm;
      this.$refs.displayError.innerHTML =
          "";
    },

    login() {
      this.$store
        .dispatch("login", {
          email: this.loginForm.email,
          password: this.loginForm.password,
        })
        // .then(() => );
    },
    signup() {
      const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      // return re.test(String(email).toLowerCase());
      if (!re.test(String(this.signupForm.email).toLowerCase())) {
        // alert("Email je ve špatném formátu!");
        this.$refs.displayError.innerHTML =
          "Email je ve špatném formátu";
        return;
      } else if (this.signupForm.password != this.signupForm.password2) {
        // alert("Zadaná hesla se neshodují");
        this.$refs.displayError.innerHTML =
          "Zadaná hesla se neshodují";
        return;
      } else {
        this.$store
          .dispatch("register", {
            email: this.signupForm.email,
            password: this.signupForm.password,
          })
          .catch(() => {
        
        this.$refs.displayError.innerHTML = "Email už existuje";
      })
      }
    },
  },
  mounted() {
    EventBus.$on("successfullAuth", () => {
      this.$router.push("/home")
    });
    EventBus.$on("failedRegistering", (msg) => {
      this.errorMsg = msg;
    });
    EventBus.$on("failedAuthentication", (msg) => {
      this.errorMsg = msg;
      // alert("Chybně zadaný email nebo heslo");
      this.$refs.displayError.innerHTML =
          "Chybně zadaný email nebo heslo";

    });
  },
  beforeDestroy() {
    EventBus.$off("failedRegistering");
    EventBus.$off("failedAuthentication");
  },
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
  padding-top: 150px;
  width: 100%;
  height: calc(100% - 100px);
  display: flex;
  justify-content: center;
  background-image: url(../../public/images/background_pattern_missing.svg);
  background-size: cover;
  background-position: center;
}

.form-background {
  background: #f4f4f4;
  padding: 30px;
}

label {
  margin-right: 20px;
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

#displayError {
  color: red;
}
</style>
