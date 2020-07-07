<template>
  <div id="page">
    <nuxt/>
  </div>
</template>

<style>
#page {
  height:100vh;
}

.main{
  height: inherit;
  text-align: center;
  background-color: #cd5c5c;
  display: flex;
  flex-direction: column;
}

.btn-blue {
  background-color: #0F434F;
  color: white;
  border-color: #0F434F;
}
.btn-blue:hover {
  background-color: #092b33;
  color: white;
  border-color: #092b33;
}
.back {
  width: fit-content;
  margin: 10pt;
  position: absolute;
  bottom: 0;
}

.back > a:hover{
  font-size: larger;
  text-decoration: none;
}
</style>