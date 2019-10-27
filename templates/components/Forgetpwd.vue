<template>
  <div>
    <header1></header1>
    <link rel="stylesheet" type="text/css" href="../../static/jquery/style.css">
    <body>
    <div id="content">
      <div class="login-header">
        <h2> 找回帐号密码</h2>
      </div>

      <div class="login-input-box">
        <span class="icon icon-user"></span>
        邮&nbsp;&nbsp;箱:&nbsp;<input type="text" v-model="email" placeholder="Please enter your email/phone">
      </div>
      <p></p>
      <div class="login-input-box">
        <span class="icon icon-password"></span>
        验证码:<input type="text" v-model="image_code" placeholder="Please enter your image_code">
        <img src="/api/getimagecode/" onclick='this.src=this.src+"?"+Math.random()' style='width:100px;height:60px;'>
      </div>
      <div class="login-button-box">
        <button @click="is_valid">立即验证</button>
      </div>
      <div>{{message}}</div>
    </div>
    </body>
    <footer1></footer1>
  </div>

</template>
<script>
    import axios from 'axios';
    import header1 from "@/components/header1";
    import footer1 from "@/components/footer1";

    export default {
        data() {
            return {
                email: '',
                image_code: '',
                message: ''
            }

        },
        components: {
            header1: header1,
            footer1: footer1
        },
        methods: {
            is_valid: function () {

                this.axios.post('/api/forgetpwd/', {'email': this.email, 'image_code': this.image_code}).then(res => {
                    if (res.data.code == 200) {
                        this.message = res.data.message
                    } else {
                        this.message = res.data.message
                    }
                })
            }
        }
    }
</script>
