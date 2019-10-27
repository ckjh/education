<template>
  <div id="weibocallback">
    正在跳转...
  </div>
</template>
<script>
    import header1 from '@/components/header1'
    import footer1 from '@/components/footer1'

    export default {
        name: 'weibocallback',
        components: {
            header1: header1,
            footer1: footer1
        },
        mounted() {
            let code = this.$route.query.code;
            // alert(code)
            this.axios({
                url: '/api/thirdLog/',
                method: 'put',
                data: {
                    'code': code
                }
            }).then((res) => {
                if (res.data.code == 200) {
                    alert('登陆成功')
                    localStorage.setItem('token', res.data.token);
                    localStorage.setItem('user_id', res.data.user_id);
                    localStorage.setItem('username', res.data.username);
                    this.$router.push({
                        name: 'index',
                    })
                } else {
                    let uid = res.data.uid;
                    alert(res.data.code)
                    this.$router.push({
                        name: 'bindweibo',
                        query: {uid: uid}
                    })
                }
            })
        },

    }
</script>
