<template>
    <v-app-bar color="indigo-lighten-5" name="app-bar" class="justify-center">
      <div class="d-flex justify-center align-center w-100">
        <span class="text-h4">Погода в интернете</span>
      </div>
    </v-app-bar>
  <v-container class="d-flex justify-center align-center flex-column">

        <v-card width="500" height="300" color="indigo-lighten-5" class="my-5" v-show="show_card">
          <v-card-title v-show="value_in_radio === 'place'">
            Погода в {{ this.name_place }}
          </v-card-title>

          <v-card-title v-show="value_in_radio === 'coords'">
            Погода по {{ this.longitude }}, {{ this.latitude }}
          </v-card-title>
            
          <v-card-item class="d-flex flex-column">
            <div class="my-2">
              <span>Температура:</span> <b>{{ inf.temp }}°</b>
            </div>

            <div class="my-2">
              <span>Ощущается как:</span> <b>{{ inf.feels_like }}°</b>
            </div>

            <div class="my-2">
              <span>Состояние:</span> <b>{{ inf.condition }}</b>
            </div>
            
            <div class="my-2">
              <span>Скорость ветра:</span> <b>{{ inf.wind_speed }}</b> м/с
            </div>
            <div class="my-2">
              <span>Время года:</span> <b>{{ inf.season }}</b>
            </div>
            <div class="my-2">
              <span>Влажность:</span> <b>{{ inf.humidity }}</b>%
            </div>

          </v-card-item>
        </v-card>

        <v-card width="500" height="300" color="indigo-lighten-5">
          <v-card-title>
            Хочу узнать погоду...
          </v-card-title>
          <v-card-item>
            <v-radio-group inline v-model="value_in_radio">
              <v-radio color="indigo" value="place" label="В месте"></v-radio>
              <v-radio color="indigo" value="coords" label="По координатам"></v-radio>
            </v-radio-group>
            <v-input>
              <v-col>
                <v-row>
                  <v-text-field label="Место" color="indigo" v-show="value_in_radio === 'place'" v-model="place"></v-text-field>

                  <v-text-field label="Долгота" color="indigo" v-show="value_in_radio === 'coords'" class="pr-2" v-model="longitude" ></v-text-field>
                  <v-text-field label="Широта" color="indigo" v-show="value_in_radio === 'coords'" class="pl-2" v-model="latitude" ></v-text-field>
                </v-row>

                <v-row>
                  <v-btn color="indigo" block @click="get_data()">Узнать</v-btn>
                </v-row>
              </v-col>


            </v-input>
          </v-card-item>
      </v-card>
  </v-container>
</template>

<script>
import axios from 'axios'


export default {
  
  data(){
    return{
      value_in_radio : '',
      place: '',
      longitude: '',
      latitude: '',
      inf: {
        temp: '', 
        wind_speed: '',
        season: '',
        humidity: '',
        condition: '',
        feels_like: ''
      },
      show_card: false,
      name_place: '',
      value_longitude: '',
      value_latitude: ''
      
    }
  },

  methods: {
    get_data(){
      this.show_card = false

      if (this.value_in_radio === 'place'){
        axios.post('http://127.0.0.1:5000/weather/api/v1.0/place',{
          name: this.place
        }).then(response => (this.inf = response.data))

        this.name_place = this.place
        this.place = ''

        this.show_card = true
      }
      else if (this.value_in_radio === 'coords'){
        axios.post('http://127.0.0.1:5000/weather/api/v1.0/long_lat',{
          long: this.longitude,
          lat: this.latitude
        }).then(response => (this.inf = response.data))

        this.value_longitude = this.longitude
        this.value_latitude = this.latitude

        this.longitude = ''
        this.latitude = ''

        this.show_card = true
      }
    }
  }
}
</script>