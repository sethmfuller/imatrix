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
                <md-button v-if="this.form.file == null" disabled type="submit" class="md-primary md-raised">Upload</md-button>
                <md-button v-if="this.form.file != null && this.form.load == false && this.form.uploaded == false" type="submit" class="md-primary md-raised">Upload</md-button>
                <radar-spinner
                    :animation-duration="2500"
                    :size="60"
                    :color="'#448aff'"
                    v-if="this.form.load == true"
                    id="logo"
                />
                <md-icon 
                    class="md-size-2x"
                    style="color: #448aff"
                    v-if="this.form.uploaded == true">
                    check_circle
                </md-icon>
            </md-empty-state>
        </form>

        <!-- Popup dialog alerting user that image was sucessfully uploaded -->
        <md-dialog :md-active.sync="dialog">
            <md-dialog-title>{{this.dialogText}}</md-dialog-title>

            <md-dialog-actions>
                <md-button class="md-primary" @click="emitUpload">Great</md-button>
            </md-dialog-actions>
        </md-dialog>
    </div>
</template>

<script>
import { postImage } from '../api/api_calls.js'
import { RadarSpinner, SemipolarSpinner} from 'epic-spinners'
export default {
    name: 'UploadPage',

    components: {
        RadarSpinner,
        SemipolarSpinner
    },

    data() {
        return {
            dialog: false,
            resultingVals: null,
            form : {
                file_name: null,
                file_data_url: null,
                file: null,
                load: false,
                uploaded: false,
            },
            dialogText: "Image Uploaded",
            requestSuccess: null,
            responseData: null,
        }
    },

    methods: {

        resetData () {
            this.resultingVals = null;
            this.form.file_name = null;
            this.form.file_data_url = null;
            this.form.file = null;
        },

        createImage (file) {
            var image = new Image();
            var reader = new FileReader();
            reader.onload = (e) => {
                this.form.file = e.target.result;
            };
            reader.readAsDataURL(file);
        },

        retrieveImage (e) {

            this.resetData();
            
            // Retrieve image from form and place in data
            var files = e.target.files || e.dataTransfer.files;
            if (!files.length)
                console.log("Error during upload");
            this.createImage(files[0]);
            this.form.file = files[0];
        },

        uploadImage () {

            this.form.load = true;

            let formData = new FormData();
            formData.append('image', this.form.file);

            var self = this;

            // Send image to server
            jQuery.ajax({
                type: 'POST',
                contentType: false,
                processData: false,
                url: `http://localhost:5000/upload`,
                data: formData,
                dataType: "json",
                success: function(json, status){
                    if (status != "success") {
                        console.log("Error loading data");
                        return;
                    }

                    self.responseData = json;
                    self.takeInData(json);
                    
                    // this.takeInData(json);
                },
                error: function(result, status, err) {
                    console.log("Error loading data");
                    return;
                }
            });
        },

        takeInData (data) {
            this.responseData = data;
            console.log("Data loaded!");
            this.form.load = false;
            this.form.uploaded = true;
            this.dialog = true;
        },

        emitUpload: function()
        {
            var results = {
                determinant: this.responseData.determinant,
                inverse: this.responseData.inverse, 
                values: this.responseData.values,
            }

            var returnVals = {
                'results': results,
                'file': this.form.file,
            }

            this.dialog = false;
            this.$emit("resultsMethod", returnVals);
        },
    }

}
</script>
