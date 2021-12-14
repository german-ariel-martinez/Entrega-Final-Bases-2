<template>
  <v-container>
    <v-row justify="center">
      <v-col cols=4>
        <!-- Que hacemos -->
        <v-card elevation="2" shaped class="mt-3">
          <v-card-title style="background-color:#424242; color: white">
            ¿Que hacemos?
          </v-card-title>
          <v-card-text class="mt-3">
            Nosotros somos los encargados de hacerte entrar a los mejores eventos y conocer personas unicas. De la misma manera podes publicar eventos en los cuales seas el anfitrion para hacerlos mas conocidos.
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols=4>
        <!-- Como funciona -->
        <v-card elevation="2" shaped class="mt-3">
          <v-card-title style="background-color:#424242; color: white">
            ¿Como funciona?
          </v-card-title>
          <v-card-text class="mt-3">
            ¡Es muy simple! Registra una cuenta en nuestro sitio web y completa el formulario que aparecera con tus datos. Una vez creada la cuenta podras observar que eventos estan ocurriendo a tu alrededor y con un simple click podras asistir a los mismos. De la misma manera podras ver que otros usuarios asistiran a ese evento.
          </v-card-text>
        </v-card>
      </v-col>
      <v-col cols=4>
        <!-- Conoce gente nueva -->
        <v-card elevation="2" shaped class="mt-3">
          <v-card-title style="background-color:#424242; color: white">
            Conoce gente nueva
          </v-card-title>
          <v-card-text class="mt-3 pb-1">
            <p>Cuando veas quienes asisten a un evento tambien podras ver a que personas cercanas a ti esa persona conoce, de esta forma no solo crearas temas de conversacion interesantes sino que te ayudara a expandir tus circulos de amigos. De esta forma nunca te sentiras solo en un evento de nuevo.</p>
            <p>¿Conociste a alguien nuevo? ¡Siguelo, no pierdas el contacto! </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <v-row justify="center">
      <v-col cols=8>
        <v-img
          lazy-src="https://picsum.photos/id/11/10/6"
          :src="images.como_funciona"
        ></v-img>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

  export default {
    name: 'Home',
    data() {
      return {
          images: {
              como_funciona: require('../assets/como_funciona.jpg')
          }
      }
    }
  }

</script>

<style scoped>
  .v-card__title + .v-card__subtitle, .v-card__title + .v-card__text {
      text-align: justify;
  }
</style>
