<template>
  <div id="app">
    <md-tabs class="md-primary" md-alignment="right">
      <md-tab id="tab-home" md-label="Home"></md-tab>
      <md-tab id="tab-pages" md-label="Pages"></md-tab>
      <md-tab id="tab-posts" md-label="Posts"></md-tab>
      <md-tab id="tab-favorites" md-label="Favorites"></md-tab>
    </md-tabs>

    <md-content class="md-elevation-1" style="width: 10%;">Wow</md-content>


    <md-button class="md-icon-button md-raised md-primary">
        <md-icon>thumb_up</md-icon>
    </md-button>

    <!-- Accent Button -->
    <md-button class="md-icon-button md-raised md-accent">
        <md-icon>thumb_down</md-icon>
    </md-button>

    <!-- Primary button -->
    <md-button class="md-fab md-primary">
        <md-icon>add</md-icon>
    </md-button>

    <!-- Spinner -->
    <semipolar-spinner
          :animation-duration="2000"
          :size="60"
          :color="'#2c3e50'"
     />
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
  text-align: center;
  color: #2c3e50;
}
</style>
