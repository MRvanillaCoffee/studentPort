<script>
    export default {
        data(){
        return{
            username:"",
            password:""
        }
        },
        methods:{
        login(){
            if(this.username && this.password){
            this.$router.push("/")
            }
        }
        }
    }
</script>

    <template>

    <div class="login-card">

    <h3>กรุณากรอก ICIT Account</h3>

    <input v-model="username" placeholder="Account">

    <input type="password" v-model="password" placeholder="Password">

    <button @click="login">
    เข้าสู่ระบบ
    </button>

</div>

</template>