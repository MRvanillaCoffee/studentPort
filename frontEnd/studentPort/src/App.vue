<script>
import Sidebar from "@/components/SideBar.vue"
import TopBar from "@/components/TopBar.vue"

export default {
 components:{ Sidebar,TopBar }
}
</script>

<template>

<div class="layout">

<Sidebar/>


<div class="content">
  <TopBar title="ระบบรายงานผลการเรียนรู้ตามเกณฑ์คะแนน"/>
  <router-view />
</div>

</div>

</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Kanit:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

*{
  font-family: 'kanit';
}
.layout {
  display: flex;
  height: 100vh;
}

.main {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.content {
  padding: 20px;
  background: #f5f5f5;
  flex: 1;
}
</style>