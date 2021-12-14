import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import RegisterAndLogin from '../views/RegisterAndLogin.vue'
import Feed from '../views/Feed.vue'
import Account from '../views/Account.vue'
import Event from '../views/Event.vue'
import EventsToAttend from '../views/EventsToAttend.vue'
import Participants from '../views/Participants.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/eventparticipants',
    name: 'Participants',
    component: Participants
  },
  {
    path: '/nextEvents',
    name: 'EventsToAttend',
    component: EventsToAttend
  },
  {
    path: '/event',
    name: 'Event',
    component: Event
  },
  {
    path: '/register',
    name: 'RegisterAndLogin',
    component: RegisterAndLogin
  },
  {
    path: '/myaccount',
    name: 'Account',
    component: Account
  },
  {
    path: '/feed',
    name: 'Feed',
    component: Feed
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
