<script>
    import { useAuthStore } from '@/stores/auth';
    export default{
        props: ["title"],
        setup(){
            const auth = useAuthStore()
            return { auth }
        }
    }
</script>

<template>
    <div class="topbar">
        <h3>{{ title }}</h3>

        <div class="right">
            <button  v-if="!auth.isLoggedIn" @click="$router.push('/login')" class="btn btn-primary ms-1">เข้าสู่ระบบ</button>
            <span v-else class="user"><router-link to="/login"><i class="bi bi-person-fill" style="font-size: 35px;" ></i></router-link></span>
        </div>
    </div>
</template>

<style>
    .topbar{
        display:flex;
        justify-content:space-between;
        align-items:center;
        background:white;
        padding:10px;
        border-radius:10px;
        box-shadow:0 2px 6px rgba(0,0,0,0.1);
    }

</style>