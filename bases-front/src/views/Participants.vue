<template>
    <v-container>
        <v-row justify="center" class="mt-3">
            <v-col cols="6">
                <v-row justify="center" class="ma-2">
                <h1 class="display-1">Personas que asistiran</h1>
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
                            <v-row justify="center">

                            </v-row>
                        </v-card-text>
                    </v-card>
                    <v-card shaped outlined class="mt-2">
                        <v-card-title>Amigos en Comun</v-card-title>
                        <v-card-text>
                            <v-list dense>
                                <div v-for="elem in fof" :key="elem.id">
                                    <div v-if="elem.id==user.user_id">
                                        <div v-if="elem.fof.length>0">
                                        <v-list-item-group v-for="aux in elem.fof" :key="aux.user_id">
                                            <v-list-item v-if="!aux.fof">
                                                <v-list-item-icon>
                                                    <v-icon>mdi-account</v-icon>
                                                </v-list-item-icon>
                                                <v-list-item-content>
                                                    <v-list-item-title>{{aux.username}}</v-list-item-title>
                                                </v-list-item-content>
                                            </v-list-item>
                                        </v-list-item-group>
                                        </div>
                                        <div v-else>
                                            <v-list-item-group>
                                                <v-list-item>
                                                    <v-list-item-content>No tienes amigos en comun
                                                    </v-list-item-content>
                                                </v-list-item>
                                            </v-list-item-group>
                                        </div>
                                    </div>
                                </div>
                            </v-list>
                        </v-card-text>
                    </v-card>
                    </v-card-text>
                </v-card>
                </div></div>
                <div v-else>
                    <v-card dark shaped>
                        <v-card-title>
                            <v-row justify="center">Todavia nadie asistira a este evento.</v-row>
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
        data() {
            return {
                user_id : localStorage.user_id,
                event_id : localStorage.event_id,
                users : [],
                fof:[]
            }
        },
        methods:{

            friendOFfriends: function(id, j) {
                console.log("entre")
                axios
                .get("/user/"+localStorage.user_id+"/friendsOfFriends/"+id)
                .then(response => {
                    let ans = response.data.detail.res
                    for( var i = 0; i< this.fof.length ; i++){
                        console.log("ans: ")
                        console.log(ans)
                        if(this.fof[i].id == this.users[j].user_id){
                            console.log(ans)
                            this.fof[i].fof = ans
                        }
                    }
                }).then()
            }

        },
        created() {
            axios
            .get("/event/"+this.event_id+"/user/"+localStorage.user_id+"/participants")
            .then(response => {
                this.users=response.data.detail.res
                for( var i = 0; i< this.users.length ; i++){
                    this.fof.push({"id":this.users[i].user_id, "fof":{}})
                }
                for( var j = 0; j< this.users.length ; j++){
                    this.friendOFfriends(this.users[j].user_id, j)
                }
            })
            
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
  .theme--dark.v-sheet[data-v-440dce4c] {
    background-color: #424242;
    border-color: #FFFFFF;
    color: #FFFFFF;
  }
</style>