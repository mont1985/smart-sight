import Vue from 'vue'
import Router from 'vue-router'
import DashboardLayout from '@/layout/DashboardLayout'
import AuthLayout from '@/layout/AuthLayout'
Vue.use(Router)

export default new Router({
  linkExactActiveClass: 'active',
  routes: [
    {
      path: '/',
      redirect: 'dashboard',
      component: DashboardLayout,
      children: [
        {
          path: '/dashboard',
          name: 'Dashboard',
          // route level code-splitting
          // this generates a separate chunk (about.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/Dashboard.vue')
        },
        {
          path: '/new_patient',
          name: 'New Patient',
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/NewPatient')
        },
        {
          path: '/view_patients',
          name: 'View Patients',
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/ViewPatients')
        },
        {
          path: '/icons',
          name: 'icons',
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/Icons.vue')
        },
        {
          path: '/dashboards',
          name: 'iconz',
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/Icons.vue')
        },
        {
          path: '/profile',
          name: 'profile',
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/UserProfile.vue')
        },
        {
          path: '/patient',
          name: 'patient',
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/PatientProfile.vue')
        },
        {
          path: '/maps',
          name: 'maps',
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/Maps.vue')
        },
        {
          path: '/tables',
          name: 'tables',
          component: () => import(/* webpackChunkName: "demo" */ './views/doctor/Tables.vue')
        }
      ]
    },
    // {
    //   path: '/dash',
    //   redirect: 'dashboards',
    //   component: DashboardLayout,
    //   children: [
    //     {
    //       path: '/dashboards',
    //       name: 'dashboards',
    //       // route level code-splitting
    //       // this generates a separate chunk (about.[hash].js) for this route
    //       // which is lazy-loaded when the route is visited.
    //       component: () => import(/* webpackChunkName: "demo" */ './views/Dashboard.vue')
    //     },
    //     {
    //       path: '/icons',
    //       name: 'icons',
    //       component: () => import(/* webpackChunkName: "demo" */ './views/Icons.vue')
    //     },
    //     {
    //       path: '/dashboards',
    //       name: 'icons',
    //       component: () => import(/* webpackChunkName: "demo" */ './views/Icons.vue')
    //     },
    //     {
    //       path: '/profile',
    //       name: 'profile',
    //       component: () => import(/* webpackChunkName: "demo" */ './views/UserProfile.vue')
    //     },
    //     {
    //       path: '/maps',
    //       name: 'maps',
    //       component: () => import(/* webpackChunkName: "demo" */ './views/Maps.vue')
    //     },
    //     {
    //       path: '/tables',
    //       name: 'tables',
    //       component: () => import(/* webpackChunkName: "demo" */ './views/Tables.vue')
    //     }
    //   ]
    // },
    {
      path: '/',
      redirect: 'login',
      component: AuthLayout,
      children: [
        {
          path: '/logins',
          name: 'logins',
          component: () => import(/* webpackChunkName: "demo" */ './views/Login.vue')
        },
        {
          path: '/register',
          name: 'register',
          component: () => import(/* webpackChunkName: "demo" */ './views/Register.vue')
        },
        {
          path: '/login',
          name: 'Login',
          component: () => import(/* webpackChunkName: "demo" */ './views/auth/Login.vue')
        }
      ]
    }
  ]
})
