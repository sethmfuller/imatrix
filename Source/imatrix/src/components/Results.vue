<template>
    <div id="results">
        <!-- <md-button class="md-accent md-raised" @click="first = true">Alert</md-button>
    <md-button class="md-primary md-raised" @click="second = true">Alert</md-button> -->
    <h2 class="md-display-1" id="results-title">Computed Results</h2>
        <div id="card-container">
            <md-content class="md-elevation-1 card top-cards ">
                <img id="uploaded-image" class="md-elevation-3" src="../assets/matrix.jpg" alt="matrix" width="200px" height="200px">
                <h3>Uploaded Matrix</h3>
            </md-content>

            <md-content class="md-elevation-1 card top-cards">
                <img id="uploaded-image" class="md-elevation-3" src="../assets/matrix.jpg" alt="matrix" width="200px" height="200px">
                <h3>Predicted Matrix</h3>
                <div>
                    <md-button class="md-icon-button md-raised md-primary">
                        <md-icon>thumb_up</md-icon>
                        <md-tooltip md-direction="bottom">Correct Prediction</md-tooltip>
                    </md-button>

                    <md-button class="md-icon-button md-raised md-accent" @click="showSnackbar = true">
                        <md-icon>thumb_down</md-icon>
                        <md-tooltip md-direction="bottom">Incorrect Prediction</md-tooltip>
                    </md-button>
                </div>
            </md-content>
        </div>

        <div id="card-container">
            <md-content id="results-container" class="md-elevation-1 card bottom-cards">
                <div class="results-containers-small">
                    <h3>Determinant</h3>
                    <span class="md-display-4">{{this.resultingVals.determinant}}</span>
                </div>
                <div class="results-containers-small">
                    <img id="uploaded-image" class="md-elevation-3" src="../assets/matrix.jpg" alt="matrix" width="200px" height="200px">
                    <h3>Inverse Matrix</h3>
                </div>
            </md-content>
        </div>


        <md-snackbar :md-position="position" :md-duration="isInfinity ? Infinity : duration" :md-active.sync="showSnackbar" md-persistent>
                <span>Please re-upload your matrix. We will compute it again.</span>
                <md-button class="md-primary" @click="showSnackbar = false">Ok</md-button>
        </md-snackbar>
    </div>
</template>

<script>
export default {
    name: 'Results',

    props: ['resultingVals'],

    data() {
        return {
            showSnackbar: false,
            position: 'center',
            duration: 4000,
            isInfinity: false
        }
    }
}
</script>

<style>

#uploaded-image
{
    border-radius: 2px;
}

#card-container
{
    display: flex;
    justify-content: center;
}

.card
{
    width:275px;
    height: 315px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    margin-left: 20px;
    margin-right: 20px;
    margin-bottom: 40px;
}

.top-cards
{
    margin-top: 30px;
}

#results-title
{
    text-align: center;
}

#results-container
{
    flex-direction: row;
    width: 590px;
}

.results-containers-small
{
    width: 200px;
    margin-left: 40px;
    margin-right: 40px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

</style>
    