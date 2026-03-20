<script>
import { useAuthStore } from '@/stores/auth';
export default{
    setup(){
        const auth = useAuthStore()
        return { auth }
    }
}
</script>

<template>
    <div class="sidebar">
        <div class="logo mb-5">
            <img src="/img/LOGO-CIT.png" alt="" width="100px">
            <h3>STUDENT PORTFOLIO</h3>
        </div>
        

        <ul>
            <li><router-link to="/" class="link"><i class="bi bi-house"></i>  หน้าแรก</router-link></li>
            <li v-if="!auth.isLoggedIn"> <router-link to="/login" class="link"><i class="bi bi-box-arrow-in-right"></i>เข้าสู่ระบบ</router-link></li>
            <li v-if="auth.isLoggedIn"><router-link to="/score" class="link"><i class="bi bi-archive"></i>คะแนน</router-link></li>
            <li><i class="bi bi-book"></i> สาขาที่เปิดสอบ</li>
            <li><i class="bi bi-journals"></i> โครงสร้างหลักสูตร</li>
        </ul>
    </div>
</template>

<style>
    .sidebar{
        border-right: #FF7B1D solid 5px ;
        padding: 10px;
        width: 300px;
        background: #2f45e5;
        color:white;
        height: 100vh;
    }

    .logo{
        text-align: center;
        display: flex;
    }

    .logo h3{
        margin-top: 15px;
        margin-left: 10px;
        text-align: left;
    }

    .sidebar ul{
        list-style-type: none;
    }

    .sidebar li{
        font-size: 20px;
        margin-bottom: 10px;
    }
 
    .link{
        text-decoration: none;
        color: white;
    }

    i{
        margin-Right: 10px;
    }
</style>