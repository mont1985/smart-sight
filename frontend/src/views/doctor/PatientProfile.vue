<template>
    <div>
        <base-header class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center"
            style="min-height: 600px; background-image: url(img/theme/profile-cover.jpg); background-size: cover; background-position: center top;">
            <!-- Mask -->
            <span class="mask bg-gradient-success opacity-8"></span>
            <!-- Header container -->
            <div class="container-fluid d-flex align-items-center">
                <div class="row">
                    <div class="col-lg-7 col-md-10">
                        <h1 class="display-2 text-white">Patient profile</h1>
                        <p class="text-white mt-0 mb-5">All information on this page is strictly confidential
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        </p>
                    </div>
                </div>
            </div>
        </base-header>

        <div class="container-fluid mt--9">
            <div class="row">
                <div class="col-xl-12 order-xl-2 mb-5 mb-xl-0">

                    <card shadow type="secondary">
                        <div slot="header" class="bg-white border-0">
                            <div class="row align-items-center">
                                <div class="col-8">
                                    <h3 class="mb-0">Patient Details</h3>
                                </div>
                            </div>
                        </div>
                        <template>
                            <form @submit.prevent>
                                <h6 class="heading-small text-muted mb-4">Personal information</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-lg-4 col-sm-12">
                                            <base-input type="text" alternative="" label="Name"
                                                placeholder="Partient's name" input-classes="form-control-alternative"
                                                v-model="patient.name" disabled />
                                        </div>
                                        <div class="col-lg-4 col-sm-12">
                                            <base-input alternative="" label="Age" placeholder="Enter patient's age"
                                                input-classes="form-control-alternative" v-model="patient.age"
                                                type="number" disabled />
                                        </div>
                                        <div class="col-lg-4 col-sm-12">
                                            <base-input required alternative="" label="Id/Passport number"
                                                placeholder="1234567" input-classes="form-control-alternative"
                                                v-model="patient.passport" disabled type="number" />
                                        </div>
                                        <div class="col-lg-5 col-sm-12">
                                            <base-input type="email" required alternative="" label="Gender"
                                                placeholder="Male" input-classes="form-control-alternative"
                                                v-model="patient.gender" disabled />
                                        </div>

                                        <div class="col-lg-3 col-sm-12">
                                            <base-input alternative="" label="Contact"
                                                placeholder="Enter patient's phone number"
                                                input-classes="form-control-alternative" v-model="patient.phoneNumber"
                                                type="number" disabled />
                                        </div>
                                        <div class="col-lg-4 col-sm-12">
                                            <base-input alternative="" label="Marital Status" placeholder=""
                                                input-classes="form-control-alternative" v-model="patient.maritalStatus"
                                                type="text" disabled />
                                        </div>
                                    </div>
                                </div>
                                <hr class="my-4" />
                                <!-- Address -->
                                <h6 class="heading-small text-muted mb-4">Contact information</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-lg-4">
                                            <base-input alternative="" label="Address" placeholder="Home Address"
                                                input-classes="form-control-alternative" v-model="patient.address"
                                                disabled />
                                        </div>
                                        <div class="col-lg-4">
                                            <base-input alternative="" label="Postal code" placeholder="Postal code"
                                                input-classes="form-control-alternative" v-model="patient.zipCode"
                                                disabled />
                                        </div>
                                        <div class="col-lg-4 col-sm-12">
                                            <base-input alternative="" label="County" placeholder=""
                                                input-classes="form-control-alternative" v-model="patient.county"
                                                type="text" disabled />
                                        </div>
                                    </div>
                                </div>
                                <hr class="my-4" />
                                <!-- Description -->
                                <h6 class="heading-small text-muted mb-4">About patient</h6>
                                <div class="pl-lg-4">
                                    <div class="row">
                                        <div class="col-sm-12 col-lg-8">
                                            <div class="form-group">
                                                <base-input alternative="">
                                                    <textarea rows="4" class="form-control form-control-alternative"
                                                        placeholder="The patient's problem ..." disabled></textarea>
                                                </base-input>
                                            </div>
                                        </div>
                                        <div class="col-sm-12 col-lg-4">
                                            <h3>System Diagnosis: {{patient.prediction}}</h3>
                                            <h3>Confidence score: {{patient.confidence}}%</h3>
                                            <h3>Doctor's diagnosis: {{patient.verdict}}</h3>
                                        </div>
                                    </div>
                                </div>
                                <div class="d-flex justify-content-center">
                                    <button :href="patient.image" :download="patient.name" class="btn btn-primary">Download image</button>
                                    <!-- <a :href="patient.image" :download="patient.name + '.TIFF'">
  <img :src="patient.image  " alt="W3Schools"> -->
</a>
                                </div>
                            </form>
                        </template>
                    </card>
                </div>


            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios';
    export default {
        name: 'user-profile',
        data() {
            return {
                patient: {
                    name: "",
                    email: "",
                    age: "",
                    passport: "",
                    gender: "",
                    maritalStatus: "",
                    phoneNumber: "",
                    address: "",
                    county: "",
                    zipCode: "",
                    about: "",
                    image: "",
                    confidence: "",
                    prediction: "",
                    verdict: "",
                    image: ""
                }
            }
        },
        methods: {
            getPatientDetails: function (patient) {
                var self = this;
                axios.get('http://127.0.0.1:8000/api/v1/patients/' + patient + "/", {
                        headers: {
                            'Authorization': 'JWT ' + this.$store.state.token
                        }
                    })
                    .then(function (response) {
                        self.patient.name = response.data.name,
                        self.patient.email = response.data.email,
                        self.patient.age = response.data.age,
                        self.patient.passport = response.data.identification,
                        self.patient.maritalStatus = response.data.marital_status,
                        self.patient.phoneNumber = response.data.contact,
                        self.patient.address = response.data.address,
                        self.patient.county = response.data.county,
                        self.patient.zipCode = response.data.postal_code,
                        self.patient.about = response.data.diagnosis.doctors_comment,
                        self.patient.confidence = response.data.diagnosis.confidence_factor,
                        self.patient.prediction = response.data.diagnosis.model_diagnosis
                        self.patient.verdict = response.data.diagnosis.is_true
                        self.patient.image = response.data.diagnosis.image
                        if(self.patient.gender == "M"){
                            response.data.gender = "Male"
                        }
                        else{
                            response.data.gender = "Female"
                        }
                    })
                    .catch(function (error) {
                        // handle error
                        console.log(error);
                    })
                    .finally(function () {
                        // always executed
                    });
            }
        },
        mounted() {
            this.getPatientDetails(3)
        }
    };
</script>
<style></style>