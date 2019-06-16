<template>
    <div>
        <base-header class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center"
            style="min-height: 600px; background-image: url(img/7.jpg); background-size: cover; background-position: center top;">
            <!-- Mask -->
            <span class="mask bg-gradient-success opacity-5"></span>
            <!-- Header container -->
            <div class="container-fluid d-flex align-items-center">
                <div class="row">
                    <div class="col-lg-7 col-md-10">
                        <h1 class="display-2 text-white">Patient information</h1>
                        <p class="text-white mt-0 mb-5">
                            Confiedential details! The should not be disclosed or shared
                            without proper authorization. Enter all information carefully as
                            it cannot be undone if a mistake is commited.
                        </p>
                        <a href="#patientform" class="btn btn-info">Add details</a>
                    </div>
                </div>
            </div>
        </base-header>

        <div class="container-fluid mt--7">
            <div class="row d-flex justify-content-center">
                <!--<div class="col-xl-4 order-xl-2 mb-5 mb-xl-0">

                            <div class="card card-profile shadow">
                                <div class="row justify-content-center">
                                    <div class="col-lg-3 order-lg-2">
                                        <div class="card-profile-image">
                                            <a href="#">
                                                <img src="img/theme/team-4-800x800.jpg" class="rounded-circle">
                                            </a>
                                        </div>
                                    </div>
                                </div>
                                <div class="card-header text-center border-0 pt-8 pt-md-4 pb-0 pb-md-4">
                                    <div class="d-flex justify-content-between">
                                        <base-button size="sm" type="info" class="mr-4">Connect</base-button>
                                        <base-button size="sm" type="default" class="float-right">Message</base-button>
                                    </div>
                                </div>
                                <div class="card-body pt-0 pt-md-4">
                                    <div class="row">
                                        <div class="col">
                                            <div class="card-profile-stats d-flex justify-content-center mt-md-5">
                                                <div>
                                                    <span class="heading">22</span>
                                                    <span class="description">Friends</span>
                                                </div>
                                                <div>
                                                    <span class="heading">10</span>
                                                    <span class="description">Photos</span>
                                                </div>
                                                <div>
                                                    <span class="heading">89</span>
                                                    <span class="description">Comments</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    <div class="text-center">
                                        <h3>
                                            Jessica Jones<span class="font-weight-light">, 27</span>
                                        </h3>
                                        <div class="h5 font-weight-300">
                                            <i class="ni location_pin mr-2"></i>Bucharest, Romania
                                        </div>
                                        <div class="h5 mt-4">
                                            <i class="ni business_briefcase-24 mr-2"></i>Solution Manager - Creative Tim Officer
                                        </div>
                                        <div>
                                            <i class="ni education_hat mr-2"></i>University of Computer Science
                                        </div>
                                        <hr class="my-4" />
                                        <p>Ryan — the name taken by Melbourne-raised, Brooklyn-based Nick Murphy — writes, performs and records all of his own music.</p>
                                        <a href="#">Show more</a>
                                    </div>
                                </div>-->
            </div>
        </div>
        <div id="patientform"></div>
        <!--<div class="col-xl-8 order-xl-1">-->
        <div class="col-lg-10 offset-1">
            <card shadow type="secondary">
                <div slot="header" class="bg-white border-0">
                    <div class="row align-items-center">
                        <div class="col-8">
                            <h3 class="mb-0">Patient Details</h3>
                        </div>
                        <!--<div class="col-4 text-right">-->
                        <!--<a href="#!" class="btn btn-sm btn-primary">Settings</a>-->
                        <!--</div>-->
                    </div>
                </div>
                <template>
                    <form @submit.prevent>
                        <h6 class="heading-small text-muted mb-4">Personal information</h6>
                        <div class="pl-lg-4">
                            <div class="row">
                                <div class="col-lg-4 col-sm-12">
                                    <base-input type="text" alternative="" label="Name" placeholder="Partient's name"
                                        input-classes="form-control-alternative" v-model="patient.name" />
                                </div>
                                <div class="col-lg-4 col-sm-12">
                                    <base-input alternative="" label="Age" placeholder="Enter patient's age"
                                        input-classes="form-control-alternative" v-model="patient.age" type="number" />
                                </div>
                                <div class="col-lg-4 col-sm-12">
                                    <base-input required alternative="" label="Id/Passport number" placeholder="1234567"
                                        input-classes="form-control-alternative" v-model="patient.passport"
                                        type="number" />
                                </div>
                                <div class="col-lg-4 col-sm-12">
                                    <base-input type="email" alternative="" label="EMail" placeholder="Patient's email"
                                        input-classes="form-control-alternative" v-model="patient.email" />
                                </div>
                                <div class="col-lg-3 col-sm-12">
                                    <div class="mb-3">
                                        <small class="text-uppercase font-weight-bold">Gender</small>
                                    </div>
                                    <div class="custom-control custom-radio mb-3">
                                        <input id="male" type="radio" class="custom-control-input"
                                            v-model="patient.gender" value="M" />
                                        <label for="male" class="custom-control-label">Male</label>
                                    </div>
                                    <div class="custom-control custom-radio mb-3">
                                        <input id="female" type="radio" class="custom-control-input"
                                            v-model="patient.gender" value="F" />
                                        <label for="female" class="custom-control-label">Female</label>
                                    </div>
                                </div>

                                <div class="col-lg-3 col-sm-12">
                                    <base-input alternative="" label="Contact"
                                        placeholder="Enter patient's phone number"
                                        input-classes="form-control-alternative" v-model="patient.phoneNumber"
                                        type="number" />
                                </div>
                                <div class="col-lg-3 col-sm-12">
                                    <div class="mb-3">
                                        <small class="text-uppercase font-weight-bold">Marital Status</small>
                                    </div>
                                    <div class="custom-control custom-radio mb-3">
                                        <input id="single" type="radio" class="custom-control-input"
                                            v-model="patient.maritalStatus" value="SINGLE" />
                                        <label for="single" class="custom-control-label">Single</label>
                                    </div>
                                    <div class="custom-control custom-radio mb-3">
                                        <input id="married" type="radio" class="custom-control-input"
                                            v-model="patient.maritalStatus" value="MARRIED" />
                                        <label for="married" class="custom-control-label">Married</label>
                                    </div>
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
                                        input-classes="form-control-alternative" v-model="patient.address" />
                                </div>
                                <div class="col-lg-4">
                                    <base-input alternative="" label="Postal code" placeholder="Postal code"
                                        input-classes="form-control-alternative" v-model="patient.zipCode" />
                                </div>
                                <div class="col-lg-4">
                                    <div class="mb-2">
                                        <small style="font-size: 14px; font-weight: bold">County</small>
                                    </div>
                                    <select class="custom-select" v-model="patient.county">
                                        <option value="" selected>Select county</option>
                                        <option value="nairobi">Nairobi</option>
                                        <option value="mombasa">Mombasa</option>
                                        <option value="kisumu">Kisumu</option>
                                    </select>
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
                                                placeholder="The patient's problem ..." v-model="patient.about"></textarea>
                                        </base-input>
                                    </div>
                                </div>
                                <div class="col-sm-12 col-lg-4">
                                    <div >
                                        <input type="file" ref="file" id="file"/>
                                        <label class="" for="file">Choose file</label>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="d-flex justify-content-center">
                            <button class="btn btn-primary" v-on:click="uploadImage()">Next step</button>
                        </div>
                    </form>
                </template>
            </card>
        </div>
    </div>
