<template>
  <div id="header1">
    <nav class="navbar navbar-default navbar-fixed-top header">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                  data-target="#header-navbar-collapse" aria-expanded="false">
            <span class="sr-only">实验楼</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/">
            <img src="/static/img/logo_03.png">
          </a>
        </div>
        <div class="collapse navbar-collapse" id="header-navbar-collapse">
          <ul class="nav navbar-nav">
            <li class="dropdown ">
              <router-link :to="{'name':'course'}">课程
                <span class="caret"></span></router-link>
              <ul class="dropdown-menu">
                <!--                <li><a class="" href="#">全部课程</a></li>-->
                <router-link :to="{'name':'course'}">全部课程</router-link>

              </ul>
            </li>
            <li class="">
              <router-link :to="{'name':'path'}">路径</router-link>
            </li>
            <li class="">
              <router-link :to="{'name':'trainingcamp'}">训练营</router-link>
            </li>
            <li class="">
              <router-link :to="{'name':'questions'}">讨论区</router-link>
            </li>
            <li class=" bootcamp new-nav logo-1111">
              <router-link :to="{'name':'BootCamp'}">秒杀</router-link>
            </li>
            <li class=" new-nav logo-1111">
              <router-link :to="{'name':'member'}">会员</router-link>
            </li>
            <li class=" new-nav logo-1111" v-show="user_id != undefined">
              <router-link class="" :to="{'name':'userCenter'}">用户 {{username}}</router-link>
            </li>

          </ul>

          <div class="navbar-right btns">

            <div v-show="user_id==undefined"><a class="btn btn-default navbar-btn sign-in" data-sign="signin"
                                                href="#sign-modal" data-toggle="modal" @click="autoLog"
            >登录</a>
              <a class="btn btn-default navbar-btn sign-up" data-sign="signup" href="#sign-modal"
                 data-toggle="modal">注册</a></div>
            <div class="btn btn-default navbar-btn" v-show="user_id !=undefined" @click="logout">退出登录</div>
          </div>


          <form class="navbar-form navbar-right" action="redisearch" method="get" role="key">
            <div class="form-group">
              <input type="text" class="form-control" name="search" autocomplete="off" placeholder="搜索 课程/问答">
            </div>
          </form>
        </div>

      </div>
    </nav>
    <div class="modal fade" id="sign-modal" tabindex="-1" role="dialog">
      <div class="modal-dialog modal-sm" role="document">
        <div class="modal-content">
          <button type="button" class="close-modal" data-dismiss="modal" aria-label="Close"><span aria-hidden="c1">&times;</span>
          </button>
          <div class="modal-body">
            <ul class="nav nav-tabs" role="tablist">
              <li role="presentation" class="active">
                <a href="#signin-form" role="tab" data-toggle="tab">登录</a>
              </li>
              <li role="presentation">
                <a href="#signup-form" aria-controls="signup-form" role="tab" data-toggle="tab">注册</a>
              </li>
            </ul>
            <div class="tab-content">
              <div role="tabpanel" class="tab-pane active" id="signin-form">
                <!--                <form action="/login" method="post">-->
                <div class="form-group">
                  <div class="input-group">
                    <div class="input-group-addon">
                      <i class="fa fa-envelope" style="margin:0;"></i>
                    </div>
                    <input type="email" v-model="regForm.email" class="form-control" placeholder="请输入邮箱">
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-group">
                    <div class="input-group-addon">
                      <i class="fa fa-lock" style="margin:0;"></i>
                    </div>
                    <input type="password" v-model="regForm.password" class="form-control" placeholder="请输入密码">
                  </div>
                </div>
                <div class="form-group remember-login">
                  <input name="remember" type="checkbox" v-model="rememberPassword"> 下次自动登录
                  <a class="pull-right" href="/Forgetpwd">忘记密码？</a>
                </div>
                <div class="form-group">
                  <input class="btn btn-primary" type="submit" @click="log" value="进入实验楼">
                </div>
                <div class="form-group widget-signin">
                  <span>快速登录</span>
                  <a href="/api/login/"><i class="fa fa-weibo"></i></a>
                </div>
                <div class="form-group error-msg" id="flash-message">
                  <div class="alert alert-danger" role="alert"></div>
                </div>
                <!--                </form>-->
              </div>
              <div role="tabpanel" class="tab-pane" id="signup-form">
                <!--                <form action="http://127.0.0.1:8000/reg" method="post">-->
                <div class="form-group">
                  <div class="input-group">
                    <div class="input-group-addon">
                      <i class="fa fa-envelope" style="margin:0;"></i>
                    </div>
                    <input type="email" v-model="regForm.email" class="form-control" placeholder="请输入邮箱">
                  </div>
                </div>
                <div class="form-group">
                  <div class="input-group">
                    <div class="input-group-addon">
                      <i class="fa fa-lock" style="margin:0;"></i>
                    </div>
                    <input type="password" v-model="regForm.password" class="form-control" placeholder="请输入密码">
                  </div>
                </div>
                <div class="form-inline">
                  <div class="form-group">
                    <div class="input-group">
                      <input type="text" v-model="regForm.image_code" class="form-control" placeholder="请输入验证码">
                    </div>
                  </div>
                  <img class="get_msg_code"
                       src="/api/getimagecode/"
                       height="50" width="100"
                       onclick="this.src=this.src+'?'+Math.random()">
                  <!--                  <img class="verify-code" src="/api/getimagecode/" width="100" height="40">-->
                </div>
                <div class="form-group">
                  <input class="btn btn-primary" name="submit" type="submit" value="注册" @click="reg">
                </div>
                <div class="form-group agree-privacy">
                  注册表示您已经同意我们的<a href="privacy/index.html" target="_blank">隐私条款</a>
                </div>
                <div class="form-group widget-signup">
                  <span>快速注册</span>
                  <a href="/auth/qq?next="><i class="fa fa-qq"></i></a>
                  <a href="/auth/weibo?next="><i class="fa fa-weibo"></i></a>
                  <a href="/auth/weixin?next="><i class="fa fa-weixin"></i></a>
                  <a href="/auth/github?next="><i class="fa fa-github"></i></a>
                  <a href="/auth/renren?next="><i class="fa fa-renren"></i></a>
                </div>
                <div class="form-group error-msg">
                  <div class="alert alert-danger" role="alert"></div>
                </div>
                <!--                </form>-->
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
        name: "header1",
        data: function () {
            return {
                username: '',
                user_id: '',
                regForm: {
                    email: '',
                    password: '',
                    image_code: '',
                    c1: true

                },
                rememberPassword: false,
                courses: [],
                paths: [],
                isRouterAlive: true
            }
        },
        methods: {
            reg: function () {
                if (this.regForm.password.length < 8 || this.regForm.password.length > 20) {
                    alert('密码最少8位，最长20位')
                }
                var regEmail = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
                if (this.regForm.email === '') {
                    alert('邮箱为空')
                } else if (!regEmail.test(this.regForm.email)) {
                    alert('邮箱格式错误')
                }
                if (this.regForm.image_code.length !== 4) {
                    alert('验证码长度错误')
                }
                this.axios({
                    url: '/api/reg/',
                    method: 'post',
                    data: this.regForm
                }).then((res) => {
                    $('#sign-modal').modal('hide')
                    this.regForm.password = '';
                    this.regForm.image_code = '';
                    if (res.data.code == 200) {
                    } else {
                        alert(res.data.message)
                    }
                })
            },
            log: function () {
                if (this.regForm.password.length < 8 || this.regForm.password.length > 20) {
                    alert('密码最少8位，最长20位')
                }
                var regEmail = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
                if (this.regForm.email === '') {
                    alert('邮箱为空')
                } else if (!regEmail.test(this.regForm.email)) {
                    alert('邮箱格式错误')
                }
                this.regForm.username = this.regForm.email;
                this.axios({
                    url: '/api/login/',
                    method: 'post',
                    data: this.regForm
                }).then((res) => {
                    if (res.data.code == 200) {
                        localStorage.setItem('token', res.data.token);
                        localStorage.setItem('user_id', res.data.uid);
                        localStorage.setItem('username', res.data.username);
                        this.user_id = localStorage.getItem('user_id')
                        $('#sign-modal').modal('hide')
                        if (this.rememberPassword == true) {
                            localStorage.setItem('rememberPassword', this.rememberPassword)
                            localStorage.setItem('password', this.regForm.password);
                            localStorage.setItem('username', this.regForm.username);
                        }
                    } else {
                        alert(res.data.message)
                    }
                })
            },

            autoLog: function () {
                var p = localStorage.getItem('password');
                if (p != null && localStorage.getItem('user_id') == undefined) {
                    this.axios({
                        url: '/api/login/',
                        method: 'post',
                        data: {'username': localStorage.getItem('username'), 'password': p}
                    }).then((res) => {
                        if (res.data.code == 200) {
                            localStorage.setItem('token', res.data.token);
                            localStorage.setItem('user_id', res.data.uid);
                            localStorage.setItem('username', res.data.username);
                            this.user_id = localStorage.getItem('user_id')
                            if (res.data.message != undefined) {
                                alert('自动' + res.data.message)
                            }
                        } else {
                            if (res.data.message != undefined) {
                                alert('自动' + res.data.message)
                            }
                        }
                    })
                }
            },
            logout: function () {
                localStorage.removeItem('user_id')
                localStorage.removeItem('token')
                this.user_id = localStorage.getItem('user_id')
            }

        },
        mounted() {
            this.username = localStorage.getItem('username');
            this.password = localStorage.getItem('password');
            this.user_id = localStorage.getItem('user_id');
            this.rememberPassword = localStorage.getItem('rememberPassword');
            if (this.user_id == undefined && this.username != undefined && this.password != undefined && this.rememberPassword) {
                this.autoLog()
            }

        }
    }
</script>

<style scoped>

</style>
