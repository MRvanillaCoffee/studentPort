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

    <div class="login-card d-flex justify-content-center">

        <div class="login-form mt-5">

      <h3>กรุณาป้อน ICIT Account</h3>

      <form @submit.prevent="submit">

        <div class="row">
          <div class="col-12">
            <input v-model="user"
                   placeholder="Account"
                   class="form-control">
          </div>
        </div>

        <div class="row mt-3">
          <div class="col-12">
            <input type="password"
                   v-model="pass"
                   placeholder="Password"
                   class="form-control">
          </div>
        </div>

        <button
          type="button"
          @click="submit"
          class="btn btn-primary mt-3"
        >
          เข้าสู่ระบบ
        </button>

      </form>

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