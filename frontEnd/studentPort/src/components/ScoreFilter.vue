<script>
export default {
  data(){
    return{
      year:"",
      term:""
    }
  }
}
</script>

<template>

<div class="filter">

  ปีการศึกษา
  <input v-model="year">

  ภาคเรียน
  <input v-model="term">

</div>

</template>

<style>
.filter{
 display:flex;
 gap:15px;
 background:#eee;
 padding:10px;
 border-radius:8px;
}
</style>