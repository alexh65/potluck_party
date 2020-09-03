<template>
  <div class="indexWrapper">
    <NavBar/>
    <div class="content">
      Hi, {{ this.$auth.user.username }}!
    </div>
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
.content {
  background-color: white;
  height: inherit;
}
.indexWrapper{
  height: inherit;
}
</style>