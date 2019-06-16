<template>
  <div class="card shadow" :class="type === 'dark' ? 'bg-default': ''">
    <div class="card-header border-0" :class="type === 'dark' ? 'bg-transparent': ''">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0" :class="type === 'dark' ? 'text-white': ''">
            {{title}}
          </h3>
        </div>
        <div class="col text-right">
          <base-button type="primary" size="sm">See all</base-button>
        </div>
      </div>
    </div>

    <div class="table-responsive">
      <base-table class="table align-items-center table-flush" :class="type === 'dark' ? 'table-dark': ''"
        :thead-classes="type === 'dark' ? 'thead-dark': 'thead-light'" tbody-classes="list" :data="ourData">
        <template slot="columns">
          <th>Name</th>
          <th>Age</th>
          <th>Gender</th>
          <th>Marital Status</th>
          <th>Postal COde</th>
          <th>Email</th>
          <th>Address</th>
          <th>Contact</th>
          <th>County</th>
          <th>Postal Code</th>
          <th>Patient Url</th>
          <th>Output</th>
          <th>System confidence</th>
          <th>Doctor's comment</th>
        </template>

        <template slot-scope="{row}">
          <!-- <th scope="row">
            <div class="media align-items-center">
              <div class="media-body">
                <span class="name mb-0 text-sm">{{row.name}}</span>
              </div>
            </div>
          </th> -->
          <td class="budget">
            {{row.name}}
          </td><!--
          <td>
            <badge class="badge-dot mr-4" :type="row.statusType">
              <i :class="`bg-${row.age}`"></i>
              <span class="status">{{row.status}}</span>
            </badge>
          </td> -->
          <td>{{row.age}}</td>
          <td>{{row.gender}}</td>
          <td>{{row.marital_status}}</td>
          <td>{{row.identification}}</td>
          <td>{{row.email}}</td>
          <td>{{row.address}}</td>
          <td>{{row.contact}}</td>
          <td>{{row.county}}</td>
          <td>{{row.postal_code}}</td>
          <td>{{row.url}}</td>
          <td>{{row.diagnosis.model_diagnosis}}</td>  
          <td>{{row.diagnosis.confidence_factor}}</td>
          <td>{{row.diagnosis.doctors_comment}}</td>
          <!-- <td>{{row.}}</td>
          <td>{{row.}}</td>
          <td>{{row.}}</td>
          <td>{{row.}}</td>
          <td>{{row.}}</td>
          <td>{{row.}}</td> -->
          <!-- <td>
            <div class="avatar-group">
              <a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip"
                data-original-title="Ryan Tompson">
                <img alt="Image placeholder" src="img/theme/team-1-800x800.jpg">
              </a>
              <a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip"
                data-original-title="Romina Hadid">
                <img alt="Image placeholder" src="img/theme/team-2-800x800.jpg">
              </a>
              <a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip"
                data-original-title="Alexander Smith">
                <img alt="Image placeholder" src="img/theme/team-3-800x800.jpg">
              </a>
              <a href="#" class="avatar avatar-sm rounded-circle" data-toggle="tooltip"
                data-original-title="Jessica Doe">
                <img alt="Image placeholder" src="img/theme/team-4-800x800.jpg">
              </a>
            </div>
          </td>

          <td>
            <div class="d-flex align-items-center">
              <span class="completion mr-2">{{row.completion}}%</span>
              <div>
                <base-progress :type="row.statusType" :show-percentage="false" class="pt-0" :value="row.completion" />
              </div>
            </div>
          </td>

          <td class="text-right">
            <base-dropdown class="dropdown" position="right">
              <a slot="title" class="btn btn-sm btn-icon-only text-light" role="button" data-toggle="dropdown"
                aria-haspopup="true" aria-expanded="false">
                <i class="fas fa-ellipsis-v"></i>
              </a>

              <template>
                <a class="dropdown-item" href="#">Action</a>
                <a class="dropdown-item" href="#">Another action</a>
                <a class="dropdown-item" href="#">Something else here</a>
              </template>
            </base-dropdown>
          </td> -->

        </template>

      </base-table>
    </div>

    <div class="card-footer d-flex justify-content-end" :class="type === 'dark' ? 'bg-transparent': ''">
      <!-- <base-pagination total="30"></base-pagination> -->
    </div>

  </div>
</template>
<script>
  import axios from 'axios';
  export default {
    name: 'projects-table',
    props: {
      type: {
        type: String
      },
      title: String
    },
    data() {
      return {
        tableData: [{
            img: 'img/theme/bootstrap.jpg',
            title: 'Argon Design System',
            budget: '$2500 USD',
            status: 'pending',
            statusType: 'warning',
            completion: 60
          },
          {
            img: 'img/theme/angular.jpg',
            title: 'Angular Now UI Kit PRO',
            budget: '$1800 USD',
            status: 'completed',
            statusType: 'success',
            completion: 100
          },
          {
            img: 'img/theme/sketch.jpg',
            title: 'Black Dashboard',
            budget: '$3150 USD',
            status: 'delayed',
            statusType: 'danger',
            completion: 72
          },
          {
            img: 'img/theme/react.jpg',
            title: 'React Material Dashboard',
            budget: '$4400 USD',
            status: 'on schedule',
            statusType: 'info',
            completion: 90
          },
          {
            img: 'img/theme/vue.jpg',
            title: 'Vue Paper UI Kit PRO',
            budget: '$2200 USD',
            status: 'completed',
            statusType: 'success',
            completion: 100
          }
        ],
        ourData: []
      }
    },
    methods: {
      getpatients: function () {

      }
    },
    mounted() {
      var self = this;
      // console.table(self.tableData);
      axios.get('http://localhost:8000/api/v1/patients/', {
          headers: {
            'Authorization': 'JWT ' + this.$store.state.token
          }
        })
        .then(function (response) {
          var x = response.data;
          // handle success
          console.table(x);
          for (var i = 0; i < x.length; i++) {
            self.ourData.push(x[i])
            var y = {
              Name: "",
              age: "",
              gender: "",
              marital_Status: "",
              contact: "",
              county: "",
              address: "",
              postal_code: "",
              doctors_diagnosis: "",
              system_diagnosis: "",
              system_confidence: "",
            }
          }
          console.log(self.ourData);
        })
        .catch(function (error) {
          // handle error
          console.log("our error  " + error);
        })
        .finally(function () {
          // always executed
          // console.table(self.tableData);  
        });

    }
  }
</script>
<style>
</style>