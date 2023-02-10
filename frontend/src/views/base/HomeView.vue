<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-img contain height="240" src="@/assets/earth.jpg" />

      <h1 class="text-h2 font-weight-bold" >Through the Earth </h1>
      <blockquote class="blockquote text-h5">
        &#8220;Your place to share and see the beauties of this World&#8221;
      </blockquote>

      <div class="py-6" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          
          <v-btn
          color="pink"
          min-width="228"
          rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="mr-3"
            :to="{ name: 'tasks-list' }"
            >
            <v-icon icon="mdi-web" size="large" start />
            Tourist Spots
          </v-btn>
          
          <v-btn
            v-if="loggedUser_"
            color="pink lighten-4"
            :to="{ name: 'base-signup' }" 
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="my-4 mr-3">
            <v-icon icon="mdi-speedometer" size="large" start />
            Sign-Up
          </v-btn>
          <v-btn
            v-if="loggedUser_"
            color="pink lighten-4"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            class="my-4">
            <v-icon icon="mdi-account-arrow-left-outline" size="large" start />
            Login
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import AccountsApi from "@/api/accounts.api.js"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  data: () => {
    return {
      loggedUser_: false,
    }
  },
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  mounted() {
      AccountsApi.whoami().then((response) => {
        this.loggedUser_ = true
      if (response.authenticated) {
        this.saveLoggedUser(response.user)
        
      }
    })
    },
  methods: {
    saveLoggedUser(user) {
      this.error = !user
      if (user) {
        this.visible = false
      }
    }
  },
}
</script>
