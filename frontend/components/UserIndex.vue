<template>
  <div>
    <NavBar/>
    Hi, {{ this.$auth.user.username }}!
  </div>
</template>

<script>
import NavBar from '@/components/NavBar'
export default {
  components: {
    NavBar
  }
}
</script>

<style scoped>

</style>