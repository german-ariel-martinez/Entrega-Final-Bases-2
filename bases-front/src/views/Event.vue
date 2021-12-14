<template>
    <v-container>
        <v-row justify="center">
            <v-col>
                <v-card shaped>
                    <v-card-title style="background-color:#424242">
                        <span style="color:white">Crear un evento</span>
                    </v-card-title>
                    <v-card-text>
                        <v-form v-model="valid" ref="form1" lazy-validation>
                            <v-row justify="center" class="mt-3">
                                <v-col>
                                    <!-- Title -->
                                    <v-text-field
                                    v-model="title"
                                    label="Ingrese su nombre"
                                    outlined
                                    :rules="textRules"
                                    clearable
                                    required
                                    ></v-text-field>
                                    <!-- descripcion -->
                                    <v-textarea
                                    v-model="description"
                                    outlined
                                    name="input-7-4"
                                    label="Descripcion"
                                    required
                                    :rules="textRules"
                                    value="Aca escribi un poco sobre vos para que los demas lo lean cuando vean tu usuario."
                                    ></v-textarea>
                                    <!-- Title -->
                                    <v-text-field
                                    v-model="location"
                                    label="Ingrese la ubicacion"
                                    outlined
                                    :rules="textRules"
                                    clearable
                                    required
                                    ></v-text-field>
                                    <!-- Date picker -->
                                    <v-card outlined shaped>
                                        <v-card-title style="background-color:#424242">
                                            <span style="color:white"> Fecha y hora</span>
                                        </v-card-title>
                                        <v-card-text class="mt-5">
                                            <v-row justify="center">
                                                <v-date-picker color="grey darken-3" class="mr-3" v-model="date"></v-date-picker>
                                                <v-time-picker
                                                    color="grey darken-3"
                                                    ampm-in-title
                                                    format="ampm"
                                                    required
                                                    scrollable
                                                    v-model="time"
                                                    :rules="[v => !!v || 'Seleccione una hora.']"
                                                ></v-time-picker>
                                            </v-row>
                                        </v-card-text>
                                    </v-card>
                                </v-col>
                            </v-row>
                            <v-row justify="center" >
                                <v-col>
                                    <v-btn v-on:click="createEvent()" class="white--text" tile block elevation="2" color="#82c7a5">
                                        Crear
                                    </v-btn>
                                </v-col>
                            </v-row>
                        </v-form>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios'
import router from '../router/index';
export default {
    data() {
        return {
            // Formularios
            valid: false,
            title:'',
            location:'',
            description:'',
            date:'',
            time:'',
            // Reglas
            textRules: [
                v => !!v || 'El campo es obligatorio.',
                v => v.length >= 3 || 'Minimo 3 caracateres.',
            ]
        }
    },
    methods:{
        createEvent: function(){
            if(this.$refs.form1.validate()){
                console.log("hola")
            }
            if(this.date==''||this.time=='')
                alert("Debe ingresar la fecha y la hora")
            console.log(this.date)
            console.log(this.time+":00")
            axios
            .post("/createvent",{
                "title": this.title,
                "date": this.date,
                "hour": this.time,
                "description": this.description,
                "location": this.location,
                "host": localStorage.user_id
                })
            .then(response => {
                console.log(response.data)
                router.push({name:'Feed'})
            })
        }
    }
}
</script>

<style>
</style>