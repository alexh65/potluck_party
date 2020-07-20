<template>
  <div class="main">
    <div v-if="$auth.loggedIn">
      Hi
    </div>
    <div v-else>
      <NonUserIndex></NonUserIndex>
    </div>
  </div>
</template>

<script>
import NonUserIndex from '../components/NonUserIndex'
export default {
  layout: 'no-nav',
  components: {
    NonUserIndex
  },
  head() {
    return {
      title: 'PotluckParty | Home'
    }
  }
}
</script>

<style scoped>
.main {
  justify-content: center;
  align-items: center;
}
</style>