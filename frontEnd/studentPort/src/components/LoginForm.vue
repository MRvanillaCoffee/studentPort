<script>
    export default {
        data(){
            return{
            user:"",
            pass:""
            }
        },
        methods:{
            submit(){
            this.$emit("login",{
                user:this.user,
                pass:this.pass
            })
            }
        }
    }
</script>

<template>

    <div class="login-card">

        <h3>กรุณาป้อน ICIT Account</h3>
        <input v-model="user" placeholder="Account">
        <input type="password" v-model="pass" placeholder="Password">
        <button @click="submit">เข้าสู่ระบบ</button>

    </div>

</template>

<style>
</style>