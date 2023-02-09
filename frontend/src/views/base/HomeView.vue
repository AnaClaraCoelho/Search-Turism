<template>
  <v-container class="fill-height">
    <v-responsive class="d-flex align-center text-center fill-height">
      <v-img contain height="240" src="@/assets/turismo.png" />

      <h1 class="text-h2 font-weight-bold" >Search Tourism</h1>
      <code>Vue3 + Vuetify + Vite</code>

      <div class="py-6" />

      <v-row class="d-flex align-center justify-center">
        <v-col cols="auto">
          <v-btn
            v-if="!loggedUser"
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
            color="pink"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            class="ml-3"
            :to="{ name: 'tasks-list' }"
            >
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Tasks
          </v-btn>

          <v-btn
            v-if="!loggedUser"
            color="pink lighten-4"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-login' }"
            class="my-4">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Login
          </v-btn>

          <v-btn
            v-else
            color="pink"
            min-width="228"
            rel="noopener noreferrer"
            size="x-large"
            variant="flat"
            :to="{ name: 'accounts-logout' }"
            class="ml-3">
            <v-icon icon="mdi-account-arrow-right-outline" size="large" start />
            Logout
          </v-btn>
        </v-col>
      </v-row>
    </v-responsive>
  </v-container>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
}
</script>
