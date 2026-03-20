<script>
import Sidebar from "./components/SideBar.vue"

export default {
 components:{ Sidebar }
}
</script>

<template>

<div class="layout">

<Sidebar/>

<div class="content">
<router-view/>
</div>

</div>

</template>