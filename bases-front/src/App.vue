<template>
  <v-app>
    <!-- TOOLBAR -->
    <Toolbar></Toolbar>
    <!-- Cuerpo de la pagina, usa Vue Router para cargarlo -->
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',

  data: () => ({
    //
  }),
};
</script>

<style scoped lang="scss">

    @import url("https://fonts.googleapis.com/css?family=Ubuntu");

    .v-application {
        font-family: "Ubuntu" !important;
    }

    .v-btn__content {
        color: white !important;
    }
</style>
