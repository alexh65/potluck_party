<template>
  <div>
    Hi, {{ $auth.user.username }}!
  </div>
</template>

<script>
export default {
  layout: 'default'
}
</script>