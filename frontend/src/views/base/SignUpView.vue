<template>
  <v-container>
    <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Sign Up</h1> </v-sheet>
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation>
          <v-text-field
            v-model="username"
            label="Username"
            :counter="14"
            :rules="usernameRules"
            prepend-inner-icon="mdi-account-multiple"
            variant="outlined"
            required
            @keyup.enter="login"></v-text-field>

            <v-text-field
            v-model="email"
            label="E-Mail"
            :rules="emailRules"
            prepend-inner-icon="mdi-email-fast-outline"
            variant="outlined"
            required
            @keyup.enter="login"></v-text-field>

            <v-text-field
            v-model="password"
            type="password"
            label="Password"
            :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            prepend-inner-icon="mdi-key-outline"
            variant="outlined"
            @click:append-inner="changeIcon"
            required
            @keyup.enter="login"></v-text-field>

          <v-text-field
            v-model="confirm_password"
            type="password"
            label="Confirm Password"
            :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            prepend-inner-icon="mdi-key-outline"
            variant="outlined"
            @click:append-inner="changeIcon"
            required
            @keyup.enter="login"></v-text-field>

          <v-btn
            block
            size="large"
            rounded="pill"
            color="primary"
            append-icon="mdi-chevron-right"
            :to="{ name: 'base-signup' } "
            >
            Sign Up
            
          </v-btn>

          
          <v-btn
          class="my-2"
            block
            size="large"
            rounded="pill"
            color="primary"
            variant="outlined"
            append-icon="mdi-home"
            :to="{ name: 'base-home' }" 
            >
            Inicio
          </v-btn>

        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import AccountsApi from "@/api/accounts.api.js"
import { useAppStore } from "@/stores/appStore"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  setup() {
  },
  data: () => {
    return {
      loading: false,
      valid: true,
      showPassword: false,
      username: "",
      usernameRules: [
        v => !!v || 'Username is required',
        v => (v && v.length <= 14) || 'Username must be less than 14 characters',
      ],
      password: "",
      email:"",
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+\..+/.test(v) || 'E-mail must be valid',
      ],
      confirm_password:"",
      passwordRules: [
      v => !!v || 'Senha é obrigatória',
      ],
      confirmPasswordRules: [
      v => !!v || 'Confirme a senha',
      v => v === this.password || 'Senhas não coincidem'],
      error: false,
      visible: false,
    }
  },
  computed: {
  },
  mounted() {
  },
  methods: {
    toggleMarker () {
        this.showPassword = !this.showPassword
    },
    login() {
    },
    saveLoggedUser(user) {
      }
    },
    showTasks() {
    }
}
</script>

<style>
  .ajuste{
    margin-top: 2px;
  }
</style>