<template>
    <div id="results">

    <!-- Compute Results Title -->
    <h2 class="md-display-1" id="results-title">Computed Results</h2>

        <!-- First Two Card Container -->
        <div id="card-container">

            <!-- Original Image Card Container -->
            <md-content class="md-elevation-1 card top-cards ">
                <img id="uploaded-image" class="md-elevation-3" :src="resultingVals.file" alt="matrix" width="200px" height="200px">
                <h3>Uploaded Matrix</h3>
            </md-content>

            <!-- Predicted Image Card Container -->
            <md-content class="md-elevation-1 card top-cards">
                <table>
                    <tr v-for="(row, rowIndex) in this.resultingVals.results.values" :key="rowIndex">
                        <td v-for="(val, valIndex) in row" class="md-display-1" :key="valIndex">{{precisionRound(val, 1)}}</td>
                    </tr>
                </table>
                <h3>Predicted Matrix</h3>
                <div v-if="this.correctPred == false">
                    <md-button class="md-icon-button md-raised md-primary" @click="correctPred = true">
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

        <!-- Computed Results Card Container -->
        <div id="card-container">

            <!-- Computed Results Card -->
            <md-content id="results-container" class="md-elevation-1 card bottom-cards">

                <!-- Determinant Results -->
                <div class="results-containers-small">
                    <h3>Determinant</h3>
                    <span class="md-display-4">{{precisionRound(this.resultingVals.results.determinant, 3)}}</span>
                </div>

                <!-- Inverse Matrix Results -->
                <div class="results-containers-small">
                    <table>
                        <tr v-for="(row, rowIndex) in this.resultingVals.results.inverse" :key="rowIndex">
                            <td v-for="(val, valIndex) in row" class="md-display-1" :key="valIndex">{{precisionRound(val, 2)}}</td>
                        </tr>
                    </table>
                    <h3>Inverse Matrix</h3>
                </div>
            </md-content>
        </div>

        <!-- Upload New Image Button -->
        <div id="new-btn-container">
            <md-button @click="emitUploadPage()" class="md-primary md-raised">Upload New Matrix!</md-button>
        </div>

        <!-- Popup snackbar for when user says matrix was predicted incorrectly -->
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
            isInfinity: false,
            correctPred: false
        }
    },

    methods: {

        // Method that rounds decimals
        precisionRound: function(number, precision) {
            var factor = Math.pow(10, precision);
            return Math.round(number * factor) / factor;
        },

        // Emits request to change to upload view
        emitUploadPage: function(){
            this.$emit("uploadPage");
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

table {
    border-left: 1px solid rgba(255,255,255,0.7);
    border-right: 1px solid rgba(255,255,255,0.7);
    width:200px;
    height: 200px;
    
}

td
{
    text-align: center;
}

#new-btn-container
{
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

</style>
    