import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import product from '../views/product'
import Category from '../views/Category'
import Search from '../views/Search'
import Cart from '../views/Cart'
import SignUp from '../views/SignUp'
import Login from '../views/Login'
import MyAccount from '../views/MyAccount'
import Checkout from '../views/Checkout'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/:category_slug/:product_slug',
    name: "Product",
    component: product
  },
  {
    path: '/:category_slug/',
    name: "Category",
    component: Category

  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/Sign-Up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/Log-in',
    name: 'Login',
    component: Login
  },
  {
    path: '/myaccount',
    name: 'MyAccount',
    component: MyAccount
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: Checkout
  },
]


const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router