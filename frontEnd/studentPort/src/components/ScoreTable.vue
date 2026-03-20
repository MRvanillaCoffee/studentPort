<script>
export default {
  props:["scores"]
}
</script>

<template>

<table class="score-table">

<tr>
  <th>วิชา</th>
  <th>คะแนน</th>
</tr>

<tr v-for="s in scores" :key="s.subject">
  <td>{{ s.subject }}</td>
  <td>{{ s.score }}</td>
</tr>

</table>

</template>

<style>
.score-table{
 width:100%;
 background:white;
 border-radius:8px;
}
</style>