<template>
    <div id="upload-page">

        <!-- Import image form -->
        <form @submit.prevent="uploadImage()">
            <md-empty-state
                md-icon="file_upload"
                md-label="Upload Matrix"
                md-description="Upload you image in png or jpg format. It must be an n x n matrix. Then the upload button. The evaluation of the matrix may take a few minutes.">
                <md-field>
                    <label>Upload Matrix Image</label>
                    <md-file 
                        v-bind="this.form.file_name" 
                        @change="retrieveImage($event)" 
                        accept="image/*" />
                </md-field>
                <br>
                <md-button type="submit" class="md-primary md-raised">Upload</md-button>
            </md-empty-state>
        </form>

        <!-- Popup dialog alerting user that image was sucessfully uploaded -->
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
            resultingVals: null,
            form : {
                file_name: null,
                file_data_url: null
            }
        }
    },

    methods: {

        createImage (file) {
            var image = new Image();
            var reader = new FileReader();

            reader.onload = (e) => {
                this.form.file = e.target.result;
            };
            reader.readAsDataURL(file);
        },

        retrieveImage (e) {
            
            // Retrieve image from form and place in data
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                console.log("Error during upload");
            this.createImage(files[0]);

        },

        uploadImage () {

            let formData = new FormData();
            formData.append('image', this.file_data_url);

            fetchData().then(data => {
                //do stuff
            });

            // Demo Data
            var results = {
                determinant: -16,
                inverse:[ [-1/2, 5/16], [7/16, -1/8] ], 
                values: [ [3,5], [7,0] ],
            }

            this.resultingVals = results;

            this.dialog = true;
        },

        emitUpload: function()
        {
            this.dialog = false;
            this.$emit("resultsMethod", this.resultingVals);
        }
    }

}
</script>
