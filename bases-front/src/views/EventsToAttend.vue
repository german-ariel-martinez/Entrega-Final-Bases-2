<template>
    <v-container>
        <v-row justify="center">
            <v-col>
                <v-row justify="center" class="ma-2">
                    <h1 class="display-1">Eventos a los que asistiras</h1>
                </v-row>
                <v-row justify="center">
                    <v-col>
                        <div class="ma-5" v-for="event in events" :key="event.event_id">
                            <v-card dark shaped class="mb-2">
                                <v-card-title>
                                <v-row>
                                    <v-col>
                                    <v-row>
                                        <v-avatar size="56">
                                        <img
                                            alt="user"
                                            src="https://image.freepik.com/free-vector/group-people-illustration-set_52683-33806.jpg"
                                        >
                                        </v-avatar>
                                        <p class="ma-3">{{ event.title }} <span style="color:grey">({{event.date}})</span></p>
                                    </v-row>
                                    </v-col>
                                    <v-col>
                                    <v-row justify="end">
                                        <v-btn @click="showParticipants(event.event_id)" rounded class="ma-2" color="#82c7a5" >
                                            <v-icon left>
                                                mdi-account-group
                                            </v-icon>
                                            Ver participantes
                                        </v-btn>
                                        <v-btn @click="cancelEvent(event.event_id)" rounded class="ma-2 orange lighten-1" >
                                            <v-icon left>
                                                mdi-calendar-remove
                                            </v-icon>
                                            Cancelar asistencia
                                        </v-btn>
                                    </v-row>
                                    </v-col>
                                </v-row>
                                </v-card-title>
                                <v-card-text>
                                <v-card shaped outlined>
                                    <v-card-title>Descripción</v-card-title>
                                    <v-card-subtitle><p style="color: grey">En "{{ event.location }}", el evento comienza a la/s {{ event.hour }}</p></v-card-subtitle>
                                    <v-card-text>{{event.description}}</v-card-text>
                                </v-card>
                                </v-card-text>
                            </v-card>
                        </div>
                    </v-col>
                </v-row>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
  // Imports
  import axios from "axios"
  import router from '../router/index'
  // Codigo
  export default {
    name: 'Feed',
    data() {
      return {
          events:[],
          user_id: localStorage.user_id
      }
    },
    methods: {
      cancelEvent: function(id){
        axios
        .get("/event/"+id+"/user/"+this.user_id+"/decline")
        .then(response => {
          console.log(response)
          for(var i = 0; i< this.events.length;i++)
            if(this.events[i].event_id==id)
              this.events.splice(i,1)
        })
      },
      showParticipants: function(id){
          localStorage.event_id=id
          router.push({name:'Participants'})
      }
    },
    created(){
      axios
      .get("/user/"+localStorage.user_id+"/events")
      .then(response => this.events = response.data.detail.res)
    }
  }

</script>

<style scoped>
  @import url("https://fonts.googleapis.com/css?family=Ubuntu");
  .v-card__title + .v-card__subtitle, .v-card__title + .v-card__text {
      text-align: justify;
  }
  .theme--dark.v-sheet {
    background-color: #424242;
    border-color: #424242;
    color: #FFFFFF;
  }
  .theme--dark.v-sheet[data-v-833ad230] {
    background-color: #424242;
    border-color: #FFFFFF;
    color: #FFFFFF;
}
</style>

