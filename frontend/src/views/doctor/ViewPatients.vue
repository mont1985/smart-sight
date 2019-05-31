<template>
    <div>
        <base-header type="gradient-success" class="pb-6 pb-8 pt-5 pt-md-8">
            <!-- Card stats -->
            <div class="row">
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Patients tested"
                                type="gradient-red"
                                sub-title="350,897"
                                icon="ni ni-active-40"
                                class="mb-4 mb-xl-0">


                    </stats-card>
                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Patients with DME"
                                type="gradient-orange"
                                sub-title="2,356"
                                icon="ni ni-chart-pie-35"
                                class="mb-4 mb-xl-0">

                    </stats-card>
                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="atients with AMD"
                                type="gradient-green"
                                sub-title="924"
                                icon="ni ni-money-coins"
                                class="mb-4 mb-xl-0">

                    </stats-card>

                </div>
                <div class="col-xl-3 col-lg-6">
                    <stats-card title="Patients treated"
                                type="gradient-info"
                                sub-title="49,65%"
                                icon="ni ni-chart-bar-32"
                                class="mb-4 mb-xl-0">

                    </stats-card>
                </div>
            </div>
        </base-header>

        <div class="container-fluid mt--7">
            <div class="row">
                <div class="col">
                    <projects-table title="Diabetic Macular Edema (DME)"></projects-table>
                </div>
            </div>
            <div class="row mt-5">
                <div class="col">
                    <projects-table title="Age-related Macular Edema (AMD)"></projects-table>
                </div>
            </div>
            <div class="row mt-5">
                <div class="col">
                    <projects-table title="All patients"></projects-table>
                </div>
            </div>
        </div>

    </div>
</template>
<script>
    import ProjectsTable from '../Tables/ProjectsTable'
    export default {
        name: 'tables',
        components: {
            ProjectsTable
        }
    };
</script>
<style></style>
