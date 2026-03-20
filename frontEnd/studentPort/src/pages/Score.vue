<script>
import { useAuthStore } from "@/stores/auth"

export default {

  computed: {
    authUser(){
      const auth = useAuthStore()
      return auth.user
    }
  },

  data(){
    return{

      year: "",
      semester: "",

      years: [],
      semesters: [],
      scores: [],
      loading: false,
      errorMessage: ""
    }
  },

  watch:{
    year(){
      this.fetchScores()
    },
    semester(){
      this.fetchScores()
    }
  },

  mounted(){
    this.fetchScores()
  },

  methods:{
    async fetchScores(){
      const auth = useAuthStore()
      const studentId = auth.user?.student_id

      if(!studentId){
        this.errorMessage = "ไม่พบข้อมูลนักศึกษา กรุณาเข้าสู่ระบบใหม่"
        this.scores = []
        return
      }

      this.loading = true
      this.errorMessage = ""

      try{
        const params = new URLSearchParams()
        if(this.year){
          params.set("year", this.year)
        }
        if(this.semester){
          params.set("semester", this.semester)
        }

        const queryString = params.toString() ? `?${params.toString()}` : ""
        const response = await fetch(`http://127.0.0.1:8000/scores/${studentId}${queryString}`)

        if(!response.ok){
          this.errorMessage = "โหลดคะแนนไม่สำเร็จ"
          this.scores = []
          return
        }

        const result = await response.json()
        this.scores = result.items || []
        this.years = result.years || []
        this.semesters = result.semesters || []
      }catch(_error){
        this.errorMessage = "ไม่สามารถเชื่อมต่อ API ได้"
        this.scores = []
      }finally{
        this.loading = false
      }
    }
  }
}
</script>

<template>

<div class="score-card mt-3">

  <div class="student-header mb-3">
    <h5 class="mb-1">ชื่อ: {{ authUser?.name || '-' }}</h5>
    <div>รหัสนักศึกษา: {{ authUser?.student_id || '-' }}</div>
  </div>

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
      <tr v-if="loading">
        <td colspan="5">กำลังโหลดข้อมูล...</td>
      </tr>
      <tr v-else-if="errorMessage">
        <td colspan="5">{{ errorMessage }}</td>
      </tr>
      <tr v-else-if="scores.length === 0">
        <td colspan="5">ไม่พบข้อมูลคะแนน</td>
      </tr>
      <tr v-else v-for="(s,i) in scores" :key="`${s.subject}-${s.year}-${s.semester}-${i}`">
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