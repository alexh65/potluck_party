<template>
  <div class="main">
    <div v-if="$auth.loggedIn">
      <UserIndex/>
    </div>
    <div v-else>
      <NonUserIndex/>
    </div>
  </div>
</template>

<script>
import NonUserIndex from '@/components/NonUserIndex'
import UserIndex from  '@/components/UserIndex'
export default {
  layout: 'no-nav',
  components: {
    NonUserIndex,
    UserIndex
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