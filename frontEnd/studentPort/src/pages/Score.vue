<script>
export default {

  data(){
    return{

      year: "",
      semester: "",

      years: ["2566","2567","2568"],
      semesters: ["1","2","3"],

      scores: [
        { subject:"Programming", score:85, grade:"A", year:"2567", semester:"1" },
        { subject:"Database", score:78, grade:"B+", year:"2567", semester:"1" },
        { subject:"Web Dev", score:92, grade:"A", year:"2567", semester:"2" },
        { subject:"Math", score:65, grade:"C+", year:"2566", semester:"2" }
      ]
    }
  },

  computed:{
    filteredScores(){
      return this.scores.filter(s => {

        const matchYear =
          !this.year || s.year === this.year

        const matchSem =
          !this.semester || s.semester === this.semester

        return matchYear && matchSem

      })
    }
  }
}
</script>

<template>

<div class="score-card mt-3">

  <div class="filter-bar">

    <label>ปีการศึกษา</label>

    <select v-model="year" class="rounded">
      <option value="">ทั้งหมด</option>
      <option v-for="y in years" :key="y" :value="y">
        {{ y }}
      </option>
    </select>

    <label>ภาคเรียนที่</label>

    <select v-model="semester" class="rounded">
      <option value="">ทั้งหมด</option>
      <option v-for="s in semesters" :key="s" :value="s">
        {{ s }}
      </option>
    </select>

  </div>

  <table class="score-table">

    <thead>
      <tr>
        <th>วิชา</th>
        <th>คะแนน</th>
        <th>เกรด</th>
        <th>ปี</th>
        <th>เทอม</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="(s,i) in filteredScores" :key="i">
        <td>{{ s.subject }}</td>
        <td>{{ s.score }}</td>
        <td>{{ s.grade }}</td>
        <td>{{ s.year }}</td>
        <td>{{ s.semester }}</td>
      </tr>
    </tbody>

  </table>

</div>

</template>

<style>
.score-card{
  background:white;
  padding:20px;
  border-radius:12px;
  box-shadow:0 4px 12px rgba(0,0,0,0.1);
}

.filter-bar{
  display:flex;
  align-items:center;
  gap:10px;
  margin-bottom:15px;
}

select{
  padding:6px;
}

.score-table{
  width:100%;
  border-collapse:collapse;
}

.score-table th,
.score-table td{
  padding:10px;
  border-bottom:1px solid #ddd;
}
</style>