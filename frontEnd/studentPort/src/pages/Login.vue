<script>


    import { useAuthStore } from "@/stores/auth"

    export default {
        data(){
            return{
            username:"Thanakorn",
            password:"1234"
            }
        },
        setup(){
            const auth = useAuthStore()
            return {auth}
        }
        ,

        methods:{
            login(){

            const auth = useAuthStore()
            if(this.username && this.password){
                auth.login({
                name: this.username
                })
                this.$router.push("/score")
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

                <form @submit.prevent="submit">

                    <div class="row">
                        <div class="col-12">
                            <input v-model="username" placeholder="Account" class="form-control">
                        </div>
                    </div>

                    <div class="row mt-3">
                        <div class="col-12">
                            <input type="password" v-model="password" placeholder="Password" class="form-control">
                        </div>
                    </div>
                    <button type="button"  @click="login" class="btn btn-primary mt-3">เข้าสู่ระบบ</button>
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