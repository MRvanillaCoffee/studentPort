<script >
  export default{
    data(){
      return{
        picture:'img/LOGO-CIT.png'
      }
    }
  }
</script>

<template>
  <div class=" d-flex vh-100" style="background-color: #d9d9d9;">
    <div class="bg-primary text-white p-3" style="width: 230px; border-right: 8px solid #ff7b1d ;">
        <div class="text-center"><img v-bind:src="picture" alt="Cit logo" width="100px"></div>
        <div class="mt-3 text-center"><h3>STUDENT <br> PORTFOLIO</h3></div>
      
    </div>

    <div class="flex-grow-1 p-4">
      <div class="row bg-white p-3 " style="border: 1px solid white;border-radius: 10px;">
        <div class="col-8">
          <h3>ระบบรายงานคะแนน</h3>
        </div>
        <div class="col-4 text-end">
          <button class="btn btn-primary">
            เข้าสู่ระบบ
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
