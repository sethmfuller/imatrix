<template>
  <div id="app" class="md-scrollbar">
    
    <!-- Nav -->
    <!-- <md-tabs class="md-primary" md-alignment="right">
      <md-tab id="tab-home" md-label="Home"></md-tab>
      <md-tab id="tab-pages" md-label="Upload"></md-tab>
      <md-tab id="tab-posts" md-label="History"></md-tab>
    </md-tabs> -->

    <!-- Nav Bar -->
    <md-toolbar class="md-primary" md-elevation="1">
      <h3 class="md-title" style="flex: 1">imatrix</h3>
      <md-button>Home</md-button>
      <md-button>Upload</md-button>
      <md-button>History</md-button>
    </md-toolbar>
    
    <!-- Jumbotron -->
    <md-content id="jumbotron" class="md-elevation-1 md-secondary">
      <span id="jumbotron-title" class="md-title md-display-4">imatrix</span>
      <p id="headline" class="md-headline">We, here at imatrix.com, use predictive neural networks to determine the numbers 
        inside an image of a matrix a user uploads. Then, using our predictions, we calculate the determinant 
        and inverse matrix from the uploaded picture. This is a quick and fun way to do your linear algebra!
      </p>
    </md-content>

    <md-dialog-alert
      :md-active.sync="first"
      md-content="Your post has been deleted!"
      md-confirm-text="Cool!" />

    <md-dialog-alert
      :md-active.sync="second"
      md-title="Post created!"
      md-content="Your post <strong>Material Design is awesome</strong> has been created." />

    <md-button class="md-accent md-raised">Upload</md-button>

    <!-- <md-button class="md-accent md-raised" @click="first = true">Alert</md-button>
    <md-button class="md-primary md-raised" @click="second = true">Alert</md-button> -->

    


    <!-- <md-button class="md-icon-button md-raised md-primary">
        <md-icon>thumb_up</md-icon>
    </md-button> -->

    <!-- Accent Button
    <md-button class="md-icon-button md-raised md-accent">
        <md-icon>thumb_down</md-icon>
    </md-button> -->

    <!-- Primary button -->
    <!-- <md-button class="md-fab md-primary">
        <md-icon>add</md-icon>
    </md-button> -->

    <!-- Spinner -->
    <!-- <semipolar-spinner
          :animation-duration="2000"
          :size="60"
          :color="'#ff5252'"
     /> -->

     <!-- <md-field>
      <label>Upload Matrix Image</label>
      <md-file v-model="single" accept="image/*" />
    </md-field> -->
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld'
import {AtomSpinner, 
        FlowerSpinner, 
        HollowDotsSpinner, 
        IntersectingCirclesSpinner, 
        OrbitSpinner, 
        TrinityRingsSpinner, 
        CirclesToRhombusesSpinner,
        SelfBuildingSquareSpinner,
        FulfillingBouncingCircleSpinner,
        FingerprintSpinner,
        BreedingRhombusSpinner,
        SpringSpinner,
        SemipolarSpinner} from 'epic-spinners'

export default {
  name: 'App',

  data: () => ({
      first: false,
      second: false
  }),

  components: {
    HelloWorld,
    AtomSpinner,
    FlowerSpinner,
    HollowDotsSpinner,
    IntersectingCirclesSpinner,
    OrbitSpinner,
    TrinityRingsSpinner,
    CirclesToRhombusesSpinner,
    SelfBuildingSquareSpinner,
    FulfillingBouncingCircleSpinner,
    FingerprintSpinner,
    BreedingRhombusSpinner,
    SpringSpinner,
    SemipolarSpinner
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

#jumbotron-title
{
  margin-left: 16px;
  flex-grow: 1;
}

#headline
{
  margin-left: 16px;
  margin-right: 16px;
}
</style>
