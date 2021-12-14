<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="8">
      <v-card shaped >
        <v-card-title style="background-color:#424242">
          <span style="color:white">Informacion de cuenta</span>
        </v-card-title>
        <v-card-text class="mt-3">
          <v-card shaped outlined height="50px">
            <v-card-text>
            <v-row justify="center" align="center" class="fill-height">
              <v-col>
                <v-row justify="center">
                  <h1 class="display-1">Seguidores: {{this.followers}}</h1>
                </v-row>
              </v-col>
              <v-col>
                <v-row justify="center">
                    <h1 class="display-1">Seguiendo: {{this.following}}</h1>
                  </v-row>
              </v-col>
            </v-row>
            </v-card-text>
          </v-card>
        </v-card-text>
      </v-card>
      </v-col>
    </v-row>
    <v-row justify="center" class="mt-3">
      <!----------------------------------->
      <!--                               -->
      <!--         TUS    AMIGOS         -->
      <!--                               -->
      <!----------------------------------->
      <v-col cols="6">
        <v-row justify="center" class="ma-2">
          <h1 class="display-1">Tus amigos</h1>
        </v-row>
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
                    <v-btn @click="unfollow(user.user_id)" rounded class="ma-2 orange lighten-1" >
                      <v-icon left>
                        mdi-account-minus
                      </v-icon>
                      Eliminar
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
              <v-card shaped outlined class="mt-2">
                <v-card-title>Redes sociales</v-card-title>
                <v-card-text>
                    <v-row justify="center" align="center">
                        <v-col cols="4">
                            <v-list dense>
                                <v-list-item-group>
                                    <v-list-item>
                                        <v-list-item-icon>
                                            <v-icon>mdi-instagram</v-icon>
                                        </v-list-item-icon>
                                        <v-list-item-content>
                                            <v-list-item-title v-if="user.instagram">{{user.instagram}}</v-list-item-title>
                                            <v-list-item-title v-else>No tiene</v-list-item-title>
                                        </v-list-item-content>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-icon>
                                            <v-icon>mdi-facebook</v-icon>
                                        </v-list-item-icon>
                                        <v-list-item-content>
                                            <v-list-item-title v-if="user.facebook">{{user.facebook}}</v-list-item-title>
                                            <v-list-item-title v-else>No tiene</v-list-item-title>
                                        </v-list-item-content>
                                    </v-list-item>
                                </v-list-item-group>
                            </v-list>
                        </v-col>
                        <v-col cols="4">
                            <v-list dense>
                                <v-list-item-group>
                                    <v-list-item>
                                        <v-list-item-icon>
                                            <v-icon>mdi-twitter</v-icon>
                                        </v-list-item-icon>
                                        <v-list-item-content>
                                            <v-list-item-title v-if="user.twitter">{{user.twitter}}</v-list-item-title>
                                            <v-list-item-title v-else>No tiene</v-list-item-title>
                                        </v-list-item-content>
                                    </v-list-item>
                                    <v-list-item>
                                        <v-list-item-icon>
                                            <v-icon>mdi-linkedin</v-icon>
                                        </v-list-item-icon>
                                        <v-list-item-content>
                                            <v-list-item-title v-if="user.linkedin">{{user.linkedin}}</v-list-item-title>
                                            <v-list-item-title v-else>No tiene</v-list-item-title>
                                        </v-list-item-content>
                                    </v-list-item>
                                </v-list-item-group>
                            </v-list>
                        </v-col>
                    </v-row>
                </v-card-text>
              </v-card>
            </v-card-text>
          </v-card>
        </div>
      </v-col>
      <v-divider vertical></v-divider>
      <v-col cols="6">
        <v-row justify="center" class="ma-2">
          <h1 class="display-1">Tus eventos creados</h1>
        </v-row>
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
                    <v-btn @click="deleteEvent(event.event_id)" rounded class="ma-2 orange lighten-1" >
                      <v-icon left>
                        mdi-delete
                      </v-icon>
                      Eliminar
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
          events:[],
          followers: 0,
          following: 0,
          user_id: localStorage.user_id
      }
    },
    methods: {
      unfollow: function(id){
        console.log(id)
        axios
        .get("/user/"+this.user_id+"/unfollow/"+id)
        .then(response => {
          console.log(response)
          for(var i = 0; i< this.users.length;i++)
            if(this.users[i].user_id==id){
              this.following = this.following - 1
              this.users.splice(i,1)
            }
        })
      },
      deleteEvent: function(id){
        axios
        .delete("/event/"+id+"/user/"+this.user_id+"/delete")
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
      .get("/users/followedBy/"+this.user_id)
      .then(response => {
        this.users=response.data
      })
      axios
      .get("/myevents/"+localStorage.user_id)
      .then(response => this.events = response.data)
      axios
      .get("/countFollowers/"+localStorage.user_id)
      .then(response => this.followers = response.data.detail.qty)
      axios
      .get("/countFollowing/"+localStorage.user_id)
      .then(response => this.following = response.data.detail.qty)
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
  .theme--dark.v-sheet[data-v-7cbffb3a] {
    background-color: #424242;
    border-color: #FFFFFF;
    color: #FFFFFF;
  }
</style>
