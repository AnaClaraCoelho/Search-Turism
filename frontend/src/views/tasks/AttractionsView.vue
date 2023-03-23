<template>
    <v-btn
        :to="{ name: 'tasks-list' } "
    >
		<v-icon class="pr-2">
			mdi-arrow-left 
		</v-icon>
    </v-btn>
	<v-autocomplete
		label="Para onde você quer ir?"
		:items="citys"
		v-model="citySearch"
		class="mx-16"
	></v-autocomplete>
	<city-select :citySearch="citySearch" v-show="citySearch != ''"/>
</template>


<script>
import { useAppStore } from "@/stores/appStore"
import { mapState } from "pinia"
import { useAccountsStore } from "@/stores/accountsStore"
import CitySelect from './CitySelect.vue'




export default {
 name: "AtrractionsView",
 components: {CitySelect },
 setup() {
   const appStore = useAppStore()
   return { appStore }
 },
 computed: {
   ...mapState(useAccountsStore, ["loggedUser"]),
 },
 data() {
   return {
	 citys: ['Aracaju', 'Belém', 'Belo Horizonte', 'Brasília', 'Curitiba', 'Natal', 'Boa vista', 'Rio de Janeiro', 'São Paulo' ],
	 citySearch:''
   		}
	}
}
</script>
