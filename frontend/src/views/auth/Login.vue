<template>
    <div class="row justify-content-center">
        <div class="col-lg-5 col-md-7">
            <div class="card bg-secondary shadow border-0">
                <div class="card-header bg-transparent pb-1 pt-3">
                    <!--<div class="text-muted text-center mt-2 mb-3"><small>Sign in with</small></div>-->
                    <div class="btn-wrapper text-center">
                        <!--  <a href="#" class="btn btn-neutral btn-icon">
                            <span class="btn-inner&#45;&#45;icon"><img src="img/icons/common/github.svg"></span>
                            <span class="btn-inner&#45;&#45;text">Github</span>
                        </a>
                        <a href="#" class="btn btn-neutral btn-icon">
                            <span class="btn-inner&#45;&#45;icon"><img src="img/icons/common/google.svg"></span>
                            <span class="btn-inner&#45;&#45;text">Google</span>
                        </a>-->
                        <h3><b>Sign in to continue</b></h3>
                    </div>
                </div>
                <div class="card-body px-lg-5 py-lg-5">
                    <!--<div class="text-center text-muted mb-4">
                        <small>Or sign in with credentials</small>
                    </div>-->
                    <form role="form">
                        <base-input class="input-group-alternative mb-3" placeholder="Username"
                            addon-left-icon="ni ni-email-83" v-model="details.username">
                        </base-input>
                        <base-input class="input-group-alternative mb-3" placeholder="Email"
                            addon-left-icon="ni ni-email-83" v-model="details.email">
                        </base-input>
                        <base-input class="input-group-alternative" placeholder="Password" type="password"
                            addon-left-icon="ni ni-lock-circle-open" v-model="details.password">
                        </base-input>
                        <!--<base-checkbox class="custom-control-alternative">-->
                        <!--<span class="text-muted">Remember me</span>-->
                        <!--</base-checkbox>-->
                        <div class="text-center">
                            <base-button type="primary" class="my-4" v-on:click="getLoginData">Sign in</base-button>
                        </div>
                    </form>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col-6">
                    <a href="#" class="text-light"><small>Forgot password?</small></a>
                </div>
                <div class="col-6 text-right">
                    <router-link to="/register" class="text-light"><small>Create new account</small></router-link>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
    import axios from 'axios';
    import Vuex from 'vuex';
    export default {
        name: 'login',
        data() {
            return {
                auth: {
                    user: {
                        id: '',
                        name: '',
                        email: '',
                        hospital: ''
                    }
                },
                details: {
                    'username': 'lewis',
                    'email': 'lewis@admin.com',
                    'password': 'lewis123'
                }
            }
        },
        methods: {
            getLoginData: function () {
                const self = this;
                if (self.details.username === "" || self.details.email === "" || self.details.password === "") {
                    alert("Fill out all fields")
                } else {
                    console.info("Submiting...")
                    axios.post('http://127.0.0.1:8000/api/v1/auth/login/', {
                        "username": self.details.username,
                        "email": self.details.email,
                        "password": self.details.password
                    })
                    .then(function (response) {
                        if (response.status == "200"){
                            self.$store.state.token = response.data.token;
                            self.$store.state.user.username = response.data.user.username;
                            self.$store.state.user.email = response.data.user.email;
                            self.$store.state.user.pk = response.data.user.pk;
                            self.$store.state.user.name = response.data.user.first_name + " " + response.data.user.last_name;
                            self.$router.push('view_patients') 
                        }
                        else{
                            alert("Check credentials");//
                        }
                    })
                    .catch(function (error) {
                        // handle error
                    })
                    .finally(function () {
                        // always executed
                        console.log(self.$store.state.user);
                    });
                }   
            }
        },
        mounted() {
        },

    }
</script>
<style>
    .error {
        border: 1px solid red;
    }
</style>