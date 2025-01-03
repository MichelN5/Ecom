<template>
   <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Djacket
            </p>
            <p class="subtitle">
                The best jacket store online
            </p>
        </div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest products</h2>
      </div>
      <ProductBox 
        v-for="product in latest_products"
        v-bind:key="product.id"
        v-bind:product="product" />

  </div>
</div>
</template>

<script>
document.title= 'Home'
import ProductBox from '../components/ProductBox.vue'
import axios from 'axios'
export default {
  name: 'Home',
  data(){
    return {
      latest_products: []
    }
  },

  components: {
    ProductBox
  },

  mounted(){
    this.getLatestProducts()
  },

  methods: {
    getLatestProducts(){
      axios.get('/api/v1/latest-products')
      .then( res => {
        this.latest_products= res.data
      })

    }
  }

}
</script>
