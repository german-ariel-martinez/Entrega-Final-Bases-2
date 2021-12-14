<template>
  <v-container>
    <v-row justify="center">
      <!----------------------------------->
      <!--                               -->
      <!--        REGISTRAR CNTA         -->
      <!--                               -->
      <!----------------------------------->
      <v-col cols="5" >
        <v-card shaped>
          <v-card-title style="background-color:#424242">
            <span style="color:white">Registrar una cuenta</span>
          </v-card-title>
          <v-card-text>
            <v-form v-model="valid" ref="form1" lazy-validation>
            <v-row justify="center" class="mt-3">
              <v-col>
                <!-- email -->
                <v-text-field
                  v-model="email"
                  label="Ingrese su email"
                  outlined
                  :rules="emailRules"
                  clearable
                  required
                ></v-text-field>
                <!-- password -->
                <v-text-field
                  v-model="password"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show1 ? 'text' : 'password'"
                  name="input-10-1"
                  label="Ingrese su contraseña"
                  outlined
                  required
                  @click:append="show1 = !show1"
                ></v-text-field>
                <!-- username -->
                <v-text-field
                  v-model="username"
                  label="Ingrese su nombre"
                  outlined
                  :rules="textRules"
                  clearable
                  required
                ></v-text-field>
                <!-- age -->
                <v-text-field
                  v-model="age"
                  label="Ingrese su edad"
                  outlined
                  :rules="ageRules"
                  clearable
                  required
                  type="number"
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
                <!-- Redes sociales -->
                <v-row justify="center">
                  <v-col cols="5">
                    <v-text-field
                      v-model="insta"
                      label="Instagram"
                      outlined
                      clearable
                      prepend-inner-icon="mdi-instagram"
                    ></v-text-field>
                  </v-col>
                  <v-col cols="5">
                    <v-text-field
                      v-model="fb"
                      label="Facebook"
                      outlined
                      clearable
                      prepend-inner-icon="mdi-facebook"
                    ></v-text-field>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-col cols="5">
                <v-text-field
                  v-model="tw"
                  label="Twitter"
                  outlined
                  clearable
                  prepend-inner-icon="mdi-twitter"
                ></v-text-field>
              </v-col>
              <v-col cols="5">
                <v-text-field
                  v-model="link"
                  label="Linkedin"
                  outlined
                  clearable
                  prepend-inner-icon="mdi-linkedin"
                ></v-text-field>
              </v-col>
            </v-row>
            <!-- Submit -->
            <v-row justify="center" >
              <v-col>
                <v-btn :disabled="!valid" v-on:click="register()" tile block elevation="2" color="#82c7a5">
                    Registrar cuenta
                </v-btn>
              </v-col>
            </v-row>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
      <!----------------------------------->
      <!--                               -->
      <!--        INICIAR SESION         -->
      <!--                               -->
      <!----------------------------------->
      <v-col cols="5">
        <v-card shaped>
          <!-- Titulo -->
          <v-card-title style="background-color:#424242">
            <span style="color:white">Ya tengo cuenta</span>
          </v-card-title>
          <!-- Formulario -->
          <v-card-text>
            <v-row justify="center" class="mt-3">
              <v-col>
                <v-text-field
                  v-model="email"
                  label="Ingrese su email"
                  outlined
                  clearable
                ></v-text-field>
                <v-text-field
                  v-model="password"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show1 ? 'text' : 'password'"
                  name="input-10-1"
                  label="Ingrese su contraseña"
                  outlined
                  @click:append="show1 = !show1"
                ></v-text-field>
              </v-col>
            </v-row>
            <!-- Submit -->
            <v-row justify="center" >
              <v-col>
                <v-btn v-on:click="login()" class="white--text" tile block elevation="2" color="#82c7a5">
                    Iniciar sesión
                </v-btn>
              </v-col>
            </v-row>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  // Imports
  import axios from "axios"
  import { logInBus } from "../main";
  import router from '../router/index';
  // Funciones y variables
  export default {
    name: 'RegisterAndLogin',
    data() {
      return {
          // Formularios
          valid: false,
          email:'',
          password: '',
          username: '',
          sex: '',
          age: 18,
          description: '',
          insta: '',
          fb:'',
          tw:'',
          link:'',
          // Reglas de validacion
          rules: {
            required: value => !!value || 'Complete este campo.',
            min: v => v.length >= 3 || 'Minimo 3 caracteres.',
            emailMatch: () => (`The email and password you entered don't match`),
          },
          emailRules: [
              v => !!v || 'El email es obligatorio.',
              v => /.+@.+/.test(v) || 'El email ingresado no es valido.',
          ],
          textRules: [
            v => !!v || 'El campo es obligatorio.',
            v => v.length >= 3 || 'Minimo 3 caracateres.',
          ],
          ageRules: [
            v => !!v || 'El campo es obligatorio.',
            v => v >= 18 || 'Debe ser mayor a 18.',
          ],
          // Variables varias
          show1: false,
      }
    },
    methods: {
      login: function(){
        axios
        .post("/login",{"email":this.email, "password": this.password},{headers: {'Content-type': 'application/json',}})
        .then(response => {
          if(response.data.status == 1){
            localStorage.logged_in=true
            console.log('user_id='+response.data.detail.user_id)
            logInBus.$emit('logedIn', true);
            localStorage.user_id =response.data.detail.user_id
            localStorage.logged_in=true
            router.push({name:'Feed'});
          }else
            alert('Usuario o contraseña incorrectos')
        }).catch(error => {console.log(error);})
      },
      register: function(){
        if(this.$refs.form1.validate()){
          axios
          .post("/createuser",{
            "username":this.username,
            "sex": "M",
            "age": this.age,
            "description": this.description,
            "instagram": this.insta,
            "facebook": this.fb,
            "twitter": this.tw,
            "linkedin": this.link,
            "email": this.email,
            "password": this.password
          }).then(response => {
            if(response.data.status == 1){
              localStorage.user_id=response.data.detail.user_id
              localStorage.logged_in=true
              router.push({name:'Feed'});
            }else
              alert(response.data.detail.error)
          }).catch(error => {console.log(error);})
        }
          console.log("valido")
      }
    }
  }

</script>

<style scoped>


  .v-card__title + .v-card__subtitle, .v-card__title + .v-card__text {
      text-align: justify;
  }
</style>
