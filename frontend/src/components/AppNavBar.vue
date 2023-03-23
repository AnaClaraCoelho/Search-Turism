<template>
  <v-app-bar>
    <v-app-bar-title  >
        <v-btn prepend-icon="mdi-earth">
          <!-- <v-img append src="@/assets/turismo.png" /> -->
          Through the Earth

        </v-btn>
      </v-app-bar-title>
    <template #append>
      <!-- <v-btn icon="mdi-magnify"></v-btn> -->
      <v-btn
        :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
        @click.stop="themeClick"></v-btn>

      <v-btn icon="mdi-dots-vertical">
        <v-icon icon="mdi-dots-vertical" />
        <v-menu activator="parent">
          <v-list >
            <v-list-item  v-if="visible" :to="{ name: 'accounts-logout' }"  > Logout </v-list-item>
            <v-list-item v-else :to="{ name: 'accounts-login' }"  > Login </v-list-item>
          </v-list>
        </v-menu>
      </v-btn>
    </template>
  </v-app-bar>
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
    return {
      visible: false,
    }
  },
  computed: {
    ...mapState(useAccountsStore, ["loggedUser"]),
  },
  mounted() {
      AccountsApi.whoami().then((response) => {
      if (response.authenticated) {
        this.visible = true
      }
    })
    },
  methods: {
    themeClick() {
      this.$emit("themeClick")
    },
  },
}
</script>
