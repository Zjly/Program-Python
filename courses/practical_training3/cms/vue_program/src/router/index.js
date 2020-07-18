import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Bing from '../views/Bing.vue'
import Word from '../views/Word.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/bing',
    name: 'Bing',
    component: Bing
  },
  {
    path: '/word',
    name: 'Word',
    component: Word
  }
]

const router = new VueRouter({
  routes
})

export default router