</template>
<script>
    import axios from "axios";
    export default {
        name: "new-patient",
        data() {
            return {
                patient: {
                    name: "",
                    age: "",
                    passport: "",
                    gender: "",
                    maritalStatus: "",
                    phoneNumber: "",
                    address: "",
                    county: "",
                    zipCode: "",
                    about: "",
                    image: ""
                }
            };
        },

        methods: {
            uploadImage: function () {
                this.file = this.$refs.file.files[0];
                console.log(this.patient)
                let self = this;
                axios.post('http://localhost:8000/api/v1/patients/', 
                
                        {name: self.patient.name,
                        age: self.patient.age,
                        gender: self.patient.gender,
                        identification: self.patient.passport,
                        email: self.patient.email,
                        contact: self.patient.phoneNumber,
                        marital_status: self.patient.maritalStatus,
                        county: self.patient.county,
                        address: self.patient.address,
                        postal_code: self.patient.zipCode,
                        hospital: 1,
                        image: self.patient.image},
                        {
                        headers: {
                            'Authorization': 'JWT ' + this.$store.state.token,
                            // 'Content-Type': 'multipart/form-data'
                        }
                    })
                    .then(function (response) {
                        var x = response.data;
                        console.log(self.patient.name)
                        // handle success
                        console.table(x);
                        // for (var i = 0; i < x.length; i++) {
                        //     self.ourData.push(x[i])
                        //     var y = {
                        //         Name: "",
                        //         age: "",
                        //         gender: "",
                        //         marital_Status: "",
                        //         contact: "",
                        //         county: "",
                        //         address: "",
                        //         postal_code: "",
                        //         doctors_diagnosis: "",
                        //         system_diagnosis: "",
                        //         system_confidence: "",
                        //     }
                        // }
                        // console.log(self.ourData);
                    })
                    .catch(function (error) {
                        // handle error
                        console.log("our error  " + error);
                    })
                    .finally(function () {
                        // always executed
                        // console.table(self.tableData);  
                    });
            },

            handleImage() {
                this.patient.file = this.$refs.file.files[0];
                let formData = new FormData();
                formData.append("file", this.patient.file);
            }
        },
        mounted() {

        }
    };
</script>
<style></style>