<template>
  <div id="app" class="md-scrollbar">

    <!-- Nav Bar -->
    <md-toolbar class="md-primary" id="nav" md-elevation="1">
      <h3 class="md-title" style="flex: 1">imatrix</h3>
      <md-button @click="homePage()">Home</md-button>
      <md-button @click="uploadPage()">Upload</md-button>
    </md-toolbar>
    
    <!-- Jumbotron -->
    <md-content v-if="this.home == true" id="jumbotron" class="md-elevation-1 md-secondary">
      <div id="title-group">
      <swapping-squares-spinner
          :animation-duration="2500"
          :size="60"
          :color="'#ff5252'"
          id="logo"
        />
      <span id="jumbotron-title" class="md-title md-display-4">
        imatrix
      </span>
      </div>
      <p id="headline" class="md-headline">
        We, here at imatrix.com, use predictive neural networks to determine the numbers 
        inside an image of a matrix a user uploads. Then, using our predictions, we calculate the determinant 
        and inverse matrix from the uploaded picture. This is a quick and fun way to do your linear algebra!
      </p>
    </md-content>

    <div v-if="this.home == true" id="section">
      <span class="md-subheading md-accent">Click the button below to upload your matrix. Then we'll evaluate it!</span> 
      <md-button @click="uploadPage()" class="md-accent md-raised">Get Started!</md-button>
    </div>

    <upload-page 
      v-if="this.upload == true" 
      @resultsMethod="resultsMethod">
    </upload-page>
    
    <results-page 
      v-if="this.results == true" 
      :resultingVals="this.resultingVals"
      @uploadPage="uploadPage">
    </results-page>
  </div>
</template>

<script>
import UploadPage from './components/UploadPage.vue'
import ResultsPage from './components/Results.vue'
import {SwappingSquaresSpinner} from 'epic-spinners'
import { throws } from 'assert';

export default {
  name: 'App',

  data: () => ({
      first: false,
      second: false,
      home: true,
      upload: false,
      results: false,
      resultingVals: ''
  }),

  methods: {
    homePage: function()
    {
      this.home = true;
      this.upload= false;
      this.results= false;
    },

    uploadPage: function()
    {
      // Erase previous stored matrix vals
      this.resultingVals = "";

      // Change view
      this.home = false;
      this.upload= true;
      this.results= false;
    },

    resultsMethod: function(vals)
    {
      this.home = false;
      this.upload = false;
      
      this.resultingVals = vals;
      
      this.results = true;
    },

  },
  components: {
    SwappingSquaresSpinner,
    UploadPage,
    ResultsPage,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

#jumbotron
{
  margin-bottom: 10px;
  padding-top: 10px;
  padding-bottom: 10px;
  text-align: center;
}

#title-group
{
  display: flex;
  justify-content: center;
  align-items: center;
}

#logo
{
  display: flex;
  flex-direction: row;
}

#jumbotron-title
{
  margin-left: 30px;
}

#headline
{
  margin-left: 16px;
  margin-right: 16px;
}

#section
{
  margin-top: 50px;
  display: flex;
  flex-direction:row;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>
