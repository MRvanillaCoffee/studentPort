<script>
    import { useAuthStore } from "@/stores/auth"

    export default {
        data(){
            return{
            studentId:"6803052411022",
            password:"1234",
            loading:false,
            errorMessage:""
            }
        },
        setup(){
            const auth = useAuthStore()
            return {auth}
        }
        ,

        methods:{
            async login(){
                this.errorMessage = ""

                if(!this.studentId || !this.password){
                    this.errorMessage = "กรุณากรอกรหัสนักศึกษาและรหัสผ่าน"
                    return
                }

                this.loading = true

                try{
                    const response = await fetch("http://127.0.0.1:8000/auth/login", {
                        method:"POST",
                        headers:{
                            "Content-Type":"application/json"
                        },
                        body: JSON.stringify({
                            student_id: this.studentId,
                            password: this.password
                        })
                    })

                    if(!response.ok){
                        const result = await response.json()
                        this.errorMessage = result.detail || "เข้าสู่ระบบไม่สำเร็จ"
                        return
                    }

                    const userData = await response.json()
                    this.auth.login(userData)
                    this.$router.push("/score")
                }catch(_error){
                    this.errorMessage = "ไม่สามารถเชื่อมต่อ API ได้"
                }finally{
                    this.loading = false
                }
            },
            logout(){
                this.auth.logout()
            }
        }
    }
</script>

<template>

    <div>
        <div v-if="!auth.isLoggedIn" class="d-flex justify-content-center">
            <div class="login-form mt-5">

                <h3>กรุณาป้อน ICIT Account</h3>

                <form @submit.prevent="login">

                    <div class="row">
                        <div class="col-12">
                            <input v-model="studentId" placeholder="Student ID" class="form-control">
                        </div>
                    </div>

                    <div class="row mt-3">
                        <div class="col-12">
                            <input type="password" v-model="password" placeholder="Password" class="form-control">
                        </div>
                    </div>
                    <p v-if="errorMessage" class="text-danger mt-2 mb-0">{{ errorMessage }}</p>
                    <button type="submit" :disabled="loading" class="btn btn-primary mt-3">
                        {{ loading ? "กำลังเข้าสู่ระบบ..." : "เข้าสู่ระบบ" }}
                    </button>
                </form>

            </div>
        </div>
        <div v-else>

    <h2>Welcome 👋 {{ auth.user.name }}</h2>

    <button @click="logout">
      Logout
    </button>

  </div>
    </div>
    

</template>

<style>
    .login-form{
        width:100%;
        max-width:500px;
        background:white;
        padding:20px;
        border-radius:12px;
        box-shadow:0 4px 12px rgba(0,0,0,0.1);
    }
</style>