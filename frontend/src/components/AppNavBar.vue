<template>
  <v-app-bar>
    <v-app-bar-title>
        <v-btn>
          <!-- <v-img append src="@/assets/turismo.png" /> -->
        
          <v-app-bar-title v-if="!loggedUser" :to="{ name: 'base-home '}"> Search Tourism </v-app-bar-title>
          <v-app-bar-title v-else> Search Tourism </v-app-bar-title>

        </v-btn>
      </v-app-bar-title>
    <template #append>
      <!-- <v-btn icon="mdi-magnify"></v-btn> -->
      <v-btn
        :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
        @click.stop="themeClick"></v-btn>

      <v-btn v-if="loggedUser" icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list >
            <v-list-item :to="{ name: 'accounts-logout' }"  > Logout </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
      <v-btn v-else icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list >
            <v-list-item :to="{ name: 'accounts-login' }"  > Login </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </template>
  </v-app-bar>
</template>

<script>
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"

export default {
  props: {
    title: {
      type: String,
      required: false,
      default: "Search Turism",
    },
    theme: {
      type: String,
      required: true,
      default: "dark",
    },
  },
  emits: ["themeClick"],
  data: () => {
    return {}
  },
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
  },
}
</script>
