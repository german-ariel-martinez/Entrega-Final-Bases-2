<template>
    <v-app-bar  
        color="grey darken-3" 
        elevation="0" 
        app>

        <!-- Titulo -->
        <v-toolbar-title>
            <span @click="return_to()">Peo<span style="color:#82c7a5">pool</span>e</span>
        </v-toolbar-title>
        <!-- Separador -->
        <v-spacer></v-spacer>

        <!-- Botones -->
        <v-btn v-show="!logged_in" rounded color="#82c7a5" class="white--text" to="/register">
            <v-icon left>
                mdi-check
            </v-icon>
            ¡Registrate!
        </v-btn>
        <v-btn v-show="logged_in" rounded color="#82c7a5" class="mr-2 white--text" to="/myaccount">
            <v-icon left>
                mdi-account
            </v-icon>
            Mi cuenta
        </v-btn>
        <v-btn v-show="logged_in" rounded color="#82c7a5" class="mr-2 white--text" to="/nextEvents">
            <v-icon left>
                mdi-calendar-clock
            </v-icon>
            Proximos eventos
        </v-btn>
        <v-btn v-show="logged_in" rounded color="#82c7a5" class="mr-2 white--text" to="/event">
            <v-icon left>
                mdi-calendar
            </v-icon>
            Hostear evento
        </v-btn>
        <v-btn v-show="logged_in" @click="logout()" class="white--text" rounded color="#82c7a5" to="/">
            <v-icon left>
                mdi-logout
            </v-icon>
            Cerrar sesión
        </v-btn>
    </v-app-bar>
</template>

<script>
  // Imports
  import { logInBus } from "../main";
  import router from '../router/index';
  // Codigo
  export default {
      
    name: 'Toolbar',
    data: () => ({
      logged_in: false
    }),
    methods: {
        logout: function(){
            router.push({name:'Home'})
            this.logged_in = false
            localStorage.clear()
        },
        return_to: function(){
            if(this.logged_in)
                router.push({name:'Feed'})
            else
                router.push({name:'Home'})
        }
    },
    created(){
        logInBus.$on('logedIn', (data)=>{
            console.log("Logged-in: "+data)
            this.logged_in=localStorage.logged_in;
        })
    },
    mounted(){
        if(localStorage.logged_in)
            this.logged_in=localStorage.logged_in
    }
  }

</script>

<style scoped lang="scss">
    @import url("https://fonts.googleapis.com/css?family=Ubuntu");

    .v-toolbar__title {
        font-size: 2rem !important;
        color: white;
        font-family: 'Ubuntu' !important;
    }

    .v-btn {
        text-transform: none !important;
        font-family: 'Ubuntu' !important;
    }

</style>
