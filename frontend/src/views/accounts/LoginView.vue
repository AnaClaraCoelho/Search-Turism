<template>
  <v-container>
    <v-row align="center" class="mt-10" no-gutters>
      <v-col cols="12" sm="6" offset-sm="3">
        <v-sheet class="pa-2"> <h1>Login</h1> </v-sheet>
        <v-form>
          <v-text-field
            v-model="username"
            label="Username"
            prepend-inner-icon="mdi-email-fast-outline"
            variant="outlined"
            required
            @keyup.enter="login"></v-text-field>

          <v-text-field
            v-model="password"
            prepend-inner-icon="mdi-key-variant"
            :append-inner-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="show1 ? 'text' : 'password'"
            name="input-10-1"
            variant="outlined"
            label="Password"
            hint="At least 8 characters"
            counter
            @click:append-inner="show1 = !show1"
            @keyup.enter="login"></v-text-field>

          <v-btn
            block
            size="large"
            rounded="pill"
            color="pink"
            append-icon="mdi-chevron-right"
            :to="{ name: 'accounts-login' }"
            @click="login">
            Login
          </v-btn>
          <v-btn
            class="my-2"
            block
            size="large"
            rounded="pill"
            color="pink"
            variant="outlined"
            :to="{ name: 'base-signup' }" >
            Sign Up
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
    const appStore = useAppStore()
    const accountsStore = useAccountsStore()
    return { appStore, accountsStore }
  },
  data: () => {
    return {
      loading: false,
      valid: false,
      username: "",
      password: "",
      error: false,
      visible: false,
      show1: false,
      rules: {
          required: value => !!value || 'Required.',
          min: v => v.length >= 8 || 'Min 8 characters',
        },
    }
  },
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  mounted() {
    console.log(this.loggedUser)
    AccountsApi.whoami().then((response) => {
      if (response.authenticated) {
        this.saveLoggedUser(response.user)
        this.appStore.showSnackbar("User alredy logged in")
        this.showTasks()
        
      }
    })
  },
  methods: {
    login() {
      this.loading = true
      AccountsApi.login(this.username, this.password)
        .then((response) => {
          if (!response) {
            this.appStore.showSnackbar("Invalid user or password")
            return
          }
          this.saveLoggedUser(response.user)
          this.showTasks()
        })
        .finally(() => {
          this.loading = false
        })
    },
    saveLoggedUser(user) {
      this.error = !user
      if (user) {
        this.accountsStore.setLoggedUser(user)
        this.visible = false
        console.log("logged")
      }
    },
    showTasks() {
      this.$router.push({ name: "tasks-list" })
      console.log("--> tasks")
    },
  },
}
</script>
