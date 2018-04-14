<template>
  <div id="app">
    <img src="./assets/logo.png">
    <HelloWorld/>
    <semipolar-spinner
          :animation-duration="2000"
          :size="610"
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
  margin-top: 60px;
}
</style>
