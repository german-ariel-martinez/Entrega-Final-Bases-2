<template>
  <v-container fluid>
    <v-row justify="center" class="mt-3">
      <!----------------------------------->
      <!--                               -->
      <!--        CONOCER  GENTE         -->
      <!--                               -->
      <!----------------------------------->
      <v-col cols="6">
        <v-row justify="center" class="ma-2">
          <h1 class="display-1">Conocer gente</h1>
        </v-row>
        <div v-if="users.length>0">
        <div class="ma-5" v-for="user in users" :key="user.user_id">
          <v-card dark shaped class="mb-2">
            <v-card-title>
              <v-row>
                <v-col>
                  <v-row>
                    <v-avatar size="56">
                      <img
                        alt="user"
                        src="https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg"
                      >
                    </v-avatar>
                    <p class="ma-3">{{ user.username }} <span style="color: grey">({{ user.sex }}-{{ user.age }})</span></p>
                  </v-row>
                </v-col>
                <v-col>
                  <v-row justify="end">
                    <v-btn @click="follow(user.user_id)" class="ma-2" rounded color="#82c7a5">
                      <v-icon left>
                        mdi-account-plus
                      </v-icon>
                      Seguir
                    </v-btn>
                  </v-row>
                </v-col>
              </v-row>
            </v-card-title>
            <v-card-text>
              <v-card shaped outlined>
                <v-card-title>Descripción</v-card-title>
                <v-card-text>{{user.description}}</v-card-text>
              </v-card>
            </v-card-text>
          </v-card>
        </div>
        </div>
        <div v-else>
            <v-card dark shaped>
                <v-card-title>
                    <v-row justify="center">Todavia no hay usuarios registrados.</v-row>
                </v-card-title>
            </v-card>
        </div>
      </v-col>
      <v-divider vertical></v-divider>
      <v-col cols="6">
        <v-row justify="center" class="ma-2">
          <h1 class="display-1">Eventos</h1>
        </v-row>
        <div v-if="events.length>0">
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
                    <v-btn @click="attendEvent(event.event_id)" class="ma-2" rounded color="#82c7a5">
                      <v-icon left>
                        mdi-calendar-check
                      </v-icon>
                      Asistir
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
        </div>
        <div v-else>
            <v-card dark shaped>
                <v-card-title>
                    <v-row justify="center">Todavia no hay eventos disponibles.</v-row>
                </v-card-title>
            </v-card>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  // Imports
  import axios from "axios"
  // import router from '../router/index'
  // Codigo
  export default {
    name: 'Feed',
    data() {
      return {
          users: [],
          events: [],
          user_id: localStorage.user_id
      }
    },
    methods: {
      follow: function(id){
        console.log(id)
        axios
        .get("/user/"+this.user_id+"/follow/"+id)
        .then(response => {
          console.log(response)
          for(var i = 0; i< this.users.length;i++)
            if(this.users[i].user_id==id)
              this.users.splice(i,1)
        })
        
      },
      attendEvent(id){
        axios
        .post("/event/"+id+"/user/"+this.user_id+"/attend",{"user_id":localStorage.user_id, "event_id": id, "status": 1})
        .then(response => {
          console.log(response)
          for(var i = 0; i< this.events.length;i++)
            if(this.events[i].event_id==id)
              this.events.splice(i,1)
        })
      }
    },
    created(){  
      axios
      .get("/users/notfollowing/"+this.user_id)
      .then(response => {
        this.users=response.data
      })
      axios
      .get("/events/"+localStorage.user_id)
      .then(response =>{console.log(response.data); this.events = response.data.detail.res})
    }
  }

</script>

<style scoped>
  .v-card__title + .v-card__subtitle, .v-card__title + .v-card__text {
      text-align: justify;
  }
  .theme--dark.v-sheet {
    background-color: #424242;
    border-color: #424242;
    color: #FFFFFF;
  }
  .theme--dark.v-sheet[data-v-d7d0cc50] {
    background-color: #424242;
    border-color: #FFFFFF;
    color: #FFFFFF;
  }
</style>
