<template>
  <div id='bind'>
    <form>
      <input v-model="join_email" type="email" placeholder="邮箱">
      <input v-model="join_password" type="password" placeholder="密码">
      <button @click="register">绑定</button>
    </form>
  </div>
</template>
<script>
    import {error} from 'util'

    export default {
        name: 'bind',
        data: function () {
            return {
                join_email: '',
                join_password: '',
                uid: ''
            }
        },
        methods: {
            register: function () {
                alert(this.uid)
                this.axios({
                    url: '/api/thirdLog/',
                    method: 'post',
                    data: {
                        'username': this.join_email,
                        'password': this.join_password,
                        'uid': this.uid
                    }
                }).then((res) => {
                    if (res.data.code == 200) {
                        alert('绑定成功')
                        localStorage.setItem('token', res.data.token);
                        localStorage.setItem('user_id', res.data.user_id);
                        localStorage.setItem('username', res.data.username);
                        this.$router.push({
                            name: 'index',
                        })
                    } else {
                        alert('绑定失败')
                    }
                })

            }
        },
        mounted() {


        },

    }
</script>
