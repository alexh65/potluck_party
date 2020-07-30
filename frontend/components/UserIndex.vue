<template>
  <div>
    Hi, {{ this.$auth.user.username }}!
  </div>
</template>

<script>
export default {
  layout: 'default'
}
</script>