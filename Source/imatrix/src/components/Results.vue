<template>
    <div id="results">
        <!-- <md-button class="md-accent md-raised" @click="first = true">Alert</md-button>
    <md-button class="md-primary md-raised" @click="second = true">Alert</md-button> -->
    <div id="card-container">
        <md-content class="md-elevation-1 card">
            <img id="uploaded-image" class="md-elevation-3" src="../assets/matrix.jpg" alt="matrix" width="200px" height="200px">
            <h3>Uploaded Matrix</h3>
        </md-content>

        <md-content class="md-elevation-1 card">
            <img id="uploaded-image" class="md-elevation-3" src="../assets/matrix.jpg" alt="matrix" width="200px" height="200px">
            <h3>Predicted Matrix</h3>
            <div>
                <md-button class="md-icon-button md-raised md-primary">
                    <md-icon>thumb_up</md-icon>
                </md-button>
                <!-- Accent Button -->
                <md-button class="md-icon-button md-raised md-accent">
                    <md-icon>thumb_down</md-icon>
                </md-button>
            </div>
        </md-content>
    </div>
    <!-- Primary button -->
    <!-- <md-button class="md-fab md-primary">
        <md-icon>add</md-icon>
    </md-button> -->
    </div>
</template>

<script>
export default {
    name: 'Results',

    props: ['resultingVals'],



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
    margin-top: 40px;
}

</style>
    