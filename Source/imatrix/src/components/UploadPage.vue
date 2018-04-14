<template>
    <div id="upload-page">

    <md-empty-state
        md-icon="file_upload"
        md-label="Upload Matrix"
        md-description="Upload you image in png or jpg format. Then the upload button. The evaluation of the matrix may take a few minutes.">
        <md-field>
            <label>Upload Matrix Image</label>
                <md-file v-model="single" accept="image/*" />
        </md-field><br>
        <md-button @click="upload()" type="submit" class="md-primary md-raised">Upload</md-button>
    </md-empty-state>

    <md-dialog-alert
        :md-active.sync="dialog"
        md-content="Your matrix has been uploaded!!"
        md-confirm-text="Ok" />

    <md-dialog :md-active.sync="dialog">
      <md-dialog-title>Image Uploaded</md-dialog-title>

      <md-dialog-actions>
        <md-button class="md-primary" @click="emitUpload">Ok</md-button>
      </md-dialog-actions>
    </md-dialog>


    </div>

    
</template>

<script>
export default {
    name: 'UploadPage',

    data() {
        return {
            dialog: false,
            resultingVals: ''

        }
    },

    methods: {
        upload: function() {
            // upload image to backend, and get results

            // Demo Data
            let results = {
                determinant: -16,
                inverse:[ [-1/2, 5/16], [7/16, -1/8] ], 
                values: [ [2,5], [7,8] ],
            }

            this.resultingVals = results;

            this.dialog = true;
        },

        emitUpload: function()
        {
            this.dialog = false;
            this.$emit("results", this.resultingVals);
        }
    }

}
</script>

<style>

</style>
